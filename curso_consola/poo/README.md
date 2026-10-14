# Programación Orientada a Objetos (POO) avanzada — Python

Ejemplos prácticos de los pilares avanzados de la POO en Python, equivalentes a los de los cursos de PHP y C#. Antes de esta carpeta conviene ver `objetos/objeto.py` (clases, herencia y miembros estáticos).

## Archivos y conceptos

### 1. Clases abstractas (`clases_abstractas.py`)

- **Concepto:** plantillas estrictas que **no se pueden instanciar** directamente (`Animal("Test")` lanza `TypeError`).
- **Utilidad:** definen una estructura base que obliga a las clases hijas a implementar ciertos métodos (los marcados con `@abstractmethod`).
- **Diferencia con PHP y C#:** `abstract` no es una palabra del lenguaje; se arma con el módulo `abc`.
- **Ejemplo:** una clase `Animal` que obliga a `Perro` y `Gato` a implementar `hacer_sonido()`.

### 2. Interfaces (`interfaces.py`)

- **Concepto:** contratos que definen **qué** métodos debe tener una clase, pero no **cómo** funcionan.
- **Diferencia con PHP y C#:** Python no tiene la palabra `interface`. Se logra con clases abstractas sin implementación (herencia múltiple) o con `Protocol` (*duck typing*: si tiene los métodos, cumple el contrato).
- **Ejemplo:** un `Celular` que cumple `ReproducibleMultimedia` y `Grabable`; un `Avion` y un `Pajaro` que cumplen `Volador` sin declararlo.

### 3. "Traits" (`traits.py`)

- **Concepto:** Python no tiene Traits; el equivalente son los **mixins**, clases pequeñas que aportan una habilidad y se agregan a la lista de padres.
- **Diferencia clave:** al contrario que la solución de C# (interfaces con método por defecto), un mixin sí puede tener estado propio, igual que un Trait de PHP.
- **Ejemplo:** un mixin `UtilidadesLog` con un método `loguear()`, usado tanto por `Usuario` como por `Producto`.

### 4. Namespaces (`namespaces.py` y carpeta `proyecto/`)

- **Concepto:** espacios de nombres para evitar conflictos cuando dos clases tienen el **mismo nombre**.
- **Diferencia con PHP y C#:** no se declara nada. Cada archivo `.py` es un módulo y cada carpeta es un paquete; la ruta del archivo **es** el namespace.
- **Ejemplo:** una clase `Persona` en `proyecto/admin.py` y otra `Persona` en `proyecto/publico.py`, sin que choquen.

## Tabla de equivalencias

| Concepto | PHP | C# | Python |
|---|---|---|---|
| Clase abstracta | `abstract class` | `abstract class` | `class X(ABC)` + `@abstractmethod` |
| Interfaz | `interface` + `implements` | `interface` | `ABC` sin implementación, o `Protocol` |
| Reutilización horizontal | `trait` + `use` | interfaz con método por defecto | mixin (herencia múltiple) |
| Espacio de nombres | `namespace A\B;` | `namespace A.B;` | carpeta `a/` + archivo `b.py` |
| Importar | `use A\B\Clase;` | `using A.B;` | `from a.b import Clase` |

## Cómo ejecutarlos

```bash
cd curso_consola/poo
python clases_abstractas.py
python interfaces.py
python traits.py
python namespaces.py
```

`namespaces.py` importa el paquete `proyecto/` que está a su lado. Funciona desde cualquier carpeta, porque Python siempre busca los módulos primero en la carpeta del archivo que se está ejecutando.
