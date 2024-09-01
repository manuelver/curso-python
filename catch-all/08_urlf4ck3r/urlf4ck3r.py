#!/usr/bin/env python3

import argparse
import os
import requests
import signal
import sys

from bs4 import BeautifulSoup, Comment
from collections import defaultdict
from urllib.parse import urljoin, urlparse
from typing import Optional, Tuple, Dict, List, Set


class URLf4ck3r:
    """
    URLf4ck3r es una herramienta que extrae las URL's del código fuente de una
    página web. Además, puede extraer comentarios sensibles del código fuente
    y guardar las URL's en archivos de texto.
    """

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GRAY = "\033[90m"
    PURPLE = "\033[95m"
    END_COLOR = "\033[0m"

    SENSITIVE_KEYWORDS = [
        # Palabras clave originales
        "password", "user", "username", "clave", "secret", "key", "token", 
        "private", "admin", "credential", "login", "auth", "api_key", "apikey", 
        "administrator",

        # # Criptografía y Seguridad
        # "encryption", "decrypt", "cipher", "security", "hash", "salt", "ssl", 
        # "tls", "secure", "firewall", "integrity",

        # # Gestión de Usuarios y Autenticación
        # "auth_token", "session_id", "access_token", "oauth", "id_token", 
        # "refresh_token", "csrf", "sso", "two_factor", "2fa",

        # # Información Personal Identificable (PII)
        # "social_security", "ssn", "address", "phone_number", "email", "dob", 
        # "credit_card", "card_number", "ccv", "passport", "tax_id", "personal_info",

        # # Configuración de Sistemas
        # "config", "database", "db_password", "db_user", "connection_string", 
        # "server", "host", "port",

        # # Archivos y Rutas
        # "filepath", "filename", "root_path", "home_dir", "backup", "logfile",

        # # Llaves y Tokens de API
        # "aws_secret", "aws_key", "api_secret", "secret_key", "private_key", 
        # "public_key", "ssh_key",

        # # Finanzas y Pagos
        # "payment", "transaction", "account_number", "iban", "bic", "swift", 
        # "bank", "routing_number", "billing", "invoice",

        # # Cuentas y Roles de Administrador
        # "superuser", "root", "sudo", "admin_password", "admin_user",

        # # Otros
        # "jwt", "cookie", "session", "bypass", "debug", "exploit"
    ]


    def __init__(self):
        """
        Inicializa las variables de instancia.
        """

        self.all_urls: Dict[str, Set[str]] = defaultdict(set)
        self.comments_data: Dict[str, List[str]] = defaultdict(list)
        self.base_url: Optional[str] = None
        self.urls_to_scan: List[str] = []
        self.flag = self.Killer()
        self.output: Optional[str] = None


    def banner(self) -> None:
        """
        Muestra el banner de la herramienta.
        """

        print("""
            
 █    ██  ██▀███   ██▓      █████▒▄████▄   ██ ▄█▀ ██▀███  
 ██  ▓██▒▓██ ▒ ██▒▓██▒    ▓██   ▒▒██▀ ▀█   ██▄█▒ ▓██ ▒ ██▒
▓██  ▒██░▓██ ░▄█ ▒▒██░    ▒████ ░▒▓█    ▄ ▓███▄░ ▓██ ░▄█ ▒
▓▓█  ░██░▒██▀▀█▄  ▒██░    ░▓█▒  ░▒▓▓▄ ▄██▒▓██ █▄ ▒██▀▀█▄  
▒▒█████▓ ░██▓ ▒██▒░██████▒░▒█░   ▒ ▓███▀ ░▒██▒ █▄░██▓ ▒██▒
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒ ░   ░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒▓ ░▒▓░
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░ ░       ░  ▒   ░ ░▒ ▒░  ░▒ ░ ▒░
 ░░░ ░ ░   ░░   ░   ░ ░    ░ ░   ░        ░ ░░ ░   ░░   ░ 
   ░        ░         ░  ░       ░ ░      ░  ░      ░     
                                 ░                        
""")


    def run(self) -> None:
        """
        Ejecuta la herramienta.
        """

        self.banner()

        args, parser = self.get_arguments()

        if not args.url:
            parser.print_help()
            sys.exit(1)

        if args.output:
            self.output = args.output

        self.base_url = args.url
        self.all_urls["scanned_urls"] = set()
        self.urls_to_scan = [self.base_url]

        _, domain, _ = self.parse_url(self.base_url)

        print(f"\n[{self.GREEN}DOMAIN{self.END_COLOR}] {domain}\n")

        while self.urls_to_scan and not self.flag.exit():
            url = self.urls_to_scan.pop(0)
            self.scan_url(url)

        print()
        self.show_lists()
        self.save_files()

        print(f"\n[{self.GREEN}URLS TO SCAN{self.END_COLOR}]:")

        if self.flag.exit():
            print(
                f"[{self.RED}!{self.END_COLOR}] Quedaron por escanear {self.RED}{len(self.urls_to_scan)}{self.END_COLOR} URLs"
            )

        elif not self.urls_to_scan:
            print(
                f"[{self.GREEN}+{self.END_COLOR}] Se escanearon todas las URLs posibles"
            )
        else:
            print(
                f"[{self.RED}!{self.END_COLOR}] Quedaron por escanear {self.RED}{len(self.urls_to_scan)}{self.END_COLOR} URLs"
            )


    def get_arguments(self) -> Tuple[argparse.Namespace, argparse.ArgumentParser]:
        """
        Obtiene los argumentos proporcionados por el usuario.
        """

        parser = argparse.ArgumentParser(
            prog="urlf4ck3r",
            description="Extraer las URL's del código fuente de una web",
            epilog="Creado por https://github.com/n0m3l4c000nt35 y modificado por gitea.vergaracarmona.es/manuelver"
        )
        parser.add_argument("-u", "--url", type=str, dest="url",
                            help="URL a escanear", required=True)
        parser.add_argument("-o", "--output", type=str,
                            dest="output", help="Nombre del archivo de salida")

        return parser.parse_args(), parser

    def scan_url(self, url: str) -> None:
        """
        Escanea una URL en busca de URLs, comentarios sensibles y archivos JS.
        """

        if self.flag.exit():
            return

        if url in self.all_urls["scanned_urls"]:
            return

        self.all_urls["scanned_urls"].add(url)
        print(f"[{self.GREEN}SCANNING{self.END_COLOR}] {url}")

        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.content, 'html.parser')

            self.extract_js_files(soup, url)
            self.extract_comments(soup, url)
            self.extract_hrefs(soup, url, res)

        except requests.Timeout:
            print(f"[{self.RED}REQUEST TIMEOUT{self.END_COLOR}] {url}")
            self.all_urls['request_error'].add(url)

        except requests.exceptions.RequestException:
            print(f"{self.RED}[REQUEST ERROR]{self.END_COLOR} {url}")
            self.all_urls['request_error'].add(url)

        except Exception as e:
            print(
                f"[{self.RED}UNEXPECTED ERROR{self.END_COLOR}] {url}: {str(e)}"
            )


    def extract_hrefs(self, soup: BeautifulSoup, url: str, res: requests.Response) -> None:
        """
        Extrae las URL's del código fuente de una página web.
        """

        for link in soup.find_all("a", href=True):
            href = link.get("href")
            scheme, domain, path = self.parse_url(href)
            schemes = ["http", "https"]

            if href:
                full_url = urljoin(url, path) if not scheme else href

                if full_url not in self.all_urls["all_urls"]:
                    self.all_urls["all_urls"].add(full_url)

                if not scheme:
                    self.all_urls["relative_urls"].add(full_url)

                else:
                    self.all_urls["absolute_urls"].add(full_url)

                if self.is_jsfile(url, res):
                    self.all_urls["javascript_files"].add(url)

                if (self.is_internal_url(self.base_url, full_url) or
                        self.is_subdomain(self.base_url, full_url)):

                    if full_url not in self.all_urls["scanned_urls"] and full_url not in self.urls_to_scan:
                        self.urls_to_scan.append(full_url)


    def extract_js_files(self, soup: BeautifulSoup, base_url: str) -> None:
        """
        Extrae los archivos JS del código fuente de una página web.
        """

        js_files = set()

        for script in soup.find_all('script', src=True):

            js_url = script['src']

            if not urlparse(js_url).netloc:

                js_url = urljoin(base_url, js_url)

            js_files.add(js_url)

        self.all_urls["javascript_files"].update(js_files)


    def is_jsfile(self, url: str, res: requests.Response) -> bool:
        """
        Verifica si un archivo es un archivo JS.
        """

        return url.lower().endswith(('.js', '.mjs')) or 'javascript' in res.headers.get('Content-Type', '').lower()


    def extract_subdomain(self, url: str) -> str:
        """
        Extrae el subdominio de una URL.
        """

        netloc = urlparse(url).netloc.split(".")

        return ".".join(netloc[1:] if netloc[0] == "www" else netloc)


    def is_subdomain(self, base_url: str, url: str) -> bool:
        """
        Verifica si una URL es un subdominio del dominio base.
        """

        base_domain = self.extract_subdomain(base_url)
        sub = self.extract_subdomain(url)

        return sub.endswith(base_domain) and sub != base_domain


    def is_internal_url(self, base_url: str, url: str) -> bool:
        """
        Verifica si una URL es interna (pertenece al mismo dominio).
        """

        return urlparse(base_url).netloc == urlparse(url).netloc


    def extract_comments(self, soup: BeautifulSoup, url: str) -> None:
        """
        Extrae los comentarios del código fuente de una página web.
        """

        comments = soup.find_all(string=lambda text: isinstance(text, Comment))

        for comment in comments:

            comment_str = comment.strip()

            if any(keyword in comment_str.lower() for keyword in self.SENSITIVE_KEYWORDS):
                self.comments_data[url].append(comment_str)
                print(
                    f"{self.YELLOW}[SENSITIVE COMMENT FOUND]{self.END_COLOR} {comment_str}"
                )


    def parse_url(self, url: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Parsea una URL y devuelve el esquema, dominio y path.
        """

        parsed_url = urlparse(url)

        return parsed_url.scheme, parsed_url.netloc, parsed_url.path



    def ensure_directory_exists(self, directory: str) -> None:
        """
        Asegura que el directorio existe, y lo crea si no es así.
        """

        if not os.path.exists(directory):
            os.makedirs(directory)


    def save_file(self, data: List[str], filename: str) -> None:
        """
        Guarda los datos en un archivo.
        """

        try:
            # Asegurarse de que el directorio 'output' existe
            self.ensure_directory_exists("output")
            
            if self.output:
                filename = f"{self.output}_{filename}"

            filepath = os.path.join("output", filename)
            
            with open(filepath, "w") as f:
                f.write("\n".join(data))

            print(f"[{self.GREEN}+{self.END_COLOR}] Guardado en {filepath}")

        except IOError as e:
            print(
                f"{self.RED}[FILE WRITE ERROR]{self.END_COLOR} No se pudo guardar el archivo {filename}: {str(e)}"
            )


    def save_files(self) -> None:
        """
        Guarda las URLs y los comentarios extraídos en archivos.
        """
        self.save_file(
            sorted(self.all_urls["all_urls"]),
            "all_urls.txt"
        )

        self.save_file(
            sorted(self.all_urls["absolute_urls"]), 
            "absolute_urls.txt"
        )

        self.save_file(
            sorted(self.all_urls["relative_urls"]), 
            "relative_urls.txt"
        )

        self.save_file(
            sorted(self.all_urls["javascript_files"]), 
            "javascript_files.txt"
        )

        if self.comments_data:
            sensitive_comments = []

            for url, comments in self.comments_data.items():
                sensitive_comments.append(f"\n[ {url} ]\n")
                sensitive_comments.extend(comments)

            self.save_file(sensitive_comments, "sensitive_comments.txt")


    def show_lists(self) -> None:
        """
        Muestra el resumen de las URLs extraídas.
        """

        print(
            f"\n[{self.GREEN}ALL URLS{self.END_COLOR}]: {len(self.all_urls['all_urls'])}"
        )
        print(
            f"[{self.GREEN}ABSOLUTE URLS{self.END_COLOR}]: {len(self.all_urls['absolute_urls'])}"
        )
        print(
            f"[{self.GREEN}RELATIVE URLS{self.END_COLOR}]: {len(self.all_urls['relative_urls'])}"
        )
        print(
            f"[{self.GREEN}JAVASCRIPT FILES{self.END_COLOR}]: {len(self.all_urls['javascript_files'])}"
        )
        print(
            f"[{self.GREEN}SENSITIVE COMMENTS{self.END_COLOR}]: {len(self.comments_data)}"
        )

    class Killer:
        """
        Clase utilizada para manejar la interrupción del script con Ctrl+C.
        """

        kill_now = False


        def __init__(self):

            signal.signal(signal.SIGINT, self.exit_gracefully)


        def exit_gracefully(self, signum, frame) -> None:
            """
            Método llamado cuando se recibe la señal de interrupción.
            """

            self.kill_now = True

        def exit(self) -> bool:
            """
            Retorna True si el script debe terminar.
            """

            return self.kill_now


if __name__ == "__main__":

    tool = URLf4ck3r()
    tool.run()
