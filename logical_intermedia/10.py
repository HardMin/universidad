"""
10. Calculadora de Edad Media

Pida una serie de edades hasta que el usuario ingrese "0". Calcule el promedio
de edad de las personas ingresadas.
"""

edades = []


def entrada():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad >= 0:
                return edad
        except ValueError:
            pass
        print("Debe ser numérico y mayor que cero.")


while True:
    edad = entrada()
    if edad == 0:
        break
    edades.append(edad)

print(f"Promedio de edad: {sum(edades) / len(edades)}")
