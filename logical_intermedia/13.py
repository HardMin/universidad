"""
13. Registro de Notas con Diccionarios

Almacene nombres de alumnos y una lista de sus notas. El programa debe calcular
el promedio individual de cada alumno.
"""

alumnos = [
    {"nombre": "Juan Pérez", "notas": [15, 12, 18, 14, 10]},
    {"nombre": "María García", "notas": [19, 17, 20, 18, 16]},
    {"nombre": "Carlos Rodríguez", "notas": [8, 11, 13, 9, 12]},
    {"nombre": "Ana Martínez", "notas": [14, 15, 16, 14, 15]},
    {"nombre": "Luis Hernández", "notas": [10, 12, 11, 13, 10]},
    {"nombre": "Elena López", "notas": [17, 18, 19, 16, 18]},
    {"nombre": "Javier González", "notas": [7, 9, 8, 10, 11]},
    {"nombre": "Lucía Díaz", "notas": [20, 19, 18, 20, 19]},
    {"nombre": "Ricardo Sánchez", "notas": [12, 13, 14, 12, 11]},
    {"nombre": "Sofía Romero", "notas": [15, 16, 15, 17, 14]},
    {"nombre": "Andrés Álvarez", "notas": [9, 10, 11, 8, 12]},
    {"nombre": "Beatriz Torres", "notas": [18, 17, 16, 18, 19]},
    {"nombre": "Marcos Ruiz", "notas": [11, 10, 12, 11, 13]},
    {"nombre": "Gabriela Morales", "notas": [16, 15, 17, 16, 15]},
    {"nombre": "Roberto Castro", "notas": [13, 14, 12, 13, 14]},
    {"nombre": "Clara Ortiz", "notas": [19, 20, 19, 18, 20]},
    {"nombre": "Fernando Silva", "notas": [6, 8, 7, 9, 10]},
    {"nombre": "Julia Méndez", "notas": [14, 15, 13, 14, 16]},
    {"nombre": "David Guzmán", "notas": [11, 12, 11, 10, 12]},
    {"nombre": "Patricia Blanco", "notas": [17, 16, 18, 17, 16]},
    {"nombre": "Jorge Castillo", "notas": [12, 11, 13, 12, 10]},
    {"nombre": "Isabel Vargas", "notas": [20, 19, 20, 19, 20]},
    {"nombre": "Miguel Salazar", "notas": [8, 7, 9, 10, 8]},
    {"nombre": "Raquel Medina", "notas": [15, 16, 14, 15, 17]},
    {"nombre": "Oscar Paredes", "notas": [11, 13, 12, 11, 14]},
    {"nombre": "Valeria Acosta", "notas": [18, 19, 17, 18, 19]},
    {"nombre": "Héctor Rojas", "notas": [9, 10, 8, 11, 9]},
    {"nombre": "Natalia Soria", "notas": [16, 17, 16, 15, 16]},
    {"nombre": "Simón Benítez", "notas": [12, 14, 13, 12, 15]},
    {"nombre": "Daniela Peña", "notas": [19, 18, 17, 19, 20]},
]


def calcular_promedio(alumno):
    notas = alumno["notas"]
    promedio = sum(notas) / len(notas)
    return promedio


def mostrar_notas(notas):
    for nota in notas:
        num = f" {nota} " if nota > 9 else f" 0{nota} "
        print(num, end="|")


print("NOTAS DE ALUMNOS".center(56))
print(
    "Nombre Apellido".center(17),
    "|",
    "Notas".center(22),
    "|",
    "Promedio".center(10),
    "|",
)
print(f"{'-' * 18}|{'-' * 24}|{'-' * 12}|")
for alumno in alumnos:
    espacio_nombre = f"{'':>{18 - len(alumno["nombre"])}}"
    print(alumno["nombre"], end=f"{espacio_nombre}|")

    mostrar_notas(alumno["notas"])
    promedio = calcular_promedio(alumno)
    print(str(promedio).center(12), end="|\n")
