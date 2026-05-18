"""
16. Permitir entrada de usuarios y generar pdf

Solicitar la edad y si es mayor a 18 años, permitir el acceso, si no, no
permitir el acceso. Solicitar hasta que se ingrese 0 y generara un pdf
con los usuarios permitidos y los no permitidos, y el total de usuarios
permitidos y no permitidos.
"""

import os

usuarios = [
    {"nombre": "Andrés García", "edad": 19},
    {"nombre": "Camila Martínez", "edad": 24},
    {"nombre": "Diego López", "edad": 52},
    {"nombre": "Elena Hernández", "edad": 41},
    {"nombre": "Fernando González", "edad": 16},
    {"nombre": "Gabriela Pérez", "edad": 58},
    {"nombre": "Hugo Rodríguez", "edad": 19},
    {"nombre": "Isabel Sánchez", "edad": 15},
    {"nombre": "Javier Ramírez", "edad": 22},
    {"nombre": "Karla Cruz", "edad": 48},
    {"nombre": "Luis Gómez", "edad": 27},
    {"nombre": "Mónica Flores", "edad": 15},
    {"nombre": "Nicolás Morales", "edad": 18},
    {"nombre": "Olivia Vázquez", "edad": 43},
    {"nombre": "Pablo Reyes", "edad": 30},
    {"nombre": "Raquel García", "edad": 60},
    {"nombre": "Santiago Martínez", "edad": 21},
    {"nombre": "Tatiana López", "edad": 17},
    {"nombre": "Víctor Hernández", "edad": 15},
    {"nombre": "Valeria González", "edad": 50},
    {"nombre": "Ricardo Pérez", "edad": 16},
    {"nombre": "Sofía Rodríguez", "edad": 42},
    {"nombre": "Marcos Sánchez", "edad": 23},
    {"nombre": "Beatriz Ramírez", "edad": 56},
    {"nombre": "Jorge Cruz", "edad": 17},
    {"nombre": "Patricia Gómez", "edad": 59},
    {"nombre": "Roberto Flores", "edad": 20},
    {"nombre": "Clara Morales", "edad": 44},
    {"nombre": "Felipe Vázquez", "edad": 15},
    {"nombre": "Lucía Reyes", "edad": 53},
]

usuarios_permitidos = []
usuarios_no_permitidos = []

for usuario in usuarios:
    if usuario["edad"] >= 18:
        usuarios_permitidos.append(usuario)
    else:
        usuarios_no_permitidos.append(usuario)

columna_usuarios_permitidos = ""

for usuario in usuarios_permitidos:
    columna_usuarios_permitidos += (
        f"<tr><td>{usuario['nombre']}</td><td>{usuario['edad']}</td></tr>"
    )

columna_usuarios_no_permitidos = ""

for usuario in usuarios_no_permitidos:
    columna_usuarios_no_permitidos += (
        f"<tr><td>{usuario['nombre']}</td><td>{usuario['edad']}</td></tr>"
    )

estructura = f"""
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Usuarios</title>
    <link href="css/style.css" rel="stylesheet" />
  </head>
    <body style="font-family: sans-serif;">
        <h1 style="text-align: center;">Usuarios</h1>
        <div style="display:flex; width: 100vw; justify-content: center;">
            <div>
                <table border="1">
                    <caption>Usuarios Permitidos</caption>
                    <thead>
                        <tr>
                            <td>Nombre</td>
                            <td>Edad</td>
                        </tr>
                    </thead>
                    <tbody>
                        {columna_usuarios_permitidos}
                    </tbody>
                </table>
                <h3>Total de Usuarios Permitidos: {len(usuarios_permitidos)}</h3>
            </div>
            <div>
                <table border="1">
                    <caption>Usuarios No Permitidos</caption>
                    <thead>
                        <tr>
                            <td>Nombre</td>
                            <td>Edad</td>
                        </tr>
                    </thead>
                    <tbody>
                        {columna_usuarios_no_permitidos}
                    </tbody>
                </table>
                <h3>Total de Usuarios no Permitidos: {len(usuarios_no_permitidos)}</h3>
            </div>
        </div>
    </body>
</html>
"""

with open("usuarios.html", "w") as archivo:
    archivo.write(estructura)
    archivo.close()

os.system('brave --headless --print-to-pdf="usuarios.pdf" usuarios.html')
