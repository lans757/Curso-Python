# ============================================================================
# CURSO DE PYTHON — MENÚ PRINCIPAL
# ============================================================================
# En PHP y JS cada ejercicio es un archivo que se abre por separado. En C#
# hizo falta un menú (Program.cs) porque un proyecto compila a un solo
# ejecutable. En Python los archivos SÍ se pueden ejecutar uno por uno:
#
#     python fundamentos/variables.py
#
# Este menú es solo una comodidad para recorrerlos sin escribir las rutas.
#
# Uso:  python menu.py            -> muestra el menú interactivo
#       python menu.py 17         -> ejecuta directo el ejercicio número 17
#       python menu.py --lista    -> solo muestra la lista y termina
# ============================================================================

import subprocess
import sys
from pathlib import Path

CARPETA = Path(__file__).parent

# (sección, título, archivo)
EJERCICIOS = [
    ("Depuración", "Hola Mundo", "hola_mundo.py"),
    ("Depuración", "print_r (equivalente)", "print_r.py"),
    ("Depuración", "var_dump (equivalente)", "var_dump.py"),
    ("Depuración", "die (equivalente)", "die.py"),

    ("Fundamentos", "Variables", "fundamentos/variables.py"),
    ("Fundamentos", "Operadores", "fundamentos/operadores.py"),
    ("Fundamentos", "Constantes", "fundamentos/constantes.py"),
    ("Fundamentos", "Entrada y salida (interactivo)", "fundamentos/entrada_salida.py"),

    ("Condicionales", "if / elif / else", "condicionales/condicionales.py"),
    ("Condicionales", "Ternario y valores por defecto", "condicionales/shorthand.py"),
    ("Condicionales", "match (switch)", "condicionales/switch.py"),

    ("Ciclos", "Índice", "ciclos/ciclos.py"),
    ("Ciclos", "for con range", "ciclos/ciclo_for.py"),
    ("Ciclos", "while", "ciclos/ciclo_while.py"),
    ("Ciclos", "Equivalente a do-while", "ciclos/ciclo_do_while.py"),
    ("Ciclos", "for sobre colecciones (foreach)", "ciclos/ciclo_foreach.py"),
    ("Ciclos", "break / continue", "ciclos/break_continue.py"),

    ("Arreglos", "Listas, diccionarios y tuplas", "arreglos/arrays.py"),
    ("Arreglos", "Contar elementos", "arreglos/contar_elementos_arreglos.py"),
    ("Arreglos", "Ordenar", "arreglos/ordenar_arreglos.py"),
    ("Arreglos", "Recorrer (for directo)", "arreglos/recorrer_arreglo.py"),
    ("Arreglos", "Recorriendo por índice (for/while)", "arreglos/recorriendo_arreglos.py"),

    ("Funciones", "Funciones", "funciones/funciones.py"),
    ("Funciones", "Métodos de texto", "funciones/funciones_texto.py"),
    ("Funciones", "Métodos de listas y diccionarios", "funciones/funciones_arreglos.py"),
    ("Funciones", "Scope (ámbito)", "funciones/scope.py"),
    ("Funciones", "Funciones matemáticas", "funciones_matematicas/matematicas.py"),

    ("Objetos y POO", "Clases, herencia y estáticos", "objetos/objeto.py"),
    ("Objetos y POO", "Clases de datos (@dataclass)", "objetos/clases_de_datos.py"),
    ("Objetos y POO", "Clases abstractas", "poo/clases_abstractas.py"),
    ("Objetos y POO", "Interfaces", "poo/interfaces.py"),
    ("Objetos y POO", "Traits (mixins)", "poo/traits.py"),
    ("Objetos y POO", "Namespaces (módulos y paquetes)", "poo/namespaces.py"),

    ("Errores", "try / except / finally", "errores/try_except.py"),
    ("Errores", "Excepciones personalizadas", "errores/excepciones_personalizadas.py"),

    ("Archivos", "Crear y escribir", "archivos/crear_escribir.py"),
    ("Archivos", "Leer", "archivos/leer_archivo.py"),

    ("Seguridad", "Hashing de contraseñas", "seguridad/password_hashing.py"),
    ("Seguridad", "Sanitización XSS", "seguridad/sanitizacion_xss.py"),

    ("Datos y módulos", "Conexión a base de datos (SQLite)", "conexion/conexion.py"),
    ("Datos y módulos", "include / require (import)", "include_import/index.py"),

    ("Propio de Python", "Comprensiones y generadores", "comprensiones/comprensiones.py"),
    ("Propio de Python", "async / await", "asincronia/async_await.py"),
    ("Propio de Python", "Anotaciones de tipo y genéricos", "tipado/type_hints.py"),
    ("Propio de Python", "Decoradores y with", "decoradores/decoradores.py"),
]


def mostrar_menu():
    print()
    print("=" * 60)
    print("  CURSO DE PYTHON — Fundamentos y lógica")
    print("=" * 60)
    seccion_actual = None
    for numero, (seccion, titulo, _) in enumerate(EJERCICIOS, start=1):
        if seccion != seccion_actual:
            print(f"\n  {seccion}")
            seccion_actual = seccion
        print(f"    {numero:>2}. {titulo}")
    print("\n     0. Salir")


def ejecutar(numero):
    seccion, titulo, archivo = EJERCICIOS[numero - 1]
    ruta = CARPETA / archivo
    print()
    print("-" * 60)
    print(f"  {numero}. {seccion} > {titulo}")
    print(f"  Archivo: {archivo}")
    print("-" * 60)
    # Cada ejercicio se ejecuta como un programa aparte, con el mismo Python
    # que está corriendo este menú. Así, si un ejercicio termina con
    # sys.exit() (como die.py) o con un error, el menú sigue funcionando.
    sys.stdout.flush()          # que el encabezado salga antes que el ejercicio
    subprocess.run([sys.executable, str(ruta)])
    print("-" * 60)


def pedir_numero():
    while True:
        respuesta = input("\nNúmero del ejercicio (0 para salir, Enter para ver el menú): ").strip()
        if respuesta == "":
            return None
        if respuesta.isdigit() and 0 <= int(respuesta) <= len(EJERCICIOS):
            return int(respuesta)
        print(f"Escribe un número entre 0 y {len(EJERCICIOS)}.")


def main():
    # Atajos por línea de comandos
    if len(sys.argv) > 1:
        argumento = sys.argv[1]
        if argumento == "--lista":
            mostrar_menu()
            return
        if argumento.isdigit() and 1 <= int(argumento) <= len(EJERCICIOS):
            ejecutar(int(argumento))
            return
        sys.exit(f"Argumento no válido. Usa un número entre 1 y {len(EJERCICIOS)}, o --lista.")

    mostrar_menu()
    while True:
        numero = pedir_numero()
        if numero is None:
            mostrar_menu()
        elif numero == 0:
            print("¡Hasta luego!")
            break
        else:
            ejecutar(numero)


if __name__ == "__main__":
    main()
