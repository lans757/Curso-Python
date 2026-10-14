# ============================================================================
# NAMESPACES (ESPACIOS DE NOMBRES) EN PYTHON: MÓDULOS Y PAQUETES
# ============================================================================
# Equivale a: poo/namespaces.php · Namespaces.cs
#
# Resuelven un problema: tener dos clases con el MISMO nombre sin que
# choquen. Son como "apellidos" o "carpetas" para tu código.
#
# En PHP y C# hay que escribir la palabra "namespace". En Python NO hace
# falta escribir nada, porque el namespace lo da el propio archivo:
#
#   - Cada archivo .py es un MÓDULO, y su nombre ya es un namespace.
#   - Cada carpeta con archivos .py es un PAQUETE.
#
# Junto a este archivo hay una carpeta "proyecto/" con dos módulos:
#
#   proyecto/
#   ├── admin.py      -> class Persona  (el administrador)
#   └── publico.py    -> class Persona  (un visitante)
#
#   PHP:     new \Proyecto\Admin\Persona()
#   C#:      new Proyecto.Admin.Persona()
#   Python:  proyecto.admin.Persona()
# ============================================================================

# Forma 1: importar los módulos y usar la ruta completa
import proyecto.admin
import proyecto.publico

print("Ejemplo de namespaces")
print("Tenemos dos clases llamadas 'Persona', pero no chocan:\n")

admin = proyecto.admin.Persona()
print("Admin:", admin.saludar())

usuario = proyecto.publico.Persona()
print("Público:", usuario.saludar())

# ----------------------------------------------------------------------------
# Forma 2: importar la clase con un alias (el "use ... as ..." de PHP y el
# "using Alias = ..." de C#)
# ----------------------------------------------------------------------------
from proyecto.admin import Persona as PersonaAdmin
from proyecto.publico import Persona as PersonaPublica

print("\nCon alias:")
print("Admin:", PersonaAdmin().saludar())
print("Público:", PersonaPublica().saludar())

# ----------------------------------------------------------------------------
# Forma 3: importar el módulo con un nombre corto
# ----------------------------------------------------------------------------
import proyecto.admin as adm

print("\nCon nombre corto de módulo:", adm.Persona().saludar())

# ----------------------------------------------------------------------------
# __name__: cada módulo sabe cómo se llama
# ----------------------------------------------------------------------------
print("\nEste archivo se llama:", __name__)             # "__main__" si se ejecuta directo
print("El módulo de admin se llama:", proyecto.admin.__name__)

# ----------------------------------------------------------------------------
# Evita esto:  from proyecto.admin import *
# Trae TODOS los nombres del módulo sin decir cuáles, y vuelve a provocar
# justo el choque de nombres que los namespaces venían a resolver.
# ----------------------------------------------------------------------------
