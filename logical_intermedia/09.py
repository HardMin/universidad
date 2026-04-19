"""
9. Verificador de Palíndromos

Solicite una frase y determine si se lee igual de izquierda a derecha
(ignorando espacios y mayúsculas).
"""

frase = input("Ingrese una frase: ")
palindromo = frase.lower().replace(" ", "")

if palindromo == palindromo[::-1]:
    print("La frase es un palindromo.")
else:
    print("La frase no es un palindromo.")

print(f"\n{'PALINDROMO':<15} | {'REVERSO':<10}")
print("-" * 30)
print(f"{palindromo:<15} | {palindromo[::-1]:<10}")
