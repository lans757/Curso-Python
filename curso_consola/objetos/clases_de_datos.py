# ============================================================================
# CLASES DE DATOS: @dataclass
# ============================================================================
# Idiomático de Python. Lo más parecido en los otros cursos:
#   C#:  record Producto(string Nombre, double Precio);
#   JS:  un objeto literal { nombre: "Arroz", precio: 2.5 }
#   PHP: una clase con "constructor property promotion" (PHP 8)
#
# Muchas clases solo sirven para GUARDAR DATOS, y su constructor es puro
# trámite: self.nombre = nombre, self.precio = precio, self.stock = stock...
#
# El decorador @dataclass escribe ese trámite por ti. Solo declaras los
# campos con su tipo y Python genera el __init__, una representación legible
# para print() y la comparación con ==.
# ============================================================================

from dataclasses import dataclass, field


# ----------------------------------------------------------------------------
# 1. La forma larga (clase normal)
# ----------------------------------------------------------------------------
class ProductoLargo:
    def __init__(self, codigo, nombre, existencia, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.existencia = existencia
        self.precio = precio


# ----------------------------------------------------------------------------
# 2. La misma clase con @dataclass
# ----------------------------------------------------------------------------
@dataclass
class Producto:
    codigo: int
    nombre: str
    existencia: int = 0            # valor por defecto
    precio: float = 0.0

    # Sigue siendo una clase normal: puede tener métodos.
    def valor_total(self):
        return self.existencia * self.precio


arroz = Producto(101, "Arroz", 40, 2.5)
harina = Producto(codigo=102, nombre="Harina")       # usa los valores por defecto

print("print() de una clase normal:  ", ProductoLargo(101, "Arroz", 40, 2.5))
print("print() de una dataclass:     ", arroz)
print("Con valores por defecto:      ", harina)
print("Valor del arroz en inventario:", arroz.valor_total())

# ----------------------------------------------------------------------------
# 3. Comparación por contenido
# Dos objetos de una clase normal solo son "iguales" si son EL MISMO objeto.
# Dos dataclasses son iguales si tienen los mismos datos.
# ----------------------------------------------------------------------------
print("\n¿Dos productos con los mismos datos son iguales?")
print(Producto(1, "Sal") == Producto(1, "Sal"))


# ----------------------------------------------------------------------------
# 4. Datos que no deben cambiar: frozen=True
# ----------------------------------------------------------------------------
@dataclass(frozen=True)
class Coordenada:
    latitud: float
    longitud: float


barinas = Coordenada(8.62, -70.21)
print("\nCoordenada inmutable:", barinas)
# barinas.latitud = 0     # FrozenInstanceError


# ----------------------------------------------------------------------------
# 5. Un campo que es una lista
# No se puede escribir  productos: list = []  (todas las instancias
# compartirían la MISMA lista). Se usa field(default_factory=list).
# ----------------------------------------------------------------------------
@dataclass
class Inventario:
    nombre: str
    productos: list = field(default_factory=list)

    def agregar(self, producto):
        self.productos.append(producto)

    def valor(self):
        return sum(p.valor_total() for p in self.productos)


bodega = Inventario("Bodega central")
bodega.agregar(arroz)
bodega.agregar(Producto(103, "Aceite", 8, 4.2))

print("\nInventario:", bodega.nombre)
for producto in bodega.productos:
    print(" -", producto.nombre, producto.existencia, "unidades")
print("Valor total:", bodega.valor())
