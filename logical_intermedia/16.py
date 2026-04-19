"""
16. Permitir entrada de usuarios y generar pdf

Solicitar la edad y si es mayor a 18 años, permitir el acceso, si no, no
permitir el acceso. Solicitar hasta que se ingrese 0 y generara un pdf
con los usuarios permitidos y los no permitidos, y el total de usuarios
permitidos y no permitidos.
"""

import os


usuarios = [15, 16, 14, 22, 30, 15, 18, 20, 22, 23, 26, 19, 21, 25, 24, 27, 28, 29, 30]

usuarios_permitidos = []
usuarios_no_permitidos = []

for usuario in usuarios:
    if usuario >= 18:
        usuarios_permitidos.append(usuario)
    else:
        usuarios_no_permitidos.append(usuario)

columna_usuarios_permitidos = ""

for usuario in usuarios_permitidos:
    columna_usuarios_permitidos += f"<tr><td>{usuario}</td></tr>"

columna_usuarios_no_permitidos = ""

for usuario in usuarios_no_permitidos:
    columna_usuarios_no_permitidos += f"<tr><td>{usuario}</td></tr>\n"

estructura = f"""
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Usuarios</title>
    <link href="css/style.css" rel="stylesheet" />
  </head>
    <body>
        <h1 style="text-align: center;">Usuarios</h1>
        <div style="display:flex; width: 100vw; justify-content: center;">
            <div>
                <table>
                    <thead>
                        <tr>
                            <td>Usuarios Permitidos</td>
                        </tr>
                    </thead>
                    <tbody>
                        {columna_usuarios_permitidos}
                    </tbody>
                </table>
                <h3>Total de Usuarios Permitidos: {len(usuarios_permitidos)}</h3>
            </div>
            <div>
                <table>
                    <thead>
                        <tr>
                            <td>Usuarios No Permitidos</td>
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
