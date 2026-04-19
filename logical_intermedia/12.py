"""
12. Simulador de Cajero Automático

Cree un programa con un saldo inicial. Permita retirar dinero solo si hay
fondos suficientes y maneje el error si se ingresa un monto no numérico.
"""

saldo = 10000


def entrada():
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            if monto > 0:
                return monto
        except ValueError:
            pass
        print("\nDebe ser numérico y mayor que cero.")


def opciones():
    while True:
        try:
            opcion = input("\n1: Retirar\n2: Salir\n> ")
            if opcion == "1" or opcion == "2":
                return opcion
        except ValueError:
            pass
        print("\nOpción inválida. Por favor, ingrese 1 o 2.")


def retirar(monto):
    global saldo
    if saldo < monto:
        print("\nNo hay fondos suficientes.")
        return
    saldo -= monto
    print(f"\nRetirado: {monto}")


print("CAJERO AUTOMÁTICO")
print("-" * 30)
print(f"Saldo: {saldo}")
print("-" * 30)
print("\n\n")
while True:
    monto = entrada()
    retirar(monto)
    if saldo == 0:
        break
    print(f"\nSaldo: {saldo}")

    if opciones() == "2":
        break
