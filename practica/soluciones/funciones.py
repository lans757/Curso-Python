# Soluciones de la práctica — 5. Funciones
# Uso:  python funciones.py [numero]
#
# Aquí cada ejercicio tiene dos partes: la función que se pedía (arriba) y
# una pequeña prueba que la usa (ejercicio_N).

from comun import elegir_y_ejecutar


# --- Las funciones pedidas -------------------------------------------------

def es_par(numero):
    """Devuelve True si el número es par."""
    return numero % 2 == 0


def mayor_de_tres(a, b, c):
    """Devuelve el mayor de tres números, sin usar max()."""
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


def calificacion(nota):
    """Devuelve la calificación cualitativa de una nota de 0 a 20."""
    if nota >= 19:
        return "Excelente"
    if nota >= 16:
        return "Muy bueno"
    if nota >= 10:
        return "Aprobado"
    return "Reprobado"


def contar_vocales(frase):
    """Cuenta las vocales de una frase, sin importar mayúsculas."""
    total = 0
    for letra in frase.lower():
        if letra in "aeiouáéíóú":
            total += 1
    return total


def es_primo(n):
    """Devuelve True si n es primo."""
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def factorial(n):
    """Devuelve n! (el producto de 1 hasta n)."""
    resultado = 1
    for i in range(2, n + 1):       # si n es 0 o 1, el ciclo no se ejecuta
        resultado *= i
    return resultado


def mcd(a, b):
    """Máximo común divisor con el algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a


def es_palindromo(frase):
    """Devuelve True si la frase se lee igual al derecho y al revés."""
    limpia = frase.lower().replace(" ", "")
    return limpia == limpia[::-1]


# --- Las pruebas -----------------------------------------------------------

def ejercicio_1():
    """es_par(numero)"""
    for numero in [8, 7, 0]:
        if es_par(numero):
            print(numero, "es par")
        else:
            print(numero, "es impar")


def ejercicio_2():
    """mayor_de_tres(a, b, c)"""
    print("Mayor de 4, 9 y 2:", mayor_de_tres(4, 9, 2))
    print("Mayor de 7, 7 y 3:", mayor_de_tres(7, 7, 3))
    print("Mayor de -5, -1 y -9:", mayor_de_tres(-5, -1, -9))


def ejercicio_3():
    """calificacion(nota)"""
    for nota in [20, 17, 10, 9]:
        print(f"{nota:>2} -> {calificacion(nota)}")


def ejercicio_4():
    """contar_vocales(frase)"""
    for frase in ["Hola Mundo", "PROGRAMACION", "xyz"]:
        print(f"'{frase}' tiene {contar_vocales(frase)} vocales")


def ejercicio_5():
    """es_primo, factorial y mcd"""
    print("Primos del 1 al 30:", [n for n in range(1, 31) if es_primo(n)])
    print("0! =", factorial(0), "  1! =", factorial(1), "  5! =", factorial(5))
    print("mcd(12, 18) =", mcd(12, 18))
    print("mcd(17, 5) =", mcd(17, 5))


def ejercicio_6():
    """es_palindromo(frase)"""
    for frase in ["Anita lava la tina", "reconocer", "Python"]:
        print(f"'{frase}':", es_palindromo(frase))


if __name__ == "__main__":
    elegir_y_ejecutar("Funciones", {
        1: ejercicio_1, 2: ejercicio_2, 3: ejercicio_3,
        4: ejercicio_4, 5: ejercicio_5, 6: ejercicio_6,
    })
