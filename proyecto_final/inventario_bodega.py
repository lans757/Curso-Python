# ============================================================================
# PROYECTO FINAL — SISTEMA DE INVENTARIO DE UNA BODEGA (solución de referencia)
# ============================================================================
# Viene de: 08_proyecto_final/soluciones/inventario_bodega.psc (curso de PSeInt)
#           warehouse-inventory-system (curso de PHP, versión simplificada)
#
# Integra todo el curso:
#   fundamentos      -> variables, operadores, f-strings
#   condicionales    -> validaciones y match para el menú
#   ciclos           -> el menú que se repite, los recorridos
#   arreglos         -> lista de diccionarios (un diccionario por producto)
#   funciones        -> una función por cada opción del menú
#   errores          -> try/except para que no se rompa con datos incorrectos
#   archivos         -> el inventario se guarda en un archivo y no se pierde
#   comprensiones    -> el reporte
#
# Qué cambió respecto a la versión de PSeInt:
# - Cuatro arreglos paralelos + la variable "cantidad"  ->  UNA lista de diccionarios.
# - Ya no hay límite de 50 productos: la lista crece sola.
# - "Por Referencia" desaparece: las listas se modifican directamente.
# - Los datos se guardan en inventario.json (PSeInt no podía escribir archivos).
# ============================================================================

import json
from pathlib import Path

ARCHIVO = Path(__file__).parent / "inventario.json"
STOCK_BAJO = 5


# ----------------------------------------------------------------------------
# Guardar y cargar (módulo de archivos)
# JSON es un formato de texto para guardar listas y diccionarios. Nació en
# JavaScript, y se parece tanto a las estructuras de Python que convertir de
# uno a otro es una sola línea.
# ----------------------------------------------------------------------------
def cargar():
    if not ARCHIVO.exists():
        return []
    try:
        return json.loads(ARCHIVO.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("El archivo de inventario está dañado. Se empieza con uno vacío.")
        return []


def guardar(productos):
    ARCHIVO.write_text(json.dumps(productos, indent=2, ensure_ascii=False), encoding="utf-8")


# ----------------------------------------------------------------------------
# Funciones de apoyo: pedir datos validados
# Repiten la pregunta hasta que el dato sea correcto (el "Repetir ... Hasta
# Que" de PSeInt) y además aguantan que el usuario escriba letras.
# ----------------------------------------------------------------------------
def pedir_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Escribe un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"El valor debe ser {minimo} o más.")
            continue
        return valor


def pedir_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Escribe un número (usa punto para los decimales).")
            continue
        if valor <= 0:
            print("El precio debe ser mayor a cero.")
            continue
        return valor


def buscar(productos, codigo):
    """Devuelve el producto con ese código, o None si no existe."""
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def mostrar_menu():
    print()
    print("===== INVENTARIO DE LA BODEGA =====")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto por código")
    print("4. Registrar entrada de mercancía")
    print("5. Registrar salida de mercancía")
    print("6. Reporte (valor total y stock bajo)")
    print("7. Salir")


# ----------------------------------------------------------------------------
# Una función por cada opción del menú
# ----------------------------------------------------------------------------
def registrar_producto(productos):
    codigo = pedir_entero("Código del producto: ", minimo=1)

    # Regla del negocio: no puede haber dos productos con el mismo código.
    if buscar(productos, codigo) is not None:
        print("Ya existe un producto con ese código.")
        return

    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    existencia = pedir_entero("Existencia inicial (0 o más): ", minimo=0)
    precio = pedir_precio("Precio (mayor a 0): ")

    productos.append({"codigo": codigo, "nombre": nombre, "existencia": existencia, "precio": precio})
    print("Producto registrado.")


def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    print(f"{'COD':>5}  {'PRODUCTO':<20} {'EXISTENCIA':>10} {'PRECIO':>10}")
    print("-" * 50)
    for p in sorted(productos, key=lambda p: p["codigo"]):
        print(f"{p['codigo']:>5}  {p['nombre']:<20} {p['existencia']:>10} {p['precio']:>10.2f}")


def consultar_producto(productos):
    codigo = pedir_entero("Código a buscar: ")
    producto = buscar(productos, codigo)

    if producto is None:
        print("No existe un producto con ese código.")
        return

    print("Producto:  ", producto["nombre"])
    print("Existencia:", producto["existencia"])
    print("Precio:    ", producto["precio"])


def mover_stock(productos, es_entrada):
    """Opciones 4 y 5: es_entrada indica si se suma o se resta."""
    codigo = pedir_entero("Código del producto: ")
    producto = buscar(productos, codigo)

    if producto is None:
        print("No existe un producto con ese código.")
        return

    print(f"Producto: {producto['nombre']} (existencia actual: {producto['existencia']})")
    unidades = pedir_entero("Unidades (mayor a 0): ", minimo=1)

    if es_entrada:
        producto["existencia"] += unidades
        print("Entrada registrada. Nueva existencia:", producto["existencia"])
    elif unidades > producto["existencia"]:
        # Regla del negocio: no se puede sacar más mercancía de la que hay.
        print("No hay suficientes unidades. Solo quedan", producto["existencia"])
    else:
        producto["existencia"] -= unidades
        print("Salida registrada. Nueva existencia:", producto["existencia"])


def valor_inventario(productos):
    return sum(p["existencia"] * p["precio"] for p in productos)


def reporte(productos):
    print("===== REPORTE =====")
    print("Productos registrados:", len(productos))
    print(f"Valor total del inventario: {valor_inventario(productos):.2f}")

    bajos = [p for p in productos if p["existencia"] < STOCK_BAJO]
    print(f"Productos con stock bajo (menos de {STOCK_BAJO} unidades):")
    if not bajos:
        print("  Ninguno.")
    for p in bajos:
        print(f"  - {p['nombre']} ({p['existencia']} unidades)")


# ----------------------------------------------------------------------------
# PROGRAMA PRINCIPAL: corto y legible, solo organiza el menú.
# ----------------------------------------------------------------------------
def main():
    productos = cargar()
    if productos:
        print(f"Se cargaron {len(productos)} productos de {ARCHIVO.name}.")

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        match opcion:
            case "1":
                registrar_producto(productos)
            case "2":
                listar_productos(productos)
            case "3":
                consultar_producto(productos)
            case "4":
                mover_stock(productos, es_entrada=True)
            case "5":
                mover_stock(productos, es_entrada=False)
            case "6":
                reporte(productos)
            case "7":
                guardar(productos)
                print(f"Inventario guardado en {ARCHIVO.name}. Hasta luego.")
                break
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
