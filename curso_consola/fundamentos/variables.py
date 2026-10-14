# ============================================================================
# VARIABLES EN PYTHON
# ============================================================================
# Equivale a: fundamentos/variables.php · variables.js · Variables.cs
#             PSeInt módulo 1 (variables y datos)
#
# Notas:
# - Los nombres distinguen mayúsculas de minúsculas (nombre y Nombre son dos
#   variables distintas). En PSeInt eran la misma.
# - No pueden llevar espacios, empezar por un número ni llevar símbolos.
# - Por convención se escriben en minúsculas con guion bajo: precio_total
#   (en JS y C# se usa precioTotal).
# - NO se declaran: una variable nace cuando se le asigna un valor.
#
#   PSeInt:  Definir edad Como Entero;  edad <- 16;
#   PHP:     $edad = 16;
#   JS:      let edad = 16;
#   C#:      int edad = 16;
#   Python:  edad = 16
#
# Tipos de datos básicos:
# - str:   texto                 ("Hola")
# - int:   número entero         (7)
# - float: número con decimales  (1.2)
# - bool:  verdadero o falso     (True / False, con mayúscula inicial)
# - None:  "sin valor"           (el null de PHP, JS y C#)
# ============================================================================

# Texto (str)
nombre = "Juan"

# Entero (int)
numero = 1

# Decimal (float)
decimal = 1.2

# Booleano (bool)
booleano = True

# Nulo (None)
nulo = None

# ----------------------------------------------------------------------------
# Comillas simples vs. comillas dobles
# En Python son IGUALES: ninguna interpreta variables por sí sola (en PHP las
# dobles sí). Para meter variables dentro de un texto se usa una f-string:
# una letra f antes de las comillas y la variable entre llaves.
# ----------------------------------------------------------------------------
print(f"Mi nombre es {nombre}")          # f-string (la forma recomendada)
print("Mi nombre es " + nombre)          # concatenación con +
print("Mi nombre es", nombre)            # print separa con un espacio

print("Numero:", numero)
print("Decimal:", decimal)
print("Booleano:", booleano)
print("Estado:", nulo)

# ----------------------------------------------------------------------------
# Tipado dinámico: la variable no tiene tipo fijo, lo tiene el VALOR
# Igual que en PHP y JS; al revés que en C# y PSeInt.
# ----------------------------------------------------------------------------
dato = "texto"
print("\ndato vale", dato, "y es de tipo", type(dato).__name__)
dato = 5
print("dato vale", dato, "y es de tipo", type(dato).__name__)

# Pero Python es de tipado FUERTE: no mezcla tipos por su cuenta.
# En PHP "5" + 5 da 10 y en JS da "55". En Python da un error:
# print("5" + 5)   # TypeError: can only concatenate str (not "int") to str

# ----------------------------------------------------------------------------
# Conversión de tipos (hay que pedirla explícitamente)
# ----------------------------------------------------------------------------
numero_texto = "123"
print("\nTexto a entero:", int(numero_texto) + 1)        # 124
print("Texto a decimal:", float("3.14") * 2)             # 6.28
print("Número a texto:", str(789) + " unidades")         # "789 unidades"
print("Cualquier cosa a booleano:", bool(""), bool("hola"), bool(0), bool(7))

# ----------------------------------------------------------------------------
# Asignación múltiple e intercambio
# En PSeInt hacía falta una variable auxiliar para intercambiar dos valores.
# En Python se hace en una línea.
# ----------------------------------------------------------------------------
a, b = 5, 8
a, b = b, a
print("\nDespués de intercambiar: a =", a, " b =", b)

# ----------------------------------------------------------------------------
# Estructuras complejas: clases y objetos (se ven a fondo en objetos/)
# ----------------------------------------------------------------------------


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mensaje(self):
        return f"Mi carro es un {self.marca} {self.modelo}"


mi_carro = Carro("Toyota", "Corolla")
print("\nObjeto:", mi_carro.mensaje())
