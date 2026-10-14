# ============================================================================
# PROYECTO FINAL — ETAPA 1: un menú que se repite hasta elegir "Salir"
# ============================================================================
# Punto de partida para construir el sistema de inventario. Ya se ejecuta:
# muestra el menú, valida la opción y sale con la 7. Tu trabajo es reemplazar
# cada mensaje "(Aquí irá: ...)" por una función que haga lo que dice.
#
# Viene de: 08_proyecto_final/ejemplos/esqueleto_menu.psc (curso de PSeInt)
# ============================================================================


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


def main():
    # El inventario: una lista de diccionarios. Cada diccionario es un producto:
    #   {"codigo": 101, "nombre": "Arroz", "existencia": 40, "precio": 2.5}
    # En PSeInt esto eran cuatro arreglos paralelos.
    productos = []

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        match opcion:
            case "1":
                print("(Aquí irá: registrar producto)")
            case "2":
                print("(Aquí irá: listar productos)")
            case "3":
                print("(Aquí irá: buscar producto)")
            case "4":
                print("(Aquí irá: registrar entrada)")
            case "5":
                print("(Aquí irá: registrar salida)")
            case "6":
                print("(Aquí irá: reporte)")
            case "7":
                print("Hasta luego")
                break
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
