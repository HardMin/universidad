"""
1. Validador de Lote de Productos

Solicite una lista de códigos de productos. El programa debe filtrar y mostrar
solo aquellos que comiencen con la letra "A" y tengan exactamente 5 dígitos.
"""

codigos_productos = []
codigos_generados = [
    "A5921",
    "C88219",
    "A1024",
    "R5502183",
    "A4412",
    "J221",
    "A7730",
    "L10293",
    "A2290",
    "G881203",
    "B902",
    "A3341",
    "X7712",
    "A9902",
    "M120934",
    "A0012",
    "H55210",
    "A6615",
    "F441920",
    "A4481",
    "A1108",
    "Z9920114",
    "A6672",
    "K44102",
    "A8823",
    "P55120",
    "A3391",
    "Q1029",
    "A5540",
    "T772109",
]


def menu_opciones(msj_1, msj_2="Salir"):
    while True:
        try:
            opcion = int(input(f"\n1: {msj_1} \n2: {msj_2} \n\n> "))

            if opcion == 2 or opcion == 1:
                print("\n")
                return opcion
        except ValueError:
            print("Ingrese una opcion válida")


def ingresar_codigos():
    while True:
        codigo = input("Ingrese un código de producto: ")
        codigos_productos.append(codigo)
        print(codigos_productos)

        if menu_opciones("Ingresar otro codigo") == 2:
            break


match menu_opciones("Codigos Generados", "Introducir codigos"):
    case 1:
        codigos_productos = codigos_generados
    case 2:
        ingresar_codigos()


codigos_filtrados = []

for codigos in codigos_productos:
    if codigos.upper().startswith("A") and len(codigos) == 5:
        codigos_filtrados.append(codigos)

print(f"Lista de códigos filtrados: {codigos_filtrados}")
