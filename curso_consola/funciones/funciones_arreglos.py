# ============================================================================
# MÉTODOS ÚTILES PARA LISTAS Y DICCIONARIOS
# ============================================================================
# Equivale a: funciones/funciones_arreglos.php · funciones_arreglos.js
#             FuncionesArreglos.cs
# ============================================================================

amigo = {
    "telefono": 6545647,
    "edad": 20,
    "pais": "mexico",
}

semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("1. Equivalente a extract()")
# PHP: extract() convierte las claves de un array en VARIABLES sueltas.
# Python no tiene (ni conviene que tenga) algo así. Lo idiomático es
# desempaquetar las claves que necesitas, diciendo cuáles son:
telefono, pais = amigo["telefono"], amigo["pais"]
print(f"Mi amigo es de {pais} y su teléfono es {telefono}.")

print("\n2. Equivalente a array_pop()")
# .pop() quita el último elemento y lo devuelve. Igual que en PHP y JS.
ultimo_dia = semana.pop()
print(f"El día eliminado fue: {ultimo_dia}")
print(f"Ahora la semana tiene {len(semana)} días.")

print("\n3. Equivalente a join() / implode()")
# OJO con el orden: en Python el SEPARADOR va primero y la lista después.
#   PHP:     implode(" - ", $semana)
#   JS:      semana.join(" - ")
#   Python:  " - ".join(semana)
print("Días restantes:", " - ".join(semana))

print("\n4. Equivalente a rsort()")
# Ordena de forma descendente Y modifica la lista original.
semana.sort(reverse=True)
print("Semana ordenada de Z a A:", ", ".join(semana))

print("\n5. Equivalente a array_reverse()")
# A diferencia de sort(), invierte el orden actual sin importar el
# alfabeto: el primero pasa a ser el último.
semana_invertida = list(reversed(semana))
print("Semana invertida totalmente:", ", ".join(semana_invertida))

# ----------------------------------------------------------------------------
# Más métodos de listas
# ----------------------------------------------------------------------------
print("\n6. Agregar, insertar y quitar")
numeros = [10, 20, 30]
numeros.append(40)               # al final              (array_push)
numeros.insert(0, 5)             # en una posición       (array_unshift si es 0)
numeros.remove(20)               # quita por VALOR
del numeros[0]                   # quita por POSICIÓN
print(numeros)

print("\n7. Buscar")
print("¿Está el 30?", 30 in numeros)                     # in_array
print("Posición del 30:", numeros.index(30))             # array_search

print("\n8. Unir dos listas")                             # array_merge
print([1, 2] + [3, 4])

# ----------------------------------------------------------------------------
# Métodos de diccionarios
# ----------------------------------------------------------------------------
print("\n9. Diccionarios")
print("Claves:", list(amigo.keys()))                     # array_keys
print("Valores:", list(amigo.values()))                  # array_values
print("¿Existe la clave 'edad'?", "edad" in amigo)       # array_key_exists
print("Clave que no existe, con valor por defecto:", amigo.get("ciudad", "Sin ciudad"))

amigo.update({"ciudad": "Monterrey", "edad": 21})        # agrega y modifica varias
print("Actualizado:", amigo)
