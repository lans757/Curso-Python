# Soluciones de la práctica — 1. Fundamentos
# Uso:  python fundamentos.py        (pregunta cuál ejecutar)
#       python fundamentos.py 3      (ejecuta el ejercicio 3)

from comun import elegir_y_ejecutar

IVA = 0.16


def ejercicio_1():
    """Tarjeta de presentación"""
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    ciudad = input("Ciudad: ")

    print("-" * 30)
    print(f" Nombre:   {nombre}")
    print(f" Apellido: {apellido}")
    print(f" Ciudad:   {ciudad}")
    print("-" * 30)


def ejercicio_2():
    """Área y perímetro del rectángulo"""
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    print("Área:", base * altura)
    print("Perímetro:", 2 * base + 2 * altura)


def ejercicio_3():
    """Compra con IVA"""
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))

    subtotal = precio * cantidad
    iva = subtotal * IVA
    total = subtotal + iva

    print(f"Subtotal: {subtotal:.2f}")
    print(f"IVA ({IVA:.0%}): {iva:.2f}")
    print(f"Total: {total:.2f}")


def ejercicio_4():
    """Minutos a horas y minutos"""
    minutos = int(input("Minutos: "))

    horas = minutos // 60          # cuántas horas completas caben
    resto = minutos % 60           # los minutos que sobran

    print(f"{horas} horas y {resto} minutos")


def ejercicio_5():
    """Segundos a días, horas, minutos y segundos"""
    total = int(input("Segundos: "))

    dias = total // 86400          # 24 * 60 * 60
    total = total % 86400
    horas = total // 3600
    total = total % 3600
    minutos = total // 60
    segundos = total % 60

    print(f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos")


def ejercicio_6():
    """Invertir un número de tres cifras"""
    numero = int(input("Número de tres cifras: "))

    centenas = numero // 100
    decenas = numero // 10 % 10
    unidades = numero % 10

    invertido = unidades * 100 + decenas * 10 + centenas
    print("Invertido:", invertido)
    # Con texto sería int(str(numero)[::-1]), pero el ejercicio pedía aritmética.


if __name__ == "__main__":
    elegir_y_ejecutar("Fundamentos", {
        1: ejercicio_1, 2: ejercicio_2, 3: ejercicio_3,
        4: ejercicio_4, 5: ejercicio_5, 6: ejercicio_6,
    })
