# ============================================================================
# TRAITS — EQUIVALENTE EN PYTHON: MIXINS
# ============================================================================
# Equivale a: poo/traits.php · Traits.cs
#
# PHP tiene herencia simple (una clase solo puede "extends" de UN padre) y
# resuelve la reutilización de código entre clases sin relación con Traits:
# bloques de código que se "pegan" dentro de una clase con "use".
#
# Python no necesita Traits porque tiene HERENCIA MÚLTIPLE. El patrón
# equivalente se llama MIXIN: una clase pequeña que no representa nada por
# sí sola, solo aporta una habilidad, y que otras clases agregan a su lista
# de padres.
#
#   PHP:     class Producto { use UtilidadesLog, ConvertidorString; }
#   Python:  class Producto(UtilidadesLog, ConvertidorString):
#
# A diferencia del "equivalente" de C# (interfaces con método por defecto),
# un mixin de Python SÍ puede tener estado propio, igual que un Trait real.
# ============================================================================

from datetime import datetime


# "Trait" 1: saber escribir en un registro (log)
class UtilidadesLog:
    def loguear(self, mensaje):
        momento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{momento}: {mensaje}"


# "Trait" 2: saber transformar textos
class ConvertidorString:
    def a_mayusculas(self, texto):
        return texto.upper()


class Usuario(UtilidadesLog):
    def __init__(self, nombre):
        self.nombre = nombre
        # El método del mixin queda disponible directamente en self,
        # igual que el método de un Trait queda disponible en $this.
        print(self.loguear(f"Usuario {nombre} creado"))


# Una clase puede usar VARIOS mixins, igual que PHP permite "use" de varios Traits.
class Producto(UtilidadesLog, ConvertidorString):
    def guardar(self):
        print(self.loguear("Producto guardado correctamente"))

    def mostrar_nombre(self, nombre):
        print(self.a_mayusculas(nombre))


print('Ejemplo de "Traits" (mixins)\n')

user = Usuario("Carlos")               # al crear, usa loguear() del mixin

prod = Producto()
prod.guardar()                         # usa loguear() de UtilidadesLog
prod.mostrar_nombre("laptop gamer")    # usa a_mayusculas() de ConvertidorString

# ----------------------------------------------------------------------------
# ¿Qué pasa si dos padres tienen un método con el mismo nombre?
# Gana el que está PRIMERO en la lista de padres. El orden completo de
# búsqueda se puede ver con __mro__ (Method Resolution Order).
# ----------------------------------------------------------------------------
print("\nOrden en que Python busca los métodos de Producto:")
for clase in Producto.__mro__:
    print("  ->", clase.__name__)

# ----------------------------------------------------------------------------
# Consejo: un mixin debe ser pequeño y aportar UNA sola habilidad. Si empieza
# a crecer, suele ser mejor la composición: que la clase TENGA un objeto
# (self.logger = Logger()) en vez de SER varias cosas a la vez.
# ----------------------------------------------------------------------------
