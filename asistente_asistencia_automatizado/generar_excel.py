import random
import pandas as pd

# Listas de nombres y apellidos para generar datos realistas
nombres = [
    "Ana",
    "Luis",
    "Carlos",
    "María",
    "José",
    "Daniela",
    "Javier",
    "Laura",
    "Pedro",
    "Sofía",
    "Andrés",
    "Valentina",
    "Ricardo",
    "Camila",
    "Diego",
    "Isabella",
    "Fernando",
    "Gabriela",
    "Miguel",
    "Elena",
    "Jorge",
    "Paula",
    "Ramón",
    "Adriana",
    "Sergio",
    "Natalia",
    "Oscar",
    "Verónica",
    "Héctor",
    "Mónica",
]
apellidos = [
    "García",
    "Pérez",
    "López",
    "Rodríguez",
    "González",
    "Martínez",
    "Sánchez",
    "Ramírez",
    "Torres",
    "Flores",
    "Díaz",
    "Herrera",
    "Vargas",
    "Rojas",
    "Castro",
    "Ortega",
    "Mendoza",
    "Silva",
    "Romero",
    "Fernández",
    "Gómez",
    "Álvarez",
    "Ruiz",
    "Núñez",
    "Jiménez",
    "Chávez",
    "Gutiérrez",
    "Paredes",
    "Molina",
    "Acosta",
]

# Materias y secciones posibles
materias = ["Matemática", "Física", "Programación", "Bases de Datos", "Estadística"]
secciones = ["A", "B", "C", "D", "E"]

# Generar datos para 30 alumnos
data = {
    "Cédula": [],
    "Nombre": [],
    "Apellido": [],
    "Correo": [],
    "Materia": [],
    "Sección": [],
    "Asistencia_Dia1": [],
    "Asistencia_Dia2": [],
    "Asistencia_Dia3": [],
    "Asistencia_Dia4": [],
}

for i in range(30):
    nombre = nombres[i]
    apellido = apellidos[i]
    # Cédula: 8 dígitos aleatorios (Venezuela)
    cedula = random.randint(10000000, 30000000)
    # Correo: nombre.apellido@dominio.com, sin espacios, todo minúsculas
    correo = f"{nombre.lower()}.{apellido.lower()}@unal.edu.co"  # Dominio ficticio
    # Opcional: algunos correos inválidos (para probar validación). Pero aquí se generan válidos.
    materia = random.choice(materias)
    seccion = random.choice(secciones)
    # Asistencias: S (asistió) con 70% de probabilidad, N (no asistió) 30%
    dias = []
    for _ in range(4):
        dias.append("S" if random.random() < 0.7 else "N")

    data["Cédula"].append(cedula)
    data["Nombre"].append(nombre)
    data["Apellido"].append(apellido)
    data["Correo"].append(correo)
    data["Materia"].append(materia)
    data["Sección"].append(seccion)
    data["Asistencia_Dia1"].append(dias[0])
    data["Asistencia_Dia2"].append(dias[1])
    data["Asistencia_Dia3"].append(dias[2])
    data["Asistencia_Dia4"].append(dias[3])

df = pd.DataFrame(data)

# Guardar como archivo Excel
df.to_excel("asistencia_unesr.xlsx", index=False, sheet_name="Asistencia")

print("Archivo 'asistencia_unesr.xlsx' generado con 30 alumnos y 4 días de asistencia.")
