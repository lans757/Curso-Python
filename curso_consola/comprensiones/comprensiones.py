# ============================================================================
# COMPRENSIONES Y GENERADORES — EL "LINQ" DE PYTHON
# ============================================================================
# Idiomático de Python. Lo más parecido en los otros cursos:
#   C#:   LINQ             lista.Where(...).Select(...)
#   JS:   métodos de Array lista.filter(...).map(...)
#   PHP:  array_filter() / array_map() / array_reduce()
#   PSeInt: un ciclo Para con un Si adentro y un arreglo nuevo
#
# Una comprensión construye una lista NUEVA a partir de otra, en una sola
# línea, diciendo QUÉ quieres y no CÓMO recorrer:
#
#   [ expresion   for elemento in coleccion   if condicion ]
#     ^ qué guardo    ^ de dónde lo saco         ^ cuáles (opcional)
#
# Se lee casi como una frase: "el doble de n, para cada n en numeros, si n es par".
# ============================================================================

productos = [
    {"nombre": "Arroz", "precio": 2.5, "stock": 40, "categoria": "Viveres"},
    {"nombre": "Harina", "precio": 1.8, "stock": 3, "categoria": "Viveres"},
    {"nombre": "Aceite", "precio": 4.2, "stock": 8, "categoria": "Viveres"},
    {"nombre": "Jabon", "precio": 1.2, "stock": 0, "categoria": "Limpieza"},
    {"nombre": "Cloro", "precio": 2.0, "stock": 12, "categoria": "Limpieza"},
]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ----------------------------------------------------------------------------
# 0. El punto de partida: lo mismo con un ciclo normal
# ----------------------------------------------------------------------------
pares_con_ciclo = []
for n in numeros:
    if n % 2 == 0:
        pares_con_ciclo.append(n)
print("Con ciclo:       ", pares_con_ciclo)

# ----------------------------------------------------------------------------
# 1. Filtrar — Where() en LINQ, filter() en JS, array_filter() en PHP
# ----------------------------------------------------------------------------
pares = [n for n in numeros if n % 2 == 0]
print("Con comprensión: ", pares)

con_stock_bajo = [p["nombre"] for p in productos if p["stock"] < 5]
print("\n1. Productos con stock bajo:", con_stock_bajo)

# ----------------------------------------------------------------------------
# 2. Transformar — Select() en LINQ, map() en JS, array_map() en PHP
# ----------------------------------------------------------------------------
cuadrados = [n ** 2 for n in numeros]
print("\n2. Cuadrados:", cuadrados)

nombres_en_mayusculas = [p["nombre"].upper() for p in productos]
print("   Nombres en mayúsculas:", nombres_en_mayusculas)

# ----------------------------------------------------------------------------
# 3. Filtrar y transformar a la vez
# ----------------------------------------------------------------------------
precios_con_iva = [round(p["precio"] * 1.16, 2) for p in productos if p["stock"] > 0]
print("\n3. Precio con IVA de lo que hay en existencia:", precios_con_iva)

# ----------------------------------------------------------------------------
# 4. Ordenar — OrderBy() en LINQ
# ----------------------------------------------------------------------------
por_precio = sorted(productos, key=lambda p: p["precio"], reverse=True)
print("\n4. Del más caro al más barato:", [p["nombre"] for p in por_precio])

# ----------------------------------------------------------------------------
# 5. Agregaciones — Sum(), Average(), Count(), Max() en LINQ
# Dentro de sum(), max()... la comprensión va SIN corchetes: eso es una
# "expresión generadora", que no crea la lista intermedia en memoria.
# ----------------------------------------------------------------------------
valor_inventario = sum(p["precio"] * p["stock"] for p in productos)
cantidad_agotados = sum(1 for p in productos if p["stock"] == 0)
mas_caro = max(productos, key=lambda p: p["precio"])
promedio = sum(p["precio"] for p in productos) / len(productos)

print("\n5. Valor total del inventario:", valor_inventario)
print("   Productos agotados:", cantidad_agotados)
print("   El más caro:", mas_caro["nombre"])
print("   Precio promedio:", round(promedio, 2))

# ----------------------------------------------------------------------------
# 6. any() y all() — Any() y All() en LINQ; some() y every() en JS
# ----------------------------------------------------------------------------
print("\n6. ¿Hay algún producto agotado?", any(p["stock"] == 0 for p in productos))
print("   ¿Todos cuestan menos de 5?", all(p["precio"] < 5 for p in productos))

# ----------------------------------------------------------------------------
# 7. Buscar el primero — FirstOrDefault() en LINQ, find() en JS
# next() toma el primer elemento que cumpla; el segundo argumento es lo que
# devuelve si no hay ninguno.
# ----------------------------------------------------------------------------
primero_de_limpieza = next((p for p in productos if p["categoria"] == "Limpieza"), None)
no_existe = next((p for p in productos if p["categoria"] == "Juguetes"), None)
print("\n7. Primer producto de limpieza:", primero_de_limpieza["nombre"])
print("   Primer juguete:", no_existe)

# ----------------------------------------------------------------------------
# 8. Comprensión de diccionario: { clave: valor for ... }
# ----------------------------------------------------------------------------
precios = {p["nombre"]: p["precio"] for p in productos}
print("\n8. Diccionario nombre -> precio:", precios)
print("   Precio del aceite:", precios["Aceite"])

# ----------------------------------------------------------------------------
# 9. Agrupar — GroupBy() en LINQ
# ----------------------------------------------------------------------------
por_categoria = {}
for p in productos:
    por_categoria.setdefault(p["categoria"], []).append(p["nombre"])
print("\n9. Agrupados por categoría:", por_categoria)

# ----------------------------------------------------------------------------
# 10. Comprensión de conjunto (set): valores sin repetir — Distinct() en LINQ
# ----------------------------------------------------------------------------
categorias = {p["categoria"] for p in productos}
print("\n10. Categorías distintas:", sorted(categorias))

# ----------------------------------------------------------------------------
# Consejo: una comprensión debe caber en una línea y leerse de corrido. Si
# necesita dos condiciones enredadas o un for dentro de otro, el ciclo
# normal se entiende mejor. Lo corto no siempre es lo más claro.
# ----------------------------------------------------------------------------
