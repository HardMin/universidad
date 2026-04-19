"""
4. Buscador en Inventario

Implemente un programa que permita buscar un artículo en una lista. Si no
existe, debe capturar el error y ofrecer al usuario la opción de agregarlo.
"""

inventario = [
    "harina",
    "leche",
    "pan",
    "queso",
    "arroz",
    "huevos",
]


def opciones():
    while True:
        try:
            opcion = input("1: Si\n2: No\n> ")
            if opcion == "1" or opcion == "2":
                return opcion
        except ValueError:
            print("Opción inválida. Por favor, ingrese 1 o 2.")


def buscador(nombre):
    try:
        producto = inventario.index(nombre.lower())
        print(f"\nEl artículo '{nombre}' se encuentra en el índice {producto}.\n")
    except ValueError:
        print(f"\nNo existe '{nombre}' en el inventario.\n")
        print("Desea agregarlo?")
        if opciones() == "1":
            inventario.append(nombre)
            print(f"\nAgregado: '{nombre}'\n")


while True:
    nombre = input("Buscar artículo: ")
    buscador(nombre)

    print("Desea buscar otro artículo?")
    if opciones() == "2":
        break
