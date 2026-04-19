"""
14. Cronómetro de Tareas

Use la librería time para medir cuántos segundos tarda el usuario en resolver
una operación matemática simple que el programa le asigne.
"""

import time

calculos = ["4 + 5", "2 * 3", "10 / 2"]

tiempo = time.time()


def entrada(msj):
    try:
        calculo = float(input(msj))
        return calculo
    except ValueError:
        print("\nIngrese un número".center(10, " - "), end="\n\n")
        return entrada(msj)


for calculo in calculos:
    resultado = eval(calculo)
    respuesta = entrada(f"Cuanto es {calculo} = ")
    if respuesta == resultado:
        print(f"\nCorrecto! {calculo} = {resultado}")
    else:
        print(f"\nError! {calculo} = {resultado}")

    print(f"\nTiempo: {(time.time() - tiempo):.2f} segundos")
    print("\n")

    tiempo = time.time()
