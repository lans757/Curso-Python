# ============================================================================
# DECORADORES Y ADMINISTRADORES DE CONTEXTO
# ============================================================================
# Idiomático de Python. Lo más parecido en los otros cursos:
#   C#:   atributos como [Authorize] y el bloque "using"
#   PHP:  atributos #[...] de PHP 8
#   JS:   funciones de orden superior (una función que recibe otra función)
#
# Ya usaste varios sin saber qué eran:
#   @staticmethod, @property           (objetos/objeto.py)
#   @abstractmethod                    (poo/clases_abstractas.py)
#   @dataclass                         (objetos/clases_de_datos.py)
#   @app.route("/")                    (curso_web/app.py)
#   with open(...) as archivo:         (archivos/)
#
# Un DECORADOR es una función que envuelve a otra para agregarle algo ANTES
# o DESPUÉS, sin tocar su código. Como el papel de regalo: el regalo es el
# mismo, pero ahora viene envuelto.
# ============================================================================

import functools
import time
from contextlib import contextmanager


# ----------------------------------------------------------------------------
# 0. La idea de base: en Python las funciones son valores
# Se pueden guardar en una variable y pasar como argumento.
# ----------------------------------------------------------------------------
def saludar(nombre):
    return f"Hola, {nombre}"


mi_funcion = saludar                 # sin paréntesis: no la llama, la guarda
print("0. Función guardada en una variable:", mi_funcion("Ana"))


# ----------------------------------------------------------------------------
# 1. Un decorador sencillo
# ----------------------------------------------------------------------------
def anunciar(funcion):
    @functools.wraps(funcion)        # conserva el nombre de la función original
    def envoltura(*args, **kwargs):
        print(f"   -> Voy a ejecutar {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"   <- Terminó {funcion.__name__}")
        return resultado
    return envoltura


@anunciar                            # equivale a:  sumar = anunciar(sumar)
def sumar(a, b):
    return a + b


print("\n1. Función decorada con @anunciar")
print("Resultado:", sumar(3, 4))


# ----------------------------------------------------------------------------
# 2. Un decorador útil: medir cuánto tarda una función
# ----------------------------------------------------------------------------
def cronometrar(funcion):
    @functools.wraps(funcion)
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        print(f"   {funcion.__name__} tardó {duracion:.4f} segundos")
        return resultado
    return envoltura


@cronometrar
def sumar_hasta(n):
    return sum(range(n + 1))


print("\n2. Decorador @cronometrar")
print("Suma del 1 al 1.000.000:", sumar_hasta(1_000_000))


# ----------------------------------------------------------------------------
# 3. Un decorador de permisos (la idea detrás de [Authorize] en C#)
# ----------------------------------------------------------------------------
usuario_actual = {"nombre": "Ana", "es_admin": False}


def solo_admin(funcion):
    @functools.wraps(funcion)
    def envoltura(*args, **kwargs):
        if not usuario_actual["es_admin"]:
            print("   Acceso denegado: se necesita ser administrador.")
            return None
        return funcion(*args, **kwargs)
    return envoltura


@solo_admin
def borrar_inventario():
    print("   Inventario borrado.")


print("\n3. Decorador @solo_admin")
borrar_inventario()
usuario_actual["es_admin"] = True
borrar_inventario()


# ----------------------------------------------------------------------------
# 4. Uno que ya viene hecho: recordar resultados con @functools.cache
# La primera vez calcula; las siguientes devuelve lo que ya tenía guardado.
# ----------------------------------------------------------------------------
@functools.cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\n4. @functools.cache")
print("fibonacci(80) =", fibonacci(80))      # sin cache tardaría años


# ----------------------------------------------------------------------------
# 5. Administradores de contexto: el bloque "with"
# Garantizan que algo se CIERRE o se DESHAGA al salir del bloque, pase lo que
# pase. Es el "using" de C#. Con @contextmanager se escribe uno propio:
# lo que va antes del yield se ejecuta al entrar; lo que va después, al salir.
# ----------------------------------------------------------------------------
@contextmanager
def seccion(titulo):
    print(f"   === Inicio: {titulo} ===")
    try:
        yield
    finally:
        print(f"   === Fin: {titulo} ===")


print("\n5. Administrador de contexto propio")
with seccion("Reporte del día"):
    print("   Ventas: 15")
    print("   Total: 320.50")

# *args y **kwargs, que aparecen en las envolturas, significan "cualquier
# cantidad de argumentos, con o sin nombre". Permiten que el decorador sirva
# para funciones con parámetros distintos.
