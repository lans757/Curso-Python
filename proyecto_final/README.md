# 📦 Proyecto final — Sistema de inventario

Es el mismo proyecto con el que cierra el curso de pseudocódigo (`08_proyecto_final`), que a su vez es la versión reducida del `warehouse-inventory-system` del curso de PHP. Aquí se resuelve en Python, y por eso sirve para ver **cuánto cambia la forma y qué poco cambia la lógica**.

## Requisitos del sistema

Un menú que se repite hasta que el usuario elige salir:

1. **Registrar un producto** (código, nombre, existencia inicial y precio).
2. **Listar todos los productos.**
3. **Buscar un producto por código.**
4. **Registrar una entrada** (llegó mercancía: suma a la existencia).
5. **Registrar una salida** (venta o consumo: resta, sin dejar negativos).
6. **Reporte:** valor total del inventario y productos con stock bajo (menos de 5 unidades).
7. **Salir.**

### Reglas del negocio

- No puede haber dos productos con el mismo código.
- La existencia no puede ser negativa; el precio debe ser mayor que cero.
- No se puede sacar más mercancía de la que hay.
- El programa **no debe romperse** si el usuario escribe letras donde va un número.

## Cómo se guardan los datos

En PSeInt hacían falta cuatro arreglos paralelos y una variable `cantidad`. En Python, una **lista de diccionarios**:

```python
productos = [
    {"codigo": 101, "nombre": "Arroz",  "existencia": 40, "precio": 2.5},
    {"codigo": 102, "nombre": "Harina", "existencia": 25, "precio": 1.8},
]
```

| En PSeInt | En Python |
|-----------|-----------|
| `codigos[i]`, `nombres[i]`, `existencias[i]`, `precios[i]` | `productos[i]["codigo"]`, `productos[i]["nombre"]`... |
| variable `cantidad` | `len(productos)` |
| límite fijo de 50 (`Dimension`) | sin límite: `productos.append(...)` |
| `buscar_posicion()` devuelve `0` si no existe | `buscar()` devuelve `None` si no existe |
| `cantidad Por Referencia` | no hace falta: la lista se modifica directamente |
| los datos se pierden al cerrar | se guardan en `inventario.json` |

## Plan de trabajo por etapas

No se escribe todo de una vez. Se construye y se **prueba cada etapa** antes de seguir. Empieza por `esqueleto_menu.py`, que ya ejecuta.

| Etapa | Qué se logra | Se prueba con |
|-------|--------------|---------------|
| 1 | Menú que se repite y sale con la opción 7 (ya está en el esqueleto) | Opciones válidas e inválidas |
| 2 | Registrar y listar | Registrar 3 productos y listarlos |
| 3 | Buscar por código y rechazar códigos repetidos | Intentar repetir un código |
| 4 | Entradas y salidas con validación | Sacar más de lo que hay |
| 5 | Reporte de valor total y stock bajo | Calcular el valor a mano y comparar |
| 6 | Que no se rompa con datos incorrectos (`try` / `except`) | Escribir `abc` como precio |
| 7 | Guardar en un archivo al salir y cargarlo al entrar | Cerrar, volver a abrir y listar |

## Mejoras opcionales

- **Eliminar** un producto.
- **Buscar por nombre**, aunque se escriba solo una parte.
- **Ordenar** el listado por nombre, precio o existencia (`sorted` con `key`).
- **Aumentar** todos los precios en un porcentaje.
- Convertir el producto en una **clase** o en una `@dataclass` (ver `objetos/clases_de_datos.py`).
- Guardar los datos en **SQLite** en vez de JSON (ver `conexion/conexion.py`).
- Hacer una **versión web** con Flask (ver `curso_web/app.py`).

## Archivos

| Archivo | Para qué |
|---------|----------|
| `esqueleto_menu.py` | Punto de partida: el menú funcionando, con las opciones por hacer |
| `inventario_bodega.py` | Solución de referencia con las 7 opciones y el guardado en archivo |

Conviene no abrir la solución hasta haber intentado una versión propia; después sirve para comparar enfoques.

```bash
cd proyecto_final
python esqueleto_menu.py
python inventario_bodega.py
```
