# /var/bin/env python3
"""
Utilizo esta web:
https://www.el-tiempo.net/api

Contiene una serie de APIs para consultar el tiempo. 
- Escoger provincia: https://www.el-tiempo.net/api/json/v2/provincias/[CODPROV]
- Lista municipio: https://www.el-tiempo.net/api/json/v2/provincias/[CODPROV]/municipios
- Escoger municipio: https://www.el-tiempo.net/api/json/v2/provincias/[CODPROV]/municipios/[ID]

"""

import json
import os
import requests
import signal
import sys

from termcolor import colored


def signal_handler(sig, frame):
    print(colored("Saliendo...", "red"))
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


# CONSTANTES
SPAIN_URL = "https://www.el-tiempo.net/api/json/v2/home"
PROVINCIAS_URL = "https://www.el-tiempo.net/api/json/v2/provincias"


def LimpiarPantalla():
    """
    Limpiar la pantalla
    """

    os.system("clear")

def Pausa():
    """
    Esperar 2 segundos
    """

    os.system("sleep 2")


def RequestUrl(url):
    """
    Realizar una petición GET a una URL y devolver el JSON
    """

    try:

        r = requests.get(url)
        r.raise_for_status()  # Excepción de códigos de estado HTTP no exitosos

        return r.json()

    except requests.exceptions.RequestException as e:

        print(colored(f"[!] Error al obtener los datos de {url}: {e}", "red"))
        sys.exit(1)


def ExtraerProvinciasData():
    """
    Extraer todas las provincias disponibles
    """

    dic_id_codprov_provincias = {}

    provincias_data_request = RequestUrl(PROVINCIAS_URL)

    provincias_data = provincias_data_request["provincias"]

    for i, provincia_data in enumerate(provincias_data):

        id = i+1
        codprov = provincia_data["CODPROV"]
        provincia = provincia_data["NOMBRE_PROVINCIA"]
        dic_id_codprov_provincias[id] = {
            'codprov': codprov, 'provincia': provincia
        }

        print(colored(f"{id} - {provincia_data['NOMBRE_PROVINCIA']}", "cyan"))

    return dic_id_codprov_provincias


def SeleccionarProvincia(dic_id_codprov_provincias):
    """
    Seleccionar una provincia
    """

    prov_selec = input(colored(
        "[+] Selecciona el número de una provincia: ", "magenta"
    ))

    nombre_prov_selec = dic_id_codprov_provincias[int(prov_selec)]['provincia']

    print(colored(
        f"\n[+] Has seleccionado la provincia: {nombre_prov_selec}\n", "green")
    )

    Pausa()
    LimpiarPantalla()

    return dic_id_codprov_provincias[int(prov_selec)]['codprov']


def ExtrarMunicipiosData(cod_prov):
    """
    Extraer todos los municipios de una provincia
    """

    dic_id_codmun_municipio = {}

    municipios_url = f"{PROVINCIAS_URL}/{cod_prov}/municipios"

    municipios_data_request = RequestUrl(municipios_url)

    municipios_data = municipios_data_request["municipios"]

    for i, municipio_data in enumerate(municipios_data):

        id = i+1
        codmun = municipio_data["CODIGOINE"][0:5]
        municipio = municipio_data['NOMBRE']
        dic_id_codmun_municipio[id] = {
            'codmun': codmun, 'municipio': municipio
        }

        print(colored(f"{id} - {municipio_data['NOMBRE']}", "cyan"))

    return dic_id_codmun_municipio


def SeleccionarMunicipio(dic_id_codmun_municipio):

    mun_selec = input(colored(
        "[+] Selecciona el número de un municipio: ", "magenta"
    ))

    nombre_mun_selec = dic_id_codmun_municipio[int(mun_selec)]['municipio']

    print(colored(
        f"\n[+] Has seleccionado el municipio: {nombre_mun_selec}\n", "green"
    ))

    Pausa()
    LimpiarPantalla()

    return dic_id_codmun_municipio[int(mun_selec)]['codmun']


def InfoTiempo(cod_prov, cod_mun):

    url_tiempo = f"{PROVINCIAS_URL}/{cod_prov}/municipios/{cod_mun}"

    tiempo_data_request = RequestUrl(url_tiempo)

    titulo = tiempo_data_request["metadescripcion"]
    fecha = tiempo_data_request["fecha"]

    hora_amanecer = tiempo_data_request["orto"]
    hora_ocaso = tiempo_data_request["ocaso"]

    estado_cielo = tiempo_data_request["stateSky"]["description"]

    temp_actual = tiempo_data_request["temperatura_actual"]
    temp_min = tiempo_data_request["temperaturas"]["min"]
    temp_max = tiempo_data_request["temperaturas"]["max"]

    humedad = tiempo_data_request["humedad"]

    print(colored(f"\n[+] {titulo.strip().upper()} A FECHA {fecha}\n", "blue"))

    print(colored(f"[+] Hora de amanecer: {hora_amanecer}", "blue"))
    print(colored(f"[+] Hora de ocaso: {hora_ocaso}\n", "blue"))

    print(colored(f"[+] Estado del cielo: {estado_cielo}\n", "blue"))

    print(colored(f"[+] Temperatura actual: {temp_actual}ºC", "blue"))
    print(colored(f"[+] Temperatura mínima: {temp_min}ºC", "blue"))
    print(colored(f"[+] Temperatura máxima: {temp_max}ºC\n", "blue"))

    print(colored(f"[+] Humedad: {humedad}%\n", "blue"))



def main():

    LimpiarPantalla()

    dic_id_codprov_provincias = ExtraerProvinciasData()

    cod_prov = SeleccionarProvincia(dic_id_codprov_provincias)

    dic_id_codmun_municipio = ExtrarMunicipiosData(cod_prov)

    cod_mun = SeleccionarMunicipio(dic_id_codmun_municipio)

    InfoTiempo(cod_prov, cod_mun)


if __name__ == "__main__":

    main()
