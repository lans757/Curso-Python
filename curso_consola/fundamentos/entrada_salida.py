# ============================================================================
# ENTRADA Y SALIDA: input() y print()
# ============================================================================
# Equivale a: PSeInt módulo 0 (Leer y Escribir)
#             formularios/ del curso de PHP (la entrada allá llega por GET/POST)
#             Console.ReadLine() de C# · readline() de PHP en consola
#
# Todo programa hace tres cosas: ENTRADA -> PROCESO -> SALIDA.
#
#   PSeInt:  Escribir Sin Saltar "Nombre: ";  Leer nombre;
#   Python:  nombre = input("Nombre: ")
#
# input() hace las dos cosas a la vez: muestra la pregunta y espera la respuesta.
#
# LA REGLA MÁS IMPORTANTE: input() SIEMPRE devuelve TEXTO.
# En PSeInt, "Leer edad" guardaba un número si edad era Entero. En Python hay
# que convertir a mano con int() o float(), o la suma no funcionará.
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Pedir un texto
# ----------------------------------------------------------------------------
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. ¡Bienvenido al curso!")

# ----------------------------------------------------------------------------
# 2. Pedir un número (hay que convertir)
# ----------------------------------------------------------------------------
edad = int(input("¿Cuántos años tienes? "))
print(f"El próximo año tendrás {edad + 1} años.")

# Sin el int(), edad sería "12" (texto) y edad + 1 daría un TypeError.

estatura = float(input("¿Cuánto mides en metros? (ejemplo: 1.52) "))
print(f"Mides {estatura * 100:.0f} centímetros.")

# ----------------------------------------------------------------------------
# 3. Opciones de print()
# ----------------------------------------------------------------------------
print("\nVarias cosas separadas por coma:", nombre, edad, estatura)

# end="" evita el salto de línea: es el "Escribir Sin Saltar" de PSeInt.
print("Cargando", end="")
print("... listo")

# sep cambia el separador entre los datos.
print("2026", "10", "13", sep="-")

# ----------------------------------------------------------------------------
# 4. Dar formato a los números dentro de una f-string
# ----------------------------------------------------------------------------
precio = 12.34567
print(f"\nPrecio con 2 decimales: {precio:.2f}")      # round($precio, 2) en PHP
print(f"Número con separador de miles: {1234567:,}")
print(f"Porcentaje: {0.256:.1%}")
