# Soluciones de la práctica — 2. Condicionales
# Uso:  python condicionales.py [numero]

import random

from comun import elegir_y_ejecutar


def ejercicio_1():
    """Positivo, negativo o cero"""
    numero = float(input("Número: "))

    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Es cero")


def ejercicio_2():
    """Par o impar"""
    numero = int(input("Número: "))

    # Con if normal
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

    # En una línea, con el operador ternario
    print("Ternario:", "par" if numero % 2 == 0 else "impar")


def ejercicio_3():
    """Nota cualitativa con validación"""
    nota = float(input("Nota (0 a 20): "))

    # Se pregunta primero por lo inválido y luego de la condición más
    # exigente a la menos exigente.
    if nota < 0 or nota > 20:
        print("Nota inválida")
    elif nota >= 19:
        print("Excelente")
    elif nota >= 16:
        print("Muy bueno")
    elif nota >= 10:
        print("Aprobado")
    else:
        print("Reprobado")


def ejercicio_4():
    """Calculadora con menú (match)"""
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("Opción: ")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    # input() devuelve texto, así que los casos se comparan con textos.
    match opcion:
        case "1":
            print("Resultado:", a + b)
        case "2":
            print("Resultado:", a - b)
        case "3":
            print("Resultado:", a * b)
        case "4":
            if b == 0:
                print("Error: no se puede dividir entre cero")
            else:
                print("Resultado:", a / b)
        case _:
            print("Opción no válida")


def ejercicio_5():
    """Año bisiesto"""
    anio = int(input("Año: "))

    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(anio, "es bisiesto")
    else:
        print(anio, "no es bisiesto")


def ejercicio_6():
    """Piedra, papel o tijera contra la computadora"""
    opciones = ["piedra", "papel", "tijera"]
    # Cada jugada le gana a la que tiene asociada.
    le_gana_a = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

    jugador = input("Tu jugada (piedra, papel o tijera): ").strip().lower()
    if jugador not in opciones:
        print("Jugada no válida")
        return

    computadora = random.choice(opciones)
    print("La computadora eligió:", computadora)

    if jugador == computadora:
        print("Empate")
    elif le_gana_a[jugador] == computadora:
        print("¡Ganaste!")
    else:
        print("Gana la computadora")


if __name__ == "__main__":
    elegir_y_ejecutar("Condicionales", {
        1: ejercicio_1, 2: ejercicio_2, 3: ejercicio_3,
        4: ejercicio_4, 5: ejercicio_5, 6: ejercicio_6,
    })
