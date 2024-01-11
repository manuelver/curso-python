#!/usr/bin/env python3
"""
Validar correo con regex
"""

import re

def validar_correo(correo):

    patron = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b"

    if re.findall(patron, correo):
        return True
    
    return False

print(validar_correo("invent@hacko.io"))
