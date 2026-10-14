# Soluciones de la práctica — 3. Ciclos
# Uso:  python ciclos.py [numero]

import random

from comun import elegir_y_ejecutar


def ejercicio_1():
    """Tabla de multiplicar"""
    numero = int(input("Número: "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def ejercicio_2():
    """Suma de 1 a n"""
    n = int(input("n: "))

    suma = 0                        # el acumulador empieza en 0 ANTES del ciclo
    for i in range(1, n + 1):
        suma += i

    print("Con acumulador:", suma)
    print("Con sum(range()):", sum(range(1, n + 1)))


def ejercicio_3():
    """Promedio de la clase y aprobados"""
    cantidad = int(input("¿Cuántos estudiantes hay? "))
    if cantidad <= 0:
        print("No hay estudiantes.")
        return

    suma = 0
    aprobados = 0
    for i in range(1, cantidad + 1):
        nota = float(input(f"Nota del estudiante {i}: "))
        suma += nota
        if nota >= 10:
            aprobados += 1

    print("Promedio:", suma / cantidad)
    print("Aprobaron:", aprobados)


def ejercicio_4():
    """Validar una edad entre 1 y 120"""
    while True:
        respuesta = input("Edad (1 a 120): ")
        try:
            edad = int(respuesta)
        except ValueError:
            print("Eso no es un número entero.")
            continue                # vuelve a preguntar

        if 1 <= edad <= 120:
            break                   # dato correcto: sale del ciclo
        print("La edad debe estar entre 1 y 120.")

    print("Edad guardada:", edad)


def ejercicio_5():
    """Número primo"""
    numero = int(input("Número: "))

    es_primo = numero >= 2
    divisor = 2
    # Basta probar divisores hasta la raíz cuadrada del número.
    while divisor * divisor <= numero and es_primo:
        if numero % divisor == 0:
            es_primo = False
        divisor += 1

    print(numero, "es primo" if es_primo else "no es primo")


def ejercicio_6():
    """Adivina el número (5 intentos)"""
    secreto = random.randint(1, 20)
    print("Estoy pensando en un número del 1 al 20. Tienes 5 intentos.")

    for intento in range(1, 6):
        numero = int(input(f"Intento {intento}: "))

        if numero == secreto:
            print(f"¡Correcto! Lo lograste en {intento} intentos.")
            break
        print("Muy bajo" if numero < secreto else "Muy alto")
    else:
        # El else de un for se ejecuta solo si el ciclo terminó SIN break.
        print(f"Se acabaron los intentos. El número era {secreto}.")


if __name__ == "__main__":
    elegir_y_ejecutar("Ciclos", {
        1: ejercicio_1, 2: ejercicio_2, 3: ejercicio_3,
        4: ejercicio_4, 5: ejercicio_5, 6: ejercicio_6,
    })
