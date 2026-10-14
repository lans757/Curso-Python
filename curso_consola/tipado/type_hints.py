# ============================================================================
# ANOTACIONES DE TIPO (TYPE HINTS), OPCIONALES Y GENÉRICOS
# ============================================================================
# Idiomático de Python. Reúne dos temas del curso de C#:
#   genericos/Generics.cs  y  nullable/NullableReferenceTypes.cs
# Se parece también a TypeScript frente a JavaScript, y a "Definir x Como
# Entero" de PSeInt.
#
# Python es de tipado dinámico: una variable puede guardar cualquier cosa.
# Eso es cómodo, pero los errores de tipo aparecen tarde, al ejecutar.
#
# Las anotaciones de tipo permiten ESCRIBIR qué tipo se espera:
#
#   def sumar(a: int, b: int) -> int:
#
# LO MÁS IMPORTANTE: Python NO las comprueba al ejecutar. Son una ayuda para
# las personas y para las herramientas: el editor (VS Code) autocompleta
# mejor y subraya los errores, y programas como "mypy" revisan todo el
# proyecto antes de ejecutarlo. Es la diferencia con C#, donde el compilador
# se niega a continuar.
# ============================================================================

from typing import Optional, TypeVar


# ----------------------------------------------------------------------------
# 1. Anotar variables, parámetros y el valor de retorno
# ----------------------------------------------------------------------------
nombre: str = "Ana"
edad: int = 12
estatura: float = 1.52
activo: bool = True


def calcular_promedio(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def saludar(nombre: str, veces: int = 1) -> None:      # None = no devuelve nada
    for _ in range(veces):
        print(f"Hola, {nombre}")


print("1. Funciones anotadas")
print("Promedio:", calcular_promedio([15, 18, 12]))
saludar("Ana", 2)

# Python NO impide esto al ejecutar (pero el editor sí lo subraya):
edad = "doce"          # el tipo anotado era int
print("edad ahora vale:", edad, "(Python no se quejó)")

# ----------------------------------------------------------------------------
# 2. Colecciones
# ----------------------------------------------------------------------------
notas: list[int] = [15, 18, 20]
precios: dict[str, float] = {"Arroz": 2.5, "Harina": 1.8}
coordenada: tuple[float, float] = (8.62, -70.21)


# ----------------------------------------------------------------------------
# 3. Valores que pueden ser None — el "string?" de C#
#   C#:      string? buscar(...)
#   Python:  str | None        (o Optional[str], que significa lo mismo)
# Avisa a quien use la función: "antes de usar el resultado, pregunta si es None".
# ----------------------------------------------------------------------------
def buscar_telefono(agenda: dict[str, str], nombre: str) -> str | None:
    return agenda.get(nombre)


def buscar_edad(edades: dict[str, int], nombre: str) -> Optional[int]:
    return edades.get(nombre)


agenda = {"Ana": "0414-1234567"}

print("\n3. Valores opcionales")
telefono = buscar_telefono(agenda, "Luis")

# Sin esta pregunta, telefono.replace(...) fallaría con AttributeError.
if telefono is not None:
    print("Teléfono:", telefono.replace("-", ""))
else:
    print("Luis no está en la agenda")

# Valor por defecto si es None (el operador ?? de C# y PHP)
print("Con valor por defecto:", buscar_telefono(agenda, "Luis") or "Sin teléfono")
print("Edad:", buscar_edad({"Ana": 12}, "Ana"))


# ----------------------------------------------------------------------------
# 4. Genéricos — "T" es un tipo que se decide al usar la función
# En C#:  static T Primero<T>(List<T> lista)
# Dice: "si me das una lista de textos devuelvo un texto; si es de números,
# un número". Sin el genérico solo podríamos decir "devuelvo cualquier cosa".
# ----------------------------------------------------------------------------
T = TypeVar("T")


def primero(lista: list[T]) -> T:
    return lista[0]


def maximo(a: T, b: T) -> T:
    return a if a > b else b


print("\n4. Funciones genéricas")
print("Primero de una lista de textos:", primero(["sol", "luna"]))
print("Primero de una lista de números:", primero([7, 8, 9]))
print("Máximo de 3 y 9:", maximo(3, 9))
print("Máximo de 'ana' y 'luis':", maximo("ana", "luis"))


# ----------------------------------------------------------------------------
# 5. Clase genérica — la Caja<T> del curso de C#
# ----------------------------------------------------------------------------
class Caja[T]:                       # sintaxis de Python 3.12 en adelante
    def __init__(self, contenido: T) -> None:
        self.contenido = contenido

    def abrir(self) -> T:
        return self.contenido


print("\n5. Clase genérica")
caja_de_texto = Caja("un secreto")
caja_de_numero = Caja(42)
print("Caja de texto:", caja_de_texto.abrir().upper())
print("Caja de número:", caja_de_numero.abrir() + 1)

# ----------------------------------------------------------------------------
# 6. Las anotaciones quedan guardadas y se pueden consultar
# ----------------------------------------------------------------------------
print("\n6. Anotaciones de calcular_promedio:")
print(calcular_promedio.__annotations__)

# ----------------------------------------------------------------------------
# ¿Vale la pena escribirlas?
# En un ejercicio de diez líneas, no. En un proyecto de varios archivos o en
# equipo, sí: son documentación que el editor puede comprobar.
# ----------------------------------------------------------------------------
