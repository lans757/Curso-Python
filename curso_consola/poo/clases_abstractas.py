# ============================================================================
# CLASES ABSTRACTAS EN PYTHON
# ============================================================================
# Equivale a: poo/clases_abstractas.php · ClasesAbstractas.cs
#
# Una clase abstracta NO se puede instanciar directamente (no puedes hacer
# Animal("Test")). Sirve como modelo base estricto para otras clases.
#
# Puede contener:
# 1. Métodos abstractos: sin cuerpo; las clases hijas ESTÁN OBLIGADAS a
#    implementarlos.
# 2. Métodos normales: con cuerpo; las hijas los heredan tal cual.
#
# Diferencia con PHP y C#: allá "abstract" es una palabra del lenguaje.
# En Python se arma con el módulo abc (Abstract Base Classes):
#   - la clase hereda de ABC
#   - cada método obligatorio lleva el decorador @abstractmethod
# ============================================================================

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    # Método normal (común para todos)
    def dormir(self):
        return f"{self.nombre} está durmiendo. Zzz..."

    # Método ABSTRACTO (obligatorio de implementar). El cuerpo queda vacío:
    # "pass" es la instrucción de Python para "aquí no va nada".
    @abstractmethod
    def hacer_sonido(self):
        pass


class Perro(Animal):
    # Estamos OBLIGADOS a definir hacer_sonido()
    def hacer_sonido(self):
        return "¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"


print("Ejemplo de clases abstractas")

mi_perro = Perro("Firulais")
mi_gato = Gato("Michi")

print(mi_perro.dormir())
print("El perro hace:", mi_perro.hacer_sonido())
print()
print(mi_gato.dormir())
print("El gato hace:", mi_gato.hacer_sonido())

# ----------------------------------------------------------------------------
# Intentar crear un Animal directamente da error. En C# el error aparece al
# COMPILAR; en Python y PHP aparece al EJECUTAR esa línea.
# ----------------------------------------------------------------------------
print("\nIntentando crear un Animal directamente...")
try:
    animal = Animal("Test")
except TypeError as error:
    print("Error:", error)


# ----------------------------------------------------------------------------
# Y si una clase hija "olvida" implementar el método obligatorio, tampoco
# se puede instanciar.
# ----------------------------------------------------------------------------
class Pez(Animal):
    pass            # no define hacer_sonido()


print("\nIntentando crear un Pez que no implementó hacer_sonido()...")
try:
    nemo = Pez("Nemo")
except TypeError as error:
    print("Error:", error)

# ----------------------------------------------------------------------------
# Polimorfismo: tratar a todos como "Animal" sin importar cuál es cada uno
# ----------------------------------------------------------------------------
print("\nTodos los animales hacen su sonido:")
for animal in [mi_perro, mi_gato]:
    print(f"  {animal.nombre}: {animal.hacer_sonido()}")
