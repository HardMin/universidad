"""
11. Formateador de Nombres Propios

Reciba una lista de nombres en desorden (ej. "JUAN", "maRía") y devuelva la
lista correctamente formateada (Capitalize) y ordenada alfabéticamente.
"""

nombres = [
    "JUAN",
    "maRía",
    "pedro",
    "ALBERTO",
    "ana lúcia",
    "rIcArDo",
    "BEATRIZ",
    "sergio",
    "vALENTINA",
    "mArCoS",
    "elena",
    "GABRIEL",
    "claudia",
    "jorge",
    "SOfíA",
    "luis",
    "mArTa",
    "andrés",
    "lucía",
    "fErNaNdO",
]

nombres_formateados = [nombre.capitalize() for nombre in nombres]
nombres_formateados.sort()

print(f"Nombres: {nombres}")
print(f"\n\nNombres formateados: {nombres_formateados}")
