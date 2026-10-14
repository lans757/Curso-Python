# ============================================================================
# GUÍA DE OBJETOS EN PYTHON
# ============================================================================
# Equivale a: objetos/objeto.php · objetos/objeto.js · Objeto.cs
# PSeInt no tiene objetos: es un lenguaje estructurado.
#
# Diferencias de escritura con PHP, JS y C#:
# - El constructor se llama __init__ (en PHP __construct; en JS constructor).
# - El objeto actual se llama "self" (en los demás, $this o this) y hay que
#   escribirlo como PRIMER PARÁMETRO de cada método. Al llamar no se pasa.
# - Para crear un objeto NO se escribe "new":  persona = Persona(...)
# - No existen public / private / protected. Por convención, un nombre que
#   empieza con guion bajo (_saldo) significa "esto es interno, no lo toques".
# ============================================================================


# 1. Definición de una clase: un molde o plantilla para crear objetos.
class Persona:
    # 3. Constructor: se ejecuta automáticamente al crear un objeto.
    def __init__(self, nombre, edad, pais):
        # 2. Propiedades (atributos): se crean al asignarlas a self.
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    # 4. Métodos (acciones)
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("País:", self.pais)

    # Método especial: define cómo se ve el objeto al hacer print(objeto).
    # Equivale a __toString() en PHP y a ToString() en C#.
    def __str__(self):
        return f"Persona({self.nombre}, {self.edad})"


# 6. Herencia: una clase (hija) hereda propiedades y métodos de otra (padre).
#   PHP:  class Estudiante extends Persona
#   C#:   class Estudiante : Persona
#   Python: class Estudiante(Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, pais, carrera):
        super().__init__(nombre, edad, pais)     # llamar al constructor del padre
        self.carrera = carrera

    def estudiar(self):
        return f"Estoy estudiando {self.carrera}."

    # Sobrescribir un método: basta con definirlo de nuevo con el mismo nombre.
    # (En C# hacían falta "virtual" y "override"; en Python y PHP, no.)
    def saludar(self):
        return f"Hola, soy el estudiante {self.nombre} y estudio {self.carrera}."


# 7. Miembros estáticos: se usan sin crear un objeto de la clase.
class Calculadora:
    PI = 3.1416                    # atributo de clase (compartido por todos)

    @staticmethod
    def sumar(a, b):
        return a + b


# 5. Instanciación (crear un objeto)
persona1 = Persona("Juan", 25, "México")
persona2 = Persona("Maria", 30, "España")

print("Ejemplo básico:")
print(persona1.saludar())
persona2.mostrar_info()
print("Con print(objeto):", persona1)

print("\nEjemplo de herencia:")
estudiante1 = Estudiante("Carlos", 20, "Argentina", "Ingeniería")
print(estudiante1.saludar())
print(estudiante1.estudiar())
print("¿Un estudiante es una Persona?", isinstance(estudiante1, Persona))

print("\nEjemplo de estáticos:")
print("Valor de PI:", Calculadora.PI)
print("Suma de 5 + 10:", Calculadora.sumar(5, 10))


# ----------------------------------------------------------------------------
# 8. Encapsulamiento: proteger un dato con una propiedad
# @property permite que un método se use como si fuera un atributo, y así
# controlar qué valores se aceptan (lo que en C# es "get; set;").
# ----------------------------------------------------------------------------
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo                # el guion bajo avisa: "es interno"

    @property
    def saldo(self):
        return self._saldo

    def retirar(self, monto):
        if monto > self._saldo:
            print("Fondos insuficientes")
        else:
            self._saldo -= monto


print("\nEjemplo de encapsulamiento:")
cuenta = Cuenta("Ana", 500)
cuenta.retirar(200)
print("Saldo:", cuenta.saldo)              # se lee como atributo, sin paréntesis
cuenta.retirar(9999)
# cuenta.saldo = 1000000    # AttributeError: la propiedad es de solo lectura

# ----------------------------------------------------------------------------
# 9. "Objetos literales" de JavaScript
# En JS se escribe  let persona = { nombre: "Ana", edad: 30 }  sin clase.
# En Python eso es un diccionario; se accede con corchetes, no con punto.
# ----------------------------------------------------------------------------
persona_js = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print("\nDiccionario (el objeto literal de JS):", persona_js["nombre"])
