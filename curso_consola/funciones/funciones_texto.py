# ============================================================================
# MÉTODOS PARA TEXTOS (str) EN PYTHON
# ============================================================================
# Equivale a: funciones/funciones_texto.php · funciones_texto.js · FuncionesTexto.cs
#             PSeInt módulo 7 (Longitud, Mayusculas, Subcadena...)
#
# Como en JS y C#, en Python son MÉTODOS del propio texto: se escriben
# después de un punto. En PHP y PSeInt eran funciones sueltas.
#
#   PHP:     strtoupper($mensaje)       PSeInt:  Mayusculas(mensaje)
#   Python:  mensaje.upper()
#
# Los textos son INMUTABLES: ningún método cambia el original; todos
# devuelven un texto nuevo.
# ============================================================================

mensaje = "  Hola Mundo, aprendiendo Python  "

# 1. Quitar espacios en blanco al inicio y al final (trim en PHP/JS)
print(f"Original: '{mensaje}'")
print(f"Con strip: '{mensaje.strip()}'")

limpio = mensaje.strip()

# 2. Mayúsculas y minúsculas
print("Mayúsculas:", limpio.upper())
print("Minúsculas:", limpio.lower())
print("Tipo título:", limpio.title())
print("Primera en mayúscula:", "barinas".capitalize())

# 3. Contar caracteres (strlen en PHP, .length en JS, Longitud en PSeInt)
print("Longitud:", len(limpio), "caracteres")

# 4. Cortar un texto: rebanadas (slices)
# texto[desde:hasta] -> las posiciones empiezan en 0 y "hasta" NO se incluye.
#   PHP:     substr($texto, 0, 4)
#   PSeInt:  Subcadena(texto, 1, 4)     (desde 1, incluye la 4)
#   Python:  texto[0:4]
print("Cortar (primeros 4):", limpio[0:4])
print("Cortar (desde la posición 5):", limpio[5:])
print("Últimos 6:", limpio[-6:])
print("Primera letra:", limpio[0])
print("Al revés:", limpio[::-1])

# 5. Reemplazar texto (str_replace en PHP)
print("Reemplazar:", limpio.replace("Python", "Programación"))

# 6. Buscar dentro de un texto
print("\n¿Contiene 'Mundo'?", "Mundo" in limpio)
print("Posición de 'Mundo':", limpio.find("Mundo"))      # -1 si no está
print("¿Empieza con 'Hola'?", limpio.startswith("Hola"))
print("¿Termina con 'PHP'?", limpio.endswith("PHP"))
print("¿Cuántas 'o' tiene?", limpio.count("o"))

# 7. Separar y unir (explode e implode en PHP; split y join en JS)
frase = "manzana,pera,uva"
lista = frase.split(",")
print("\nSeparar:", lista)
print("Unir:", " - ".join(lista))

# 8. Comprobar el contenido
print("\n'123'.isdigit():", "123".isdigit())      # útil para validar antes de int()
print("'abc'.isalpha():", "abc".isalpha())

# 9. Comparar sin importar mayúsculas
respuesta = "SI"
if respuesta.lower() == "si":
    print("\nEl usuario respondió que sí")

# 10. Escapar HTML (htmlspecialchars en PHP) — VITAL para evitar que un
# usuario inyecte código malicioso (XSS) si este texto se muestra en una
# página web. Se ve con detalle en seguridad/sanitizacion_xss.py.
import html

script = "<b>Hola</b> <script>alert('ataque XSS');</script>"
print("\nTexto con etiquetas (peligroso):", script)
print("Texto sanitizado (seguro):", html.escape(script))
