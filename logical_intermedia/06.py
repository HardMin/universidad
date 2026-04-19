"""
6. Conversor de Monedas con Diccionarios

Utilice un diccionario para almacenar tasas de cambio (USD, EUR, GBP). El
usuario ingresa el monto en moneda local y el programa devuelve la conversión solicitada.
"""

tasa_cambio = {
    1: {"moneda": "USD", "precio": 467.0},
    2: {"moneda": "EUR", "precio": 567.0},
    3: {"moneda": "CO", "precio": 0.0019},
    4: {"moneda": "USDT", "precio": 650.0},
}


def solicitar_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto en Bs: "))
            if monto > 0:
                return monto
        except ValueError:
            print("El monto debe ser numérico y mayor que cero.")


def opcion_conversion():
    while True:
        try:
            opcion = int(input("1: USD\n2: EUR\n3: CO\n4: USDT\n> "))
            if opcion >= 1 or opcion <= 4:
                return [opcion, tasa_cambio[opcion]["moneda"]]
            print("Opción inválida. Por favor, ingrese las opciones disponibles.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese las opciones disponibles.")


def convertir(opcion, monto):
    return monto / tasa_cambio[opcion]["precio"]


monto = solicitar_monto()
opcion, moneda = opcion_conversion()
conversion = convertir(opcion, monto)

print(f"El monto en {moneda} es {conversion:.2f}")
