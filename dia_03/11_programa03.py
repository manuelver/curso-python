"""
Programa día 3 - Analizador de text
"""

txt = input("""
Ingresa un texto para analizar
""")

print("\nIngresa tres letras por favor")
l1 = input("\tIngresa la primera letra: ")
l2 = input("\tIngresa la segunda letra: ")
l3 = input("\tIngresa la tercera letra: ")

letras = [l1, l2, l3]

print("\nPRIMERO. Vamos a ver las veces que aparecen las letras en el texto:")
print(f"\t- La letra {l1} se encuentra {txt.lower().count(letras[0].lower())} veces en el texto.")
print(f"\t- La letra {l2} se encuentra {txt.lower().count(letras[1].lower())} veces en el texto.")
print(f"\t- La letra {l3} se encuentra {txt.lower().count(letras[2].lower())} veces en el texto.")

print(f"\nSEGUNDO. El texto tiene {len(txt.split())} palabras.")

pos_pri = txt[0]
pos_fin = txt[-1]
print(f"\nTERCERO. La primera letra del texto es \"{pos_pri}\" y la última es \"{pos_fin}\"")

print(f"\nCUARTO. Cuidao, el texto al revés es así:\n{' '.join(txt[::-1])}")

ser_o_no_ser = ("python" in txt)
dic_si_o_no = {True:"sí",False:"no"}
print(f"\nQUINTO. La palabra python {dic_si_o_no[ser_o_no_ser]} se encuentra en el texto")
