# TEST
LINK GITHUB: https://github.com/lmiel/TEST.git

Imagina que necesitamos implementar una función que calcule el factorial de un número. Si aplicamos la metodología de Desarrollo Basado en Pruebas (TDD), el primer paso es crear una función vacía, únicamente para poder llamarla. Luego, escribiremos una prueba que verifique su funcionamiento y la ejecutaremos para comprobar que efectivamente falla, como se espera.

# Paso 1: Creación de Archivos y Estructura Inicial
Primero, vamos a crear un archivo llamado myfactorial.py, en el que definiremos la función factorial. Esta función inicialmente no hará nada, simplemente devolverá un valor predeterminado (como 0) para que podamos probarla. Luego, crearemos un archivo llamado test_.py, en el que escribiremos una prueba unitaria para verificar el cálculo del factorial.

Código en myfactorial.py:


def factorial(numero):
    return 0
Código en test_.py:


import pytest
import myfactorial

def test_myfactorial():
    assert myfactorial.factorial(3) == 6
# Paso 2: Ejecutar la Prueba Inicial
Una vez que tengamos estos archivos, abrimos una terminal en el directorio donde están ubicados y ejecutamos el siguiente comando para correr las pruebas:


pytest test_.py
Este comando ejecutará la prueba y, dado que la función factorial aún no está correctamente implementada, la prueba fallará, lo cual es el comportamiento esperado en TDD.

# Paso 3: Implementar la Función Factorial
Ahora, procedemos a implementar la lógica necesaria para calcular el factorial en la función factorial.

Código actualizado en myfactorial.py:


def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact *= i
    return fact

# Paso 4: Volver a Ejecutar las Pruebas
Después de haber implementado la función, volvemos a ejecutar el comando pytest test_.py. Si todo está correcto, la prueba debería pasar sin problemas, lo que indicará que nuestra función ahora calcula correctamente el factorial.

Paso 5: Ampliar las Pruebas
Ahora es tu turno. Debes implementar pruebas adicionales que verifiquen el comportamiento de la función factorial en casos especiales. Por ejemplo, debes escribir pruebas que comprueben:

Qué sucede cuando intentas calcular el factorial de 0.
Qué sucede cuando intentas calcular el factorial de un número negativo.
Después de escribir estas pruebas, ejecútalas y observa los resultados. Si alguna prueba falla, refactoriza la función factorial hasta que pase todas las pruebas.
