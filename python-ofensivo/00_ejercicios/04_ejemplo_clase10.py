#!/usr/bin/env python3
"""
Clases subclases y herencia
"""


class Dispositivo:

    def __init__(self, modelo):

        self.modelo = modelo

    def escanear_vulnerabilidades(self):

        raise NotImplementedError("Este método debe ser definido para el resto de subclases existentes")

class Ordenador(Dispositivo):

    def escanear_vulnerabilidades(self):

        return f"[+] Análisis de vulnerabilidades concluido: Actualización de sowfware necesaria, múltiples desactualizaciones de software detectadas"

class Router(Dispositivo):

    def escanear_vulnerabilidades(self):

        return f"[+] Análisis de vulnerabilidades concluido: Múltiples puertos críticos abiertos, es recomendable cerrar estos puertos"

class TelefonoMovil(Dispositivo):

    def escanear_vulnerabilidades(self):

        return f"[+] Análisis de vulnerabilidades concluido: Múltipleas aplicaciones detectadas con permisos excesivos"


def realizar_escaneo(dispositivo):

    print(dispositivo.escanear_vulnerabilidades())

pc = Ordenador("Dell XPS")
router = Router("TP-Link Archer C50")
movil = TelefonoMovil("Xiaomi Galaxy S21")

realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)
