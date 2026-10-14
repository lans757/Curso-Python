# ============================================================================
# EXCEPCIONES PERSONALIZADAS EN PYTHON
# ============================================================================
# Equivale a: errores/excepciones_personalizadas.php · ExcepcionesPersonalizadas.cs
#
# Igual que en PHP y C#, podemos crear nuestras propias clases de error
# heredando de la clase base "Exception", para tener errores más específicos
# en nuestra aplicación.
#
#   PHP:     class InventarioException extends Exception { }
#   C#:      class InventarioException : Exception { }
#   Python:  class InventarioError(Exception):
#
# Convención de Python: los nombres de las excepciones terminan en "Error".
# ============================================================================


# Creamos nuestra propia clase de error
class InventarioError(Exception):
    def obtener_detalles(self):
        # str(self) devuelve el mensaje con el que se lanzó la excepción.
        return "Error de Inventario: " + str(self)


class Producto:
    def __init__(self, stock):
        self.stock = stock

    def comprar(self, cantidad):
        if cantidad > self.stock:
            # Lanzamos nuestra excepción personalizada
            raise InventarioError("No hay suficiente stock disponible.")

        self.stock -= cantidad
        print(f"Compra exitosa. Stock restante: {self.stock}")


print("Prueba de excepción personalizada")

try:
    camisa = Producto(5)                 # inventario inicial: 5

    print("Intentando comprar 3 camisas...")
    camisa.comprar(3)                    # esto funciona

    print("Intentando comprar 4 camisas más...")
    camisa.comprar(4)                    # esto debería fallar
except InventarioError as e:
    # Capturamos específicamente los errores de inventario. Igual que en PHP
    # y C#, el except más específico debe ir ANTES que el genérico: Python
    # usa el primero que coincida.
    print(e.obtener_detalles())
except Exception as e:
    # Este bloque atraparía cualquier otro error.
    print("Error genérico:", e)


# ----------------------------------------------------------------------------
# Una excepción puede llevar datos adicionales
# ----------------------------------------------------------------------------
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Quisiste retirar {monto} y solo tienes {saldo}.")


def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto


print("\nExcepción con datos adicionales")
try:
    nuevo_saldo = retirar(100, 250)
except SaldoInsuficienteError as e:
    print("No se pudo retirar:", e)
    print("Te faltan:", e.monto - e.saldo)

# ----------------------------------------------------------------------------
# ¿Para qué sirve crear excepciones propias?
# Para que quien use tu código pueda distinguir "se acabó el stock" (algo
# esperable, que se le explica al cliente) de "se cayó la base de datos"
# (algo grave), y reaccionar distinto ante cada uno.
# ----------------------------------------------------------------------------
