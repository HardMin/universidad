"""
8. Generador de Facturas con IVA Variable

Cree una función que reciba el precio base y un porcentaje de IVA opcional
(por defecto 16%). Debe retornar el desglose total.
"""


def entrada(msj):
    while True:
        try:
            valor = float(input(msj))
            if valor > 0:
                return valor
        except ValueError:
            pass

        print("Debe ser numérico y mayor que cero.")


def precio_base():
    return entrada("Ingrese el precio base: ")


def iva_variable():
    return entrada("Ingrese el porcentaje de IVA: ") / 100


def calcular_total(monto, iva):
    return monto * (1 + iva)


def Mensaje(monto, iva):
    mensaje = f"""
                    FACTURA
    {"-" * 38}


      TOTAL:                     {monto}Bs
      IVA:                       {iva * 100}%
    {"-" * 38}
      TOTAL:                     {calcular_total(monto, iva)}Bs
    """
    return mensaje


monto_base = precio_base()
iva = iva_variable()

print(Mensaje(monto_base, iva))
