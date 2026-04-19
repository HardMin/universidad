# Guía de Actividades

Lógica Intermedia en Python

## Instrucciones

Desarrolle scripts óptimos y seguros, aplicando funciones para modularizar el
código y manejando excepciones donde sea necesario. RECUERDEN Leer el libro
electrónico que les compartí.

## 1. Validador de Lote de Productos

Solicite una lista de códigos de productos. El programa debe filtrar y mostrar
solo aquellos que comiencen con la letra "A" y tengan exactamente 5 dígitos.

## 2. Cálculo de Nómina con Horas Extra

Cree una función que reciba horas trabajadas y pago por hora. Si las horas
exceden las 40, las excedentes se pagan al doble. Calcule el salario neto.

## 3. Filtro de Ventas Altas

Dada una lista de diccionarios con ventas

Ejemplo:

```python
[
  {
    "vendedor": "Ana",
    "monto": 500
  },
  {
    "vendedor": "Pepe",
    "monto": 1000
  },
  ...
]
```

retorne una nueva lista solo con los vendedores que superaron los $1000.

## 4. Buscador en Inventario

Implemente un programa que permita buscar un artículo en una lista. Si no
existe, debe capturar el error y ofrecer al usuario la opción de agregarlo.

## 5. Analizador de Texto Corporativo

Solicite un párrafo. El script debe contar cuántas palabras tiene y extraer la
palabra más larga utilizada.

## 6. Conversor de Monedas con Diccionarios

Utilice un diccionario para almacenar tasas de cambio (USD, EUR, GBP). El
usuario ingresa el monto en moneda local y el programa devuelve la conversión solicitada.

## 7. Sistema de Turnos (Colas)

Simule un sistema de atención al cliente usando una lista. Permita añadir
clientes al final y "atender" al primero de la lista (método pop(0)).

## 8. Generador de Facturas con IVA Variable

Cree una función que reciba el precio base y un porcentaje de IVA opcional
(por defecto 16%). Debe retornar el desglose total.

## 9. Verificador de Palíndromos

Solicite una frase y determine si se lee igual de izquierda a derecha
(ignorando espacios y mayúsculas).

## 10. Calculadora de Edad Media

Pida una serie de edades hasta que el usuario ingrese "0". Calcule el promedio
de edad de las personas ingresadas.

## 11. Formateador de Nombres Propios

Reciba una lista de nombres en desorden (ej. "JUAN", "maRía") y devuelva la
lista correctamente formateada (Capitalize) y ordenada alfabéticamente.

## 12. Simulador de Cajero Automático

Cree un programa con un saldo inicial. Permita retirar dinero solo si hay
fondos suficientes y maneje el error si se ingresa un monto no numérico.

## 13. Registro de Notas con Diccionarios

Almacene nombres de alumnos y una lista de sus notas. El programa debe calcular
el promedio individual de cada alumno.

## 14. Cronómetro de Tareas

Use la librería time para medir cuántos segundos tarda el usuario en resolver
una operación matemática simple que el programa le asigne.

## 15. Limpieza de Datos de Usuario

Reciba un correo electrónico y verifique si contiene un "@" y un punto ".". Si
no cumple, solicite el ingreso nuevamente usando un bucle while.
