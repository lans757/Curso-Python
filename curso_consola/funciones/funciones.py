# ============================================================================
# DECLARACIÓN DE FUNCIONES EN PYTHON
# ============================================================================
# Equivale a: funciones/funciones.php · funciones.js · Funciones.cs
#             PSeInt módulo 6 (Funcion y SubProceso)
#
# Una función es un bloque de código con nombre que podemos ejecutar muchas
# veces llamándolo.
#
#   PSeInt:  SubProceso saludar(nombre) ... FinSubProceso
#            Funcion r <- sumar(a, b) ... FinFuncion
#   PHP/JS:  function sumar($a, $b) { return $a + $b; }
#   C#:      static int Sumar(int a, int b) { return a + b; }
#   Python:  def sumar(a, b):
#                return a + b
#
# - Se define con "def" y dos puntos; el cuerpo va con sangría.
# - PSeInt separaba SubProceso (no devuelve nada) y Funcion (devuelve algo).
#   En Python todo es "def": si tiene return devuelve un valor; si no, devuelve None.
# - La función debe estar DEFINIDA antes de la línea que la llama.
# ============================================================================


# 1. Función simple
def saludar():
    print("Hola, ¡bienvenido al curso de Python!")


# 2. Función con parámetros
def saludar_usuario(nombre):
    print(f"Hola {nombre}, ¿cómo estás hoy?")


# 3. Función con retorno
def sumar(num1, num2):
    resultado = num1 + num2
    return resultado


saludar()
print("----------")

saludar_usuario("Carlos")
saludar_usuario("Maria")
print("----------")

total = sumar(10, 5)
print(f"El resultado de la suma es: {total}")


# ----------------------------------------------------------------------------
# 4. Parámetros con valor por defecto
# Si no se envía el dato, se usa el valor indicado en la definición.
# ----------------------------------------------------------------------------
def calcular_precio(precio, iva=0.16):
    return precio + precio * iva


print("\nCon IVA por defecto:", calcular_precio(100))
print("Con otro IVA:", calcular_precio(100, 0.08))

# ----------------------------------------------------------------------------
# 5. Argumentos con nombre
# Al llamar se puede decir a qué parámetro va cada dato. Así el orden no
# importa y la llamada se explica sola.
# ----------------------------------------------------------------------------
print("Con nombres:", calcular_precio(iva=0.08, precio=100))


# ----------------------------------------------------------------------------
# 6. Devolver varios valores
# En PSeInt hacía falta "Por Referencia" para sacar dos resultados de una
# función. En Python se devuelven juntos, separados por coma (es una tupla).
# ----------------------------------------------------------------------------
def estadisticas(notas):
    return min(notas), max(notas), sum(notas) / len(notas)


menor, mayor, promedio = estadisticas([12, 18, 9, 15])
print(f"\nMenor: {menor}  Mayor: {mayor}  Promedio: {promedio}")


# ----------------------------------------------------------------------------
# 7. Por valor y por referencia
# Python no tiene la palabra "Por Referencia" de PSeInt ni el & de PHP.
# La regla práctica:
# - Números, textos y booleanos: la función NO puede cambiar el original.
# - Listas y diccionarios: si la función los MODIFICA, el original cambia
#   (igual que los arreglos en PSeInt, PHP con &, JS y C#).
# ----------------------------------------------------------------------------
def duplicar_numero(n):
    n = n * 2                       # solo cambia la copia local


def agregar_nota(lista, nota):
    lista.append(nota)              # modifica la lista original


numero = 10
duplicar_numero(numero)
print("\nEl número sigue igual:", numero)

mis_notas = [15, 18]
agregar_nota(mis_notas, 20)
print("La lista sí cambió:", mis_notas)


# ----------------------------------------------------------------------------
# 8. Documentar una función: el docstring
# Un texto entre comillas triples justo debajo del def. Lo muestran los
# editores al pasar el ratón y la función help().
# ----------------------------------------------------------------------------
def es_par(numero):
    """Devuelve True si el número es par."""
    return numero % 2 == 0


print("\n¿8 es par?", es_par(8))
print("Documentación:", es_par.__doc__)

# ----------------------------------------------------------------------------
# 9. Funciones cortas en una línea: lambda
# Equivale a las funciones flecha de JS (x => x * 2) y de PHP (fn($x) => $x * 2).
# Se usan sobre todo como argumento de otra función (por ejemplo, key en sorted).
# ----------------------------------------------------------------------------
doble = lambda x: x * 2
print("\nLambda doble(7):", doble(7))

palabras = ["sol", "computadora", "casa"]
print("Ordenadas por la última letra:", sorted(palabras, key=lambda p: p[-1]))
