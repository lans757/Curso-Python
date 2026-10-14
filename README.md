# 🐍 Curso de Python: Fundamentos y lógica

Equivalente en Python de los otros cuatro cursos de la serie. Reúne lo que cada uno aporta:

| Curso | Qué toma de él este curso |
|---|---|
| [Curso Básico de PHP](../Curso-Basico-PHP) | El **temario**: los mismos temas, en el mismo orden y con los mismos ejemplos (meses, frutas, `Persona`, `Animal`, inventario) |
| [Curso Básico de JS](../Curso-Basico-JS) | La forma de trabajo: **un archivo por tema** que se ejecuta suelto desde la terminal |
| [Curso de C#](../curso%20c%23) | La separación **consola / web**, el menú de ejercicios y la sección de **temas propios del lenguaje** |
| [Curso de PSeInt](../curso-pseint/curso-pseint) | La **práctica**: ejercicios por niveles, "predice y corrige", soluciones ejecutables y el proyecto final por etapas |

Mantiene el enfoque de todos: aprender la **lógica**, con comentarios que explican el *por qué* y no solo el *qué*. Cada archivo indica al inicio a qué archivo de los otros cursos equivale y en qué se diferencia Python.

## Estructura

```
Curso-Basico-Python/
├── curso_consola/     → 45 ejercicios de lógica pura, con un menú (menu.py)
├── curso_web/         → formularios, cookies, sesiones y subida de archivos (Flask)
├── practica/          → ejercicios por niveles, "predice y corrige" y soluciones
├── proyecto_final/    → sistema de inventario por etapas
├── recursos/          → tabla de equivalencias entre los cinco lenguajes
├── README.md          → este archivo
├── TUTORIAL.md        → cómo instalar, ejecutar y qué problemas esperar
└── start.sh           → script de arranque
```

### `curso_consola/` — todo lo que no depende de una petición HTTP

A diferencia de C#, en Python cada archivo se puede ejecutar por separado, como en PHP y JS. El menú es solo una comodidad.

```bash
cd curso_consola
python menu.py                      # menú interactivo
python menu.py 17                   # ejecuta directo el ejercicio 17
python fundamentos/variables.py     # o cualquier archivo, sin el menú
```

Temas (carpeta → equivalente en los otros cursos):

- `hola_mundo`, `print_r`, `var_dump`, `die` — depuración (`print`, `pprint`, `type`, `sys.exit`)
- `fundamentos/` — variables, operadores, constantes, y **entrada y salida** (`input`/`print`, el `Leer`/`Escribir` de PSeInt)
- `condicionales/` — `if`/`elif`/`else`, ternario y valores por defecto, `match` (el `switch`)
- `ciclos/` — `for` con `range`, `while`, equivalente a `do-while`, `for` sobre colecciones (el `foreach`), `break`/`continue`
- `arreglos/` — listas, diccionarios, tuplas y matrices; contar, ordenar y recorrer
- `funciones/` — funciones, métodos de texto, métodos de listas y diccionarios, scope
- `funciones_matematicas/` — `math` y `random`
- `objetos/` — clases, herencia, miembros estáticos, propiedades y `@dataclass`
- `poo/` — clases abstractas, interfaces (`ABC` y `Protocol`), "traits" (mixins), namespaces (módulos y paquetes)
- `errores/` — `try`/`except`/`finally`, excepciones personalizadas
- `archivos/` — crear, escribir y leer archivos de texto
- `seguridad/` — hashing de contraseñas (PBKDF2, incluido en Python), sanitización XSS
- `conexion/` — base de datos con SQLite (incluido en Python; al final se explica la variante con el MySQL de XAMPP)
- `include_import/` — `import`, el equivalente de `include`/`require`

Temas **propios de Python**, sin equivalente directo en PHP:

- `comprensiones/` — comprensiones de listas y diccionarios, expresiones generadoras, `any`/`all` (lo que en C# es LINQ y en JS `filter`/`map`)
- `asincronia/` — `async`/`await`, ejecución secuencial frente a concurrente con `asyncio.gather`
- `tipado/` — anotaciones de tipo, valores opcionales (`str | None`) y genéricos (los temas `genericos/` y `nullable/` del curso de C#)
- `decoradores/` — decoradores propios, `functools.cache` y administradores de contexto (`with`)

### `curso_web/` — lo que solo tiene sentido dentro de una petición HTTP

Una aplicación Flask, equivalente al `CursoWeb` de C# y a los temas web del curso de PHP.

```bash
cd curso_web
pip install -r requirements.txt     # solo la primera vez
python app.py
# abre http://localhost:4050
```

Rutas:

- `/formularios` — equivalente a `formulario.php` + `formulario.view.php` + `recibir.php`
- `/cookies`, `/cookies/texto`, `/cookies/borrar` — equivalente a `cookies/index.php` + `texto.php`
- `/sesiones`, `/sesiones/pagina2`, `/sesiones/cerrar` — equivalente a `sesiones/*.php`
- `/archivos/subir` — equivalente a `archivos/subir_archivo.php`
- `/seguridad` — demostración de XSS: el mismo comentario escapado y sin escapar

### `practica/` — escribir, no solo leer

- `ejercicios.md` — 30 ejercicios en tres niveles (⭐ ⭐⭐ ⭐⭐⭐) sobre fundamentos, condicionales, ciclos, arreglos y funciones
- `predice_y_corrige.md` — 8 fragmentos para predecir la salida y 6 con un error por encontrar; casi todos son trampas típicas al venir de otro lenguaje
- `soluciones/` — una solución ejecutable por tema: `python ciclos.py 6`

### `proyecto_final/` — sistema de inventario

El mismo proyecto que cierra el curso de PSeInt, ahora con lista de diccionarios, validación con `try`/`except` y guardado en un archivo JSON. Incluye un esqueleto para empezar y la solución de referencia. Ver [proyecto_final/README.md](proyecto_final/README.md).

## Diferencias clave con los otros lenguajes (resumen)

| En los otros cursos | En Python | Nota |
|---|---|---|
| Llaves `{ }` o `FinSi`, `FinPara` | **Sangría** y dos puntos `:` | La sangría deja de ser estética: define los bloques |
| `;` al final de cada instrucción | Nada | Una instrucción por línea |
| `$variable` (PHP), `let` (JS), tipo fijo (C#, PSeInt) | `variable = valor` | No se declara; el tipo lo tiene el valor |
| `10 == "10"` es verdadero (PHP, JS) | Es `False` | Tipado fuerte: no convierte por su cuenta |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` | Con palabras, como `Y`, `O`, `NO` de PSeInt |
| `for (i = 0; i < n; i++)` | `for i in range(n)` | `range` nunca incluye el último número |
| `do { } while (c)` y `Repetir … Hasta Que` | `while True:` + `break` | Python no tiene `do-while` |
| `switch` con `break` | `match` / `case` | Sin `break`; el `default` es `case _` |
| Arreglos desde 1 (PSeInt) | Listas desde 0 | Y `lista[-1]` es el último |
| Array asociativo (PHP), objeto (JS) | Diccionario `{ }` | Listas y diccionarios son tipos distintos |
| `new Persona()`, `$this` / `this` | `Persona()`, `self` | `self` se escribe como primer parámetro |
| `public` / `private` | Convención del guion bajo | `_saldo` significa "no tocar desde afuera" |
| `interface`, `trait` | `ABC`, `Protocol`, mixins | Se resuelve con herencia múltiple |
| `include` / `require` / `using` | `import` | Cada archivo `.py` ya es un módulo |
| `$_POST`, `$_SESSION`, `$_COOKIE` | `request.form`, `session`, `request.cookies` | Viven en Flask, no en el lenguaje |

La tabla completa, concepto por concepto y en los cinco lenguajes, está en [recursos/equivalencias.md](recursos/equivalencias.md).

## Orden sugerido

1. `hola_mundo.py` y `fundamentos/` → práctica 1
2. `condicionales/` → práctica 2
3. `ciclos/` → práctica 3
4. `arreglos/` y `funciones/` → prácticas 4 y 5, y `practica/predice_y_corrige.md`
5. `proyecto_final/` (etapas 1 a 5)
6. `errores/` y `archivos/` → `proyecto_final/` (etapas 6 y 7)
7. `objetos/` y `poo/`
8. `seguridad/`, `conexion/`, `include_import/` y `curso_web/`
9. Temas propios de Python: `comprensiones/`, `tipado/`, `decoradores/`, `asincronia/`

Quien viene del curso de PSeInt puede seguir este orden tal cual. Quien ya domina PHP, JS o C# puede ir directo a la tabla de equivalencias y a los puntos 7 a 9.

## Requisitos

- Python 3.12 o superior (`python --version`). El curso se probó con Python 3.14.
- Para `curso_web/`: Flask (`pip install -r curso_web/requirements.txt`).
- Todo lo demás, incluida la base de datos, funciona solo con Python: no hace falta XAMPP ni ningún servidor.

Los detalles de instalación y los problemas frecuentes están en [TUTORIAL.md](TUTORIAL.md).
