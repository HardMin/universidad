"""
7. Sistema de Turnos (Colas)

Simule un sistema de atención al cliente usando una lista. Permita añadir
clientes al final y "atender" al primero de la lista (método pop(0)).
"""

clientes = []


def opciones(msj_1, msj_2):
    while True:
        try:
            opcion = input(f"\n1: {msj_1}\n2: {msj_2}\n> ")
            if opcion == "1" or opcion == "2":
                return opcion
        except ValueError:
            pass
        print("Opción inválida. Por favor, ingrese 1 o 2.")


def agregar_cliente():
    clientes.append(input("\nIngrese el nombre del cliente: "))
    print(f"Clientes: {clientes}")


while True:
    if opciones(msj_1="Agregar cliente", msj_2="Atender cliente") == "1":
        agregar_cliente()
    else:
        if len(clientes) < 1:
            print("\nNo hay clientes en el sistema.")

            if opciones(msj_1="Agregar cliente", msj_2="Salir") == "1":
                agregar_cliente()
            else:
                break
        else:
            print(f"\nAtendiendo {clientes[0]}.")
            clientes.pop(0)
            print(f"Clientes restantes: {clientes or 'No hay clientes'}")
