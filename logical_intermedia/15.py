"""
15. Limpieza de Datos de Usuario

Reciba un correo electrónico y verifique si contiene un "@" y un punto ".". Si
no cumple, solicite el ingreso nuevamente usando un bucle while.
"""


def entrada():
    while True:
        try:
            correo = input("\nIngrese un correo: ")
            if "@" in correo and "." in correo:
                return correo
            else:
                print("Correo invalido!")
        except ValueError:
            print("Ingrese un correo válido")


print("Limpieza de Datos de Usuario".center(40))
print("Ingrese un correo válido".center(40))

correo = entrada()
print(f"\nCorreo: {correo}")
