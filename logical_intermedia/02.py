"""
2. Cálculo de Nómina con Horas Extra

Cree una función que reciba horas trabajadas y pago por hora. Si las horas
exceden las 40, las excedentes se pagan al doble. Calcule el salario neto.
"""


def entrada():
    while True:
        try:
            horas = int(input("Ingrese las horas trabajadas: "))
            if horas > 0:
                return horas
            else:
                print("Ingrese un número positivo")
        except ValueError:
            print("Ingrese un número válido")


horas_trabajadas = entrada()

salario = 0
pago_hora = 10

if horas_trabajadas > 40:
    excedente = horas_trabajadas - 40
    salario = 40 * pago_hora + excedente * pago_hora * 2
else:
    salario = horas_trabajadas * pago_hora

print(f"El salario neto es {salario}")
