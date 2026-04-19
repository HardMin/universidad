"""
5. Analizador de Texto Corporativo

Solicite un párrafo. El script debe contar cuántas palabras tiene y extraer la
palabra más larga utilizada.
"""

texto = input("Ingrese un parrafo: ")
palabras = texto.split(" ")
palabra_larga = max(palabras, key=len)

print(
    f"El Parrafo tiene {len(palabras)} palabras, la palabra más larga es '{palabra_larga}'."
)
