# ============================================================================
# match ... case — EL "SWITCH" DE PYTHON
# ============================================================================
# Equivale a: condicionales/switch.php · switch.js · Switch.cs
#             "Segun ... Hacer" de PSeInt (módulo 3)
#
# Sirve para comparar la MISMA variable con muchos valores distintos. Es más
# legible que una fila larga de elif cuando solo hay comparaciones de igualdad.
#
#   PSeInt:  Segun mes Hacer  1: ...  De Otro Modo: ...  FinSegun
#   PHP/JS/C#:  switch (mes) { case 'Enero': ... break; default: ... }
#   Python:     match mes:
#                   case "Enero": ...
#                   case _: ...
#
# Diferencias con el switch de PHP, JS y C#:
# - NO lleva "break": cada case termina solo (igual que en PSeInt). Olvidar
#   el break era el error clásico del switch; aquí no puede pasar.
# - Varios valores en un mismo case se separan con una barra: |
# - El "default" se escribe "case _" (un guion bajo).
#
# match existe desde Python 3.10. En versiones anteriores se usa if/elif.
# ============================================================================

mes = "Enero"

match mes:
    case "Diciembre":
        print("Feliz Navidad")
    case "Enero":
        print("Feliz Año Nuevo")
    case "Julio":
        print("Feliz Julio")
    # Podemos agrupar casos que comparten la misma respuesta
    case "Marzo" | "Abril":
        print("Estamos en primavera")
    case _:
        print("En este mes no hay celebración programada")

# ----------------------------------------------------------------------------
# Ejemplo típico: el menú de una calculadora (como en PSeInt)
# ----------------------------------------------------------------------------
opcion = 4
a = 12
b = 0

print("\nMenú de calculadora, opción", opcion)

match opcion:
    case 1:
        print("Suma:", a + b)
    case 2:
        print("Resta:", a - b)
    case 3:
        print("Multiplicación:", a * b)
    case 4:
        # Dentro de un case se puede escribir cualquier cosa, también un if.
        if b == 0:
            print("Error: no se puede dividir entre cero")
        else:
            print("División:", a / b)
    case _:
        print("Opción no válida")

# ----------------------------------------------------------------------------
# La alternativa clásica: un diccionario
# Antes de que existiera match, así se resolvía en Python. Sigue siendo muy
# útil cuando cada caso solo devuelve un valor.
# ----------------------------------------------------------------------------
dias = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}

numero_dia = 3
print("\nDía", numero_dia, "->", dias.get(numero_dia, "Fin de semana"))
numero_dia = 7
print("Día", numero_dia, "->", dias.get(numero_dia, "Fin de semana"))

# ----------------------------------------------------------------------------
# Diferencia clave con if:
# match evalúa la expresión UNA sola vez y busca el case que coincide.
# Es ideal para menús, estados o variables con varias opciones fijas.
# Para rangos (nota >= 18, nota >= 10...) sigue siendo mejor if/elif.
# ----------------------------------------------------------------------------
