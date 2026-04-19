"""
3. Filtro de Ventas Altas

Dada una lista de diccionarios con ventas

Ejemplo:
[
  {
    "vendedor": "Ana",
    "monto": 500
  },
  {
    "vendedor": "Pepe",
    "monto": 1000
  },
]

retorne una nueva lista solo con los vendedores que superaron los $1000.
"""

ventas = [
    {"vendedor": "Ana", "monto": 500},
    {"vendedor": "Pepe", "monto": 1000},
    {"vendedor": "Carlos", "monto": 1250},
    {"vendedor": "María", "monto": 1800},
    {"vendedor": "Luis", "monto": 650},
    {"vendedor": "Elena", "monto": 2000},
    {"vendedor": "Javier", "monto": 950},
    {"vendedor": "Lucía", "monto": 1100},
    {"vendedor": "Ricardo", "monto": 550},
    {"vendedor": "Sofía", "monto": 1400},
    {"vendedor": "Andrés", "monto": 800},
    {"vendedor": "Beatriz", "monto": 1600},
    {"vendedor": "Marcos", "monto": 720},
    {"vendedor": "Gabriela", "monto": 1950},
    {"vendedor": "Roberto", "monto": 1050},
    {"vendedor": "Clara", "monto": 500},
    {"vendedor": "Fernando", "monto": 1350},
    {"vendedor": "Julia", "monto": 1500},
    {"vendedor": "David", "monto": 900},
    {"vendedor": "Patricia", "monto": 1700},
]

ventas_filtradas = [venta for venta in ventas if venta["monto"] > 1000]

print(f"{'VENDEDOR':<15} | {'MONTO':<10}")
print("-" * 30)
for venta in ventas_filtradas:
    print(f"{venta['vendedor']:<15} | {venta['monto']:<10}")
