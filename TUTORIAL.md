# Curso de Python — Guía de uso y cosas a tener en cuenta

Este archivo reúne lo que hace falta para ejecutar el curso y los problemas que es normal encontrarse, para no redescubrirlos desde cero.

---

## 1. Requisitos antes de empezar

| Requisito | Para qué | Cómo verificar |
|---|---|---|
| Python 3.12 o superior | Todo el curso | `python --version` (ver la sección 4 si no se reconoce el comando) |
| Flask | Solo para `curso_web/` | `python -c "import flask"` (si no da error, está instalado) |
| Un editor | Leer y modificar los archivos | VS Code con la extensión *Python* de Microsoft |

Todo lo demás (POO, archivos, base de datos, seguridad, asincronía) **no necesita nada externo**: usa la biblioteca estándar de Python. La base de datos es SQLite, que viene incluida, así que no hace falta tener XAMPP encendido.

**¿Por qué 3.12?** El curso usa `match` (existe desde la 3.10) y la sintaxis `class Caja[T]` de `tipado/type_hints.py` (desde la 3.12). Con una versión anterior, ese archivo da `SyntaxError`; el resto funciona desde la 3.10.

---

## 2. Estructura del proyecto

```
Curso-Basico-Python/
├── curso_consola/     → 45 ejercicios de lógica pura, con un menú (menu.py)
├── curso_web/         → formularios, cookies, sesiones, subida de archivos (Flask)
├── practica/          → ejercicios por niveles y sus soluciones
├── proyecto_final/    → sistema de inventario
├── recursos/          → equivalencias PSeInt ↔ PHP ↔ JS ↔ C# ↔ Python
├── README.md          → detalle de cada tema y su equivalente en los otros cursos
├── TUTORIAL.md        → este archivo
└── start.sh           → script de arranque (deja elegir qué iniciar)
```

---

## 3. Cómo ejecutarlo — paso a paso

### Opción A: con `start.sh` (lo más simple)

Abre una terminal Git Bash en la carpeta del proyecto:

```bash
cd "Documentos/Proyectos/Curso-Basico-Python"
bash start.sh
```

Pregunta si quieres iniciar `1` (consola), `2` (web) o `3` (proyecto final).

### Opción B: a mano

**Consola** (el menú de 45 ejercicios):

```bash
cd "Documentos/Proyectos/Curso-Basico-Python/curso_consola"
python menu.py
```

Se muestra el menú numerado: escribes el número del ejercicio y Enter. `0` para salir.

Atajos:

```bash
python menu.py 17          # ejecuta directo el ejercicio 17
python menu.py --lista     # solo muestra la lista
python ciclos/ciclo_for.py # ejecuta un archivo sin pasar por el menú
```

**Web** (formularios, cookies, sesiones, subida de archivos):

```bash
cd "Documentos/Proyectos/Curso-Basico-Python/curso_web"
pip install -r requirements.txt     # solo la primera vez
python app.py
```

Abre el navegador en **http://localhost:4050**. `Ctrl + C` en la terminal para detenerlo.

**Práctica y proyecto final:**

```bash
cd practica/soluciones
python ciclos.py 6

cd ../../proyecto_final
python inventario_bodega.py
```

### Opción C: desde VS Code

Abre la carpeta `Curso-Basico-Python`, abre cualquier archivo `.py` y pulsa el botón ▶ (*Run Python File*) arriba a la derecha. La salida aparece en el panel de terminal.

---

## 4. Si `python` no se reconoce como comando

En Windows hay tres nombres posibles. Prueba en este orden:

```bash
python --version
py --version
python3 --version
```

- Si funciona `py` pero no `python`, usa `py` en todos los comandos de este tutorial (`py menu.py`).
- Si al escribir `python` se abre la **Microsoft Store**, es un alias de Windows y no un Python real. Instala Python desde <https://www.python.org/downloads/> y, en el instalador, marca la casilla **"Add python.exe to PATH"**.
- Después de instalar, **cierra y vuelve a abrir** la terminal para que tome el PATH nuevo.

---

## 5. Entornos virtuales (recomendado para `curso_web/`)

Instalar paquetes con `pip install` los pone en el Python de todo el sistema. Lo habitual es darle a cada proyecto su propio "entorno virtual": una carpeta con su copia de Python y sus paquetes. Es el equivalente de `node_modules/` en JS y de `vendor/` en PHP.

```bash
cd curso_web
python -m venv .venv                 # crea el entorno (una sola vez)
source .venv/Scripts/activate        # lo activa (Git Bash en Windows)
pip install -r requirements.txt
python app.py
```

En PowerShell se activa con `.venv\Scripts\Activate.ps1`; en Linux y macOS, con `source .venv/bin/activate`. Cuando está activo, el nombre `(.venv)` aparece al inicio de la línea de la terminal. Se desactiva con `deactivate`.

La carpeta `.venv/` no se sube al repositorio (ya está en `.gitignore`).

---

## 6. Problemas frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `IndentationError` | Sangría incorrecta o mezcla de tabuladores y espacios | Usar siempre 4 espacios. En VS Code: *Convert Indentation to Spaces* |
| `SyntaxError: expected ':'` | Faltan los dos puntos al final de `if`, `for`, `while`, `def` o `class` | Agregarlos |
| `TypeError: can only concatenate str (not "int") to str` | Se intentó sumar un texto con un número | Convertir: `int(texto)` o usar una f-string |
| `NameError: name 'x' is not defined` | La variable no existe (error de tipeo, o se usó antes de asignarla) | Revisar el nombre; mayúsculas y minúsculas cuentan |
| `IndexError: list index out of range` | Posición que no existe; las listas empiezan en 0 | El último índice es `len(lista) - 1`, o `lista[-1]` |
| `KeyError: 'clave'` | Clave que no existe en el diccionario | Usar `diccionario.get("clave", valor_por_defecto)` |
| `ModuleNotFoundError: No module named 'flask'` | Flask no está instalado (o el entorno virtual no está activo) | `pip install -r requirements.txt` |
| `ModuleNotFoundError` al importar un archivo propio | Hay que importar el nombre **sin** `.py`, y el archivo debe estar en la misma carpeta | `import header`, no `import header.py` |
| Un `import` trae un módulo equivocado | Un archivo propio se llama igual que uno de Python (`random.py`, `math.py`, `html.py`) | Renombrar el archivo propio |
| Las tildes se ven mal en un archivo creado | Se abrió sin `encoding="utf-8"` | Escribir siempre `open(ruta, "w", encoding="utf-8")` |
| `UnicodeEncodeError` al imprimir | La terminal no usa UTF-8 (pasa al redirigir la salida a un archivo en Windows) | Ejecutar con `python -X utf8 archivo.py` |
| El programa no termina | Ciclo infinito | `Ctrl + C` en la terminal |
| `Address already in use` al iniciar la web | El puerto 4050 está ocupado | Cambiar el número en la última línea de `app.py` |
| `notas.txt` no aparece donde esperabas | Se crea junto al archivo `.py`, en `curso_consola/archivos/` | Buscarlo ahí |

### Tres hábitos que evitan casi todos los errores

1. **Lee la última línea del error.** Python muestra un rastro largo (*traceback*); lo importante está al final: el tipo de error y el mensaje. La línea de código está justo encima.
2. **Imprime lo que crees que vale.** `print(f"{variable=}")` muestra el nombre y el valor. Es el `var_dump` de Python.
3. **Predice antes de ejecutar.** Igual que en el curso de PSeInt: anota qué crees que saldrá y compáralo.

---

## 7. Archivos que generan los ejercicios

Al ejecutarse, algunos ejercicios crean archivos. Se pueden borrar sin problema; se vuelven a crear solos.

| Archivo | Lo crea |
|---|---|
| `curso_consola/archivos/notas.txt` y `resumen.txt` | `archivos/crear_escribir.py` |
| `curso_consola/conexion/prueba.db` | `conexion/conexion.py` |
| `curso_web/uploads/` | La ruta `/archivos/subir` |
| `proyecto_final/inventario.json` | `inventario_bodega.py`, al salir con la opción 7 |
| carpetas `__pycache__/` | Python, al importar módulos |

Todos están en `.gitignore`.

---

## 8. Base de datos: SQLite aquí, MySQL en los otros cursos

Los cursos de PHP y C# se conectan al MySQL de XAMPP, y había que importar `prueba.sql` desde phpMyAdmin. Aquí `conexion/conexion.py` usa **SQLite**, que viene dentro de Python:

- No hay nada que instalar ni que encender.
- La base de datos es un solo archivo, `prueba.db`, que el propio script crea.
- `prueba.sql` es la misma tabla `usuarios`, adaptada a SQLite; el script la ejecuta solo.

Para conectarse al MySQL de XAMPP con la misma base de los otros cursos, el final de `conexion.py` trae el código: se instala `mysql-connector-python`, se cambia la línea de conexión y los `?` de las consultas pasan a ser `%s`. Los pasos (conectar, cursor, ejecutar, leer) son los mismos.

---

## 9. Dashboard de proyectos

El módulo web usa el puerto **4050**, que estaba libre en `dashboard/projects.json` (el curso de C# usa el 4040). Este curso **no** se registró en el dashboard; si se quiere agregar, la tarjeta apuntaría a `Curso-Basico-Python\curso_web` con el comando `python app.py`. El menú de consola no tiene sentido ahí, porque es interactivo.
