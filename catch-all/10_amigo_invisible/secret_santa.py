#!/usr/bin/env python3
"""
secret_santa.py

Uso básico:
  python secret_santa.py --input participants.csv

Opciones:
  --input PATH        CSV de entrada con columnas: name,email,exclusions (opcional)
  --output PATH       CSV de salida (por defecto assignments.csv)
  --seed INT          Semilla aleatoria (opcional, reproducible)
  --send              Enviar correos vía SMTP (ver opciones siguientes)
  --smtp-server HOST  Servidor SMTP (ej. smtp.gmail.com)
  --smtp-port PORT    Puerto SMTP (ej. 587)
  --smtp-user USER    Usuario SMTP
  --smtp-pass PASS    Contraseña SMTP (mejor usar variable de entorno)
  --subject "..."     Asunto del email (plantilla)
  --body "..."        Cuerpo (plantilla)
  --max-attempts N    Intentos máximos para buscar emparejamiento (por defecto 10000)
"""

import csv
import random
import argparse
import sys
import smtplib
import os
import logging
from email.message import EmailMessage
from typing import List, Dict, Tuple, Set
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Configuración del logger con niveles detallados
logging.basicConfig(
    level=logging.os.getenv('LOG_LEVEL', 'INFO').upper(),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('secret_santa.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def read_participants(path: str) -> List[Dict]:
    """Lee el archivo CSV con los participantes y sus exclusiones."""
    participants = []
    try:
        logger.info(f"[i] Abriendo el archivo {path} para leer los participantes.")
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('name') or row.get('Name') or ''
                email = row.get('email') or row.get('Email') or ''
                exclusions_raw = row.get('exclusions') or row.get('Exclusions') or ''
                exclusions = set()
                if exclusions_raw:
                    for item in exclusions_raw.split(';'):
                        s = item.strip()
                        if s:
                            exclusions.add(s.lower())
                participants.append({
                    'name': name.strip(),
                    'email': email.strip().lower(),
                    'exclusions': exclusions
                })
        logger.info(f"[i] Se leyeron {len(participants)} participantes del archivo.")
    except FileNotFoundError:
        logger.error(f"[i] El archivo {path} no fue encontrado.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"[!] Error al leer el archivo CSV: {e}")
        sys.exit(1)
    return participants

def valid_pairing(giver: Dict, recipient: Dict) -> bool:
    """Verifica si una asignación entre giver y recipient es válida."""
    if giver['email'] == recipient['email']:
        logger.debug(f"[!] Invalid pairing: {giver['email']} cannot give to themselves.")
        return False
    if recipient['email'] in giver['exclusions']:
        logger.debug(f"[!] Invalid pairing: {giver['email']} cannot give to {recipient['email']} (exclusion).")
        return False
    if recipient['name'].strip().lower() in giver['exclusions']:
        logger.debug(f"[!] Invalid pairing: {giver['email']} cannot give to {recipient['name']} (exclusion).")
        return False
    return True

def generate_assignments(participants: List[Dict], max_attempts: int = 10000) -> List[Tuple[Dict, Dict]]:
    """Genera las asignaciones de forma aleatoria."""
    n = len(participants)
    if n < 2:
        logger.error("[!] Necesitas al menos 2 participantes.")
        raise ValueError("Necesitas al menos 2 participantes.")
    
    logger.info(f"[i] Generando asignaciones para {n} participantes.")
    indices = list(range(n))
    for attempt in range(max_attempts):
        logger.debug(f"[i] Intentando emparejamiento aleatorio, intento {attempt + 1}.")
        random.shuffle(indices)
        ok = True
        pairs = []
        for i, giver in enumerate(participants):
            recipient = participants[indices[i]]
            if not valid_pairing(giver, recipient):
                ok = False
                break
            pairs.append((giver, recipient))
        if ok:
            logger.info("[i] Asignación generada con éxito.")
            return pairs
    logger.error(f"[!] No fue posible encontrar una asignación válida tras {max_attempts} intentos.")
    sol = backtracking_assign(participants)
    if sol is None:
        logger.critical("[!] No se pudo encontrar una asignación válida ni después del backtracking.")
        raise RuntimeError(f"[!] No fue posible encontrar una asignación válida tras {max_attempts} intentos y búsqueda.")
    return sol

def backtracking_assign(participants: List[Dict]) -> List[Tuple[Dict, Dict]] or None:
    """Intenta asignar los participantes usando backtracking."""
    n = len(participants)
    recipients = list(range(n))
    used = [False]*n
    assignment = [None]*n
    allowed = []
    for giver in participants:
        allowed_list = [j for j, r in enumerate(participants) if valid_pairing(giver, r)]
        allowed.append(allowed_list)
    order = sorted(range(n), key=lambda i: len(allowed[i]))

    logger.debug("[i] Comenzando búsqueda por backtracking.")
    def dfs(pos):
        if pos == n:
            return True
        i = order[pos]
        for j in allowed[i]:
            if not used[j]:
                used[j] = True
                assignment[i] = j
                if dfs(pos+1):
                    return True
                used[j] = False
                assignment[i] = None
        return False

    if dfs(0):
        logger.info("[i] Búsqueda por backtracking exitosa.")
        return [(participants[i], participants[assignment[i]]) for i in range(n)]
    logger.error("[!] Búsqueda por backtracking fallida.")
    return None

def write_assignments_csv(pairs: List[Tuple[Dict, Dict]], path: str):
    """Escribe las asignaciones en un archivo CSV."""
    try:
        logger.info(f"[i] Escribiendo las asignaciones en {path}.")
        with open(path, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['giver_name', 'giver_email', 'recipient_name', 'recipient_email']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for giver, recipient in pairs:
                writer.writerow({
                    'giver_name': giver['name'],
                    'giver_email': giver['email'],
                    'recipient_name': recipient['name'],
                    'recipient_email': recipient['email']
                })
        logger.info(f"[i] Asignaciones guardadas en {path}")
    except Exception as e:
        logger.error(f"[!] Error escribiendo el archivo CSV: {e}")
        sys.exit(1)

def send_emails(pairs: List[Tuple[Dict,Dict]], smtp_config: Dict, subject_template: str, body_template: str):
    """Envía los correos electrónicos a los participantes."""
    server_host = smtp_config['server']
    server_port = smtp_config['port']
    user = smtp_config['user']
    password = smtp_config['pass']

    try:
        logger.info(f"[i] Iniciando conexión con el servidor SMTP {server_host}:{server_port}.")
        with smtplib.SMTP(server_host, server_port) as server:
            server.starttls()
            server.login(user, password)
            for giver, recipient in pairs:
                msg = EmailMessage()
                subject = subject_template.format(
                    giver_name=giver['name'],
                    giver_email=giver['email'],
                    recipient_name=recipient['name'],
                    recipient_email=recipient['email']
                )
                body = body_template.format(
                    giver_name=giver['name'],
                    giver_email=giver['email'],
                    recipient_name=recipient['name'].upper(),
                    recipient_email=recipient['email']
                )
                msg['Subject'] = subject
                msg['From'] = user or server_host
                msg['To'] = giver['email']
                msg.set_content(body)
                server.send_message(msg)
                logger.info(f"[+] Enviado a {giver['email']}")
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"[!] Error de autenticación SMTP: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"[!] Error enviando correos: {e}")
        sys.exit(1)


def read_template_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Amigo Invisible - Emparejador")

    parser.add_argument('--input', default='participants.csv', help='CSV de participantes (name,email,exclusions)')
    parser.add_argument('--output', default='assignments.csv', help='CSV de salida')
    parser.add_argument('--seed', type=int, help='Semilla aleatoria')
    parser.add_argument('--send', action='store_true', default=True, help='Enviar correos vía SMTP')
    parser.add_argument('--smtp-server', default=os.getenv('SMTP_SERVER', 'smtp.gmail.com'), help='Servidor SMTP')
    parser.add_argument('--smtp-port', type=int, default=int(os.getenv('SMTP_PORT', 587)), help='Puerto SMTP')
    parser.add_argument('--smtp-user', default=os.getenv('SMTP_USER'), help='Usuario SMTP')
    parser.add_argument('--smtp-pass', default=os.getenv('SMTP_PASS'), help='Contraseña SMTP')
    parser.add_argument('--subject-template', default='templates/subject.txt', help='Ruta del archivo de asunto')
    parser.add_argument('--body-template', default='templates/body.txt', help='Ruta del archivo de cuerpo')
    parser.add_argument('--max-attempts', type=int, default=10000, help='Max intentos aleatorios antes de fallback')

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    subject_template = read_template_file(args.subject_template)
    body_template = read_template_file(args.body_template)

    logger.info("[i] Iniciando el proceso de emparejamiento de amigos invisibles.")

    participants = read_participants(args.input)
    if len(participants) == 0:
        logger.error("[!] No se encontraron participantes en el CSV.")
        sys.exit(1)

    try:
        pairs = generate_assignments(participants, max_attempts=args.max_attempts)
    except Exception as e:
        logger.error(f"[!] Error generando emparejamientos: {e}")
        sys.exit(1)

    write_assignments_csv(pairs, args.output)
    if args.send:
        smtp_config = {
            'server': args.smtp_server,
            'port': args.smtp_port,
            'user': args.smtp_user,
            'pass': args.smtp_pass
        }
        logger.info("[i] Enviando correos...")
        send_emails(pairs, smtp_config, subject_template, body_template)
        logger.info("[i] Envío finalizado.")

if __name__ == '__main__':
    main()
