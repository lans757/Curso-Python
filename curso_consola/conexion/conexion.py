# ============================================================================
# CONEXIÓN A BASE DE DATOS EN PYTHON
# ============================================================================
# Equivale a: conexion/conexion.php + selec.php · Conexion.cs
# En PSeInt la "base de datos" se simulaba con arreglos paralelos.
#
# PHP usa PDO y C# usa ADO.NET: una interfaz común y un "driver" según el
# motor. Python tiene el mismo concepto, llamado DB-API: todos los drivers
# (SQLite, MySQL, PostgreSQL...) se usan con los mismos pasos:
#
#   1. conectar          conexion = driver.connect(...)
#   2. pedir un cursor   cursor = conexion.cursor()
#   3. ejecutar SQL      cursor.execute("SELECT ...", parametros)
#   4. leer resultados   cursor.fetchall()
#   5. confirmar/cerrar  conexion.commit()  /  conexion.close()
#
# Este ejemplo usa SQLite porque VIENE INCLUIDO en Python: no hay que
# instalar nada ni tener XAMPP encendido. La base de datos es un solo
# archivo (prueba.db) que se crea al lado de este script.
#
# Para usar el MySQL de XAMPP, como en los cursos de PHP y C#, ver el final.
# ============================================================================

import sqlite3
from pathlib import Path

carpeta = Path(__file__).parent
archivo_bd = carpeta / "prueba.db"
archivo_sql = carpeta / "prueba.sql"


def conectar():
    conexion = sqlite3.connect(archivo_bd)
    # Con row_factory = sqlite3.Row cada fila se puede leer por el nombre de
    # la columna (fila["nombre"]), como PDO::FETCH_ASSOC en PHP.
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla_si_no_existe(conexion):
    # Equivale a importar prueba.sql en phpMyAdmin.
    conexion.executescript(archivo_sql.read_text(encoding="utf-8"))
    conexion.commit()


def listar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    filas = cursor.fetchall()

    print("Lista de usuarios (base de datos)")
    if not filas:
        print("No hay usuarios registrados en la tabla aún.")
    for fila in filas:
        print(f"  [{fila['id']}] {fila['nombre']} <{fila['email']}>")


def buscar_por_nombre(conexion, nombre):
    # CONSULTA PARAMETRIZADA (prepared statement): el dato del usuario NUNCA
    # se pega dentro del texto del SQL. Se pone un signo ? y el valor se
    # envía aparte. Así se evita la inyección de SQL.
    #
    #   MAL:   "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"
    #   BIEN:  "SELECT * FROM usuarios WHERE nombre = ?", (nombre,)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE nombre = ?", (nombre,))
    return cursor.fetchone()          # una sola fila, o None si no hay


def insertar_usuario(conexion, nombre, email):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
    conexion.commit()                 # sin commit(), el cambio no se guarda
    return cursor.lastrowid


conexion = None
try:
    conexion = conectar()
    print("Estado: Conexión exitosa con sqlite3\n")

    crear_tabla_si_no_existe(conexion)
    listar_usuarios(conexion)

    print("\nBuscando al usuario 'luis' con una consulta parametrizada:")
    encontrado = buscar_por_nombre(conexion, "luis")
    if encontrado:
        print(f"  Encontrado: {encontrado['nombre']} <{encontrado['email']}>")

    print("\nIntento de inyección de SQL (no funciona gracias al parámetro):")
    ataque = "' OR '1'='1"
    print("  Resultado:", buscar_por_nombre(conexion, ataque))

    if buscar_por_nombre(conexion, "Ana") is None:
        nuevo_id = insertar_usuario(conexion, "Ana", "ana@ana.com")
        print(f"\nUsuario 'Ana' insertado con id {nuevo_id}.")
    else:
        print("\nEl usuario 'Ana' ya existía; no se inserta de nuevo.")

    print()
    listar_usuarios(conexion)
except sqlite3.Error as e:
    # Equivalente al catch (PDOException $e) de PHP.
    print("Error de base de datos:", e)
finally:
    if conexion is not None:
        conexion.close()
        print("\nConexión cerrada.")

# ----------------------------------------------------------------------------
# CON MySQL (XAMPP), como en los cursos de PHP y C#
#
#   pip install mysql-connector-python
#
#   import mysql.connector
#   conexion = mysql.connector.connect(
#       host="localhost", database="prueba", user="root", password=""
#   )
#   cursor = conexion.cursor(dictionary=True)
#   cursor.execute("SELECT id, nombre, email FROM usuarios WHERE nombre = %s", (nombre,))
#
# Los pasos son los mismos. Solo cambian dos detalles: la línea de conexión
# y el marcador de los parámetros (%s en MySQL, ? en SQLite).
# ----------------------------------------------------------------------------
