# ============================================================================
# INTERFACES EN PYTHON
# ============================================================================
# Equivale a: poo/interfaces.php · Interfaces.cs
#
# Una interfaz es un contrato: dice QUÉ métodos debe tener una clase, pero
# no CÓMO funcionan. Una clase puede cumplir VARIOS contratos.
#
# Python NO tiene la palabra "interface". Hay dos formas de lograr lo mismo:
#
# A) Clase abstracta con SOLO métodos abstractos (lo más parecido a PHP/C#).
#    La clase declara qué contratos cumple heredando de ellos.
#
# B) Protocol ("duck typing" con nombre): la clase NO declara nada. Si tiene
#    los métodos, cumple el contrato. "Si camina como pato y hace cuac como
#    pato, es un pato".
#
# Como Python permite HERENCIA MÚLTIPLE, una clase puede heredar de varias
# interfaces a la vez (en PHP y C# solo se hereda de una clase, pero se
# implementan varias interfaces: el resultado es el mismo).
# ============================================================================

from abc import ABC, abstractmethod
from typing import Protocol


# ----------------------------------------------------------------------------
# FORMA A: interfaces como clases abstractas
# ----------------------------------------------------------------------------
class ReproducibleMultimedia(ABC):
    @abstractmethod
    def reproducir(self):
        pass

    @abstractmethod
    def pausar(self):
        pass


class Grabable(ABC):
    @abstractmethod
    def grabar(self):
        pass


# Clase que cumple el contrato de ReproducibleMultimedia
class ReproductorMp3(ReproducibleMultimedia):
    def reproducir(self):
        return "Reproduciendo música MP3..."

    def pausar(self):
        return "Música pausada."


# Clase que cumple DOS contratos (herencia múltiple)
#   PHP:  class Celular implements ReproducibleMultimedia, Grabable
#   C#:   class Celular : IReproducibleMultimedia, IGrabable
class Celular(ReproducibleMultimedia, Grabable):
    def reproducir(self):
        return "Reproduciendo video en YouTube..."

    def pausar(self):
        return "Video pausado."

    def grabar(self):
        return "Grabando nota de voz..."


print("Ejemplo de interfaces (forma A: clases abstractas)")

ipod = ReproductorMp3()
print("MP3:", ipod.reproducir())

iphone = Celular()
print("Celular:", iphone.reproducir(), "y luego", iphone.grabar())

print("¿El celular es Grabable?", isinstance(iphone, Grabable))
print("¿El MP3 es Grabable?", isinstance(ipod, Grabable))


# ----------------------------------------------------------------------------
# FORMA B: Protocol (duck typing)
# ----------------------------------------------------------------------------
class Volador(Protocol):
    def volar(self) -> str: ...


# Estas dos clases NO heredan de Volador ni lo mencionan.
class Avion:
    def volar(self):
        return "El avión despega de la pista."


class Pajaro:
    def volar(self):
        return "El pájaro bate las alas."


def despegar(cosa: Volador):
    # A esta función le da igual la clase: solo necesita que exista .volar()
    print(cosa.volar())


print("\nEjemplo de interfaces (forma B: Protocol / duck typing)")
despegar(Avion())
despegar(Pajaro())

# ----------------------------------------------------------------------------
# ¿Cuál usar?
# - Forma A cuando quieres que Python IMPIDA crear una clase incompleta.
# - Forma B cuando solo quieres documentar qué se espera y que el editor
#   avise. Es la más común en código Python moderno.
# ----------------------------------------------------------------------------
