# ============================================================================
# for SOBRE COLECCIONES — EL "FOREACH" DE PYTHON
# ============================================================================
# Equivale a: ciclos/ciclo_foreach.php · CicloForeach.cs · for...of de JS
# En PSeInt no existía: siempre se recorría por posición con "Para i <- 1 Hasta n".
#
# En Python, el for normal YA ES un foreach: recorre cualquier colección
# elemento por elemento, sin índices.
#
#   PHP:     foreach ($frutas as $fruta) { ... }
#   JS:      for (const fruta of frutas) { ... }
#   C#:      foreach (var fruta in frutas) { ... }
#   Python:  for fruta in frutas:
# ============================================================================

print("--- FOR SOBRE UNA LISTA (valores) ---")
frutas = ["Manzana", "Pera", "Uva", "Sandía"]

# EXPLICACIÓN DEL RECORRIDO:
# 1. Python toma la lista frutas.
# 2. Se sitúa en el primer elemento ("Manzana").
# 3. Copia ese valor a la variable temporal fruta.
# 4. Ejecuta el bloque usando fruta.
# 5. Salta solo al siguiente elemento, hasta llegar al final.
for fruta in frutas:
    print(f"Fruta: {fruta}")

# ----------------------------------------------------------------------------
# ¿Y si necesito el número de posición? -> enumerate()
# Devuelve la posición Y el valor en cada vuelta.
# ----------------------------------------------------------------------------
print("\n--- CON POSICIÓN: enumerate() ---")
for posicion, fruta in enumerate(frutas):
    print(f"[{posicion}] {fruta}")

# Para que empiece a contar en 1 (como le gusta a las personas):
for numero, fruta in enumerate(frutas, start=1):
    print(f"{numero}. {fruta}")

# ----------------------------------------------------------------------------
# Recorrer un diccionario (clave => valor)
# ----------------------------------------------------------------------------
print("\n--- FOR SOBRE UN DICCIONARIO (clave y valor) ---")
edades = {"Juan": 25, "Maria": 30, "Pedro": 22}

# EXPLICACIÓN DEL RECORRIDO:
# 1. .items() entrega cada elemento como una pareja (clave, valor).
# 2. nombre toma la clave ("Juan") y edad toma el valor (25).
#
#   PHP:  foreach ($edades as $nombre => $edad)
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años.")

print("\nSolo las claves:")
for nombre in edades:                 # recorrer el diccionario da las claves
    print("-", nombre)

print("\nSolo los valores:")
for edad in edades.values():
    print("-", edad)

# ----------------------------------------------------------------------------
# Recorrer un texto: un texto también es una colección (de letras)
# ----------------------------------------------------------------------------
print("\n--- FOR SOBRE UN TEXTO ---")
vocales = 0
for letra in "programacion":
    if letra in "aeiou":
        vocales += 1
print(f"La palabra 'programacion' tiene {vocales} vocales")

# ----------------------------------------------------------------------------
# Recorrer dos listas a la vez: zip()
# Es la versión cómoda de los "arreglos paralelos" de PSeInt.
# ----------------------------------------------------------------------------
print("\n--- DOS LISTAS A LA VEZ: zip() ---")
nombres = ["Ana", "Luis", "Marta"]
notas = [18, 14, 20]

for nombre, nota in zip(nombres, notas):
    print(f"{nombre}: {nota}")
