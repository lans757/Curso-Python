# Soluciones de la práctica — 4. Arreglos
# Uso:  python arreglos.py [numero]

from comun import elegir_y_ejecutar


def pedir_cinco_numeros():
    numeros = []
    for i in range(1, 6):
        numeros.append(float(input(f"Número {i}: ")))
    return numeros


def ejercicio_1():
    """Cinco números al revés"""
    numeros = pedir_cinco_numeros()

    print("En el orden original:", numeros)
    print("Al revés:", numeros[::-1])

    # La versión "a mano", recorriendo por índice desde el último:
    for i in range(len(numeros) - 1, -1, -1):
        print(numeros[i], end=" ")
    print()


def ejercicio_2():
    """Suma, promedio, mayor y menor"""
    numeros = pedir_cinco_numeros()

    print("Suma:", sum(numeros))
    print("Promedio:", sum(numeros) / len(numeros))
    print("Mayor:", max(numeros))
    print("Menor:", min(numeros))


def ejercicio_3():
    """Notas por encima del promedio"""
    notas = [12, 18, 9, 15, 20, 7, 14, 11]

    promedio = sum(notas) / len(notas)
    superiores = [nota for nota in notas if nota > promedio]

    print("Notas:", notas)
    print("Promedio:", promedio)
    print("Por encima del promedio:", superiores)


def ejercicio_4():
    """Buscar un nombre y contar cuántas veces aparece"""
    nombres = ["Ana", "Luis", "Marta", "ana", "Jose", "Carla", "ANA"]
    buscado = input("Nombre a buscar: ").strip().lower()

    # Se compara todo en minúsculas para que no importe cómo se escribió.
    en_minusculas = [nombre.lower() for nombre in nombres]

    if buscado in en_minusculas:
        print("Primera posición:", en_minusculas.index(buscado))
        print("Aparece", en_minusculas.count(buscado), "veces")
    else:
        print("Ese nombre no está en la lista")


def ejercicio_5():
    """Ranking de estudiantes"""
    estudiantes = [
        {"nombre": "Ana", "nota": 18},
        {"nombre": "Luis", "nota": 14},
        {"nombre": "Marta", "nota": 20},
        {"nombre": "Jose", "nota": 9},
        {"nombre": "Carla", "nota": 16},
    ]

    ranking = sorted(estudiantes, key=lambda e: e["nota"], reverse=True)

    print("RANKING")
    for puesto, estudiante in enumerate(ranking, start=1):
        print(f"{puesto}. {estudiante['nombre']:<8} {estudiante['nota']}")


def ejercicio_6():
    """Tabla de notas: promedios por estudiante y por materia"""
    estudiantes = ["Ana", "Luis", "Marta", "Jose"]
    materias = ["Matemática", "Castellano", "Ciencias"]
    notas = [
        [18, 15, 20],
        [12, 9, 14],
        [20, 19, 17],
        [8, 11, 10],
    ]

    print("Promedio de cada estudiante:")
    for nombre, fila in zip(estudiantes, notas):
        print(f"  {nombre:<8} {sum(fila) / len(fila):.2f}")

    print("Promedio de cada materia:")
    for columna, materia in enumerate(materias):
        notas_de_la_materia = [fila[columna] for fila in notas]
        print(f"  {materia:<12} {sum(notas_de_la_materia) / len(notas_de_la_materia):.2f}")

    print("Nota más alta de toda la tabla:", max(max(fila) for fila in notas))


if __name__ == "__main__":
    elegir_y_ejecutar("Arreglos", {
        1: ejercicio_1, 2: ejercicio_2, 3: ejercicio_3,
        4: ejercicio_4, 5: ejercicio_5, 6: ejercicio_6,
    })
