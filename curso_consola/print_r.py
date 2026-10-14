# ============================================================================
# print() y pprint() — EQUIVALENTE A print_r()
# ============================================================================
# Equivale a: print_r.php · print_r.js · PrintR.cs
#
# print_r() de PHP muestra una variable de forma legible, sin decir su tipo.
# En Python eso lo hace print() directamente: sabe mostrar listas y
# diccionarios sin ayuda (en PHP, "echo $arreglo" solo imprime "Array").
#
# Para estructuras grandes o anidadas existe pprint ("pretty print"), que las
# acomoda en varias líneas con sangría, como hace print_r dentro de <pre>.
# ============================================================================

from pprint import pprint

texto = "Carlos"
numero = 10
numero2 = "5"
arreglo = ["Carlos", "Cesar", "Alejandro"]
arreglo_asociativo = {"nombre": "Carlos", "edad": 20}
booleano = False

print("Variable Texto:", texto)
print("Variable Numero (entero):", numero)
print("Variable Numero2 (texto):", numero2)
print("Variable Arreglo Indexado:", arreglo)
print("Variable Arreglo Asociativo:", arreglo_asociativo)

# Diferencia con PHP: allá print_r(false) no imprime NADA.
# En Python siempre se ve el valor: False.
print("Variable Booleana:", booleano)

# ----------------------------------------------------------------------------
# pprint: para estructuras anidadas que no caben en una línea
# ----------------------------------------------------------------------------
cursos = {
    "Programacion": {
        "GrupoA": [{"nombre": "Ana", "nota": 18}, {"nombre": "Luis", "nota": 15}],
        "GrupoB": [{"nombre": "Carlos", "nota": 17}],
    },
    "Diseno": {"GrupoC": [{"nombre": "Maria", "nota": 19}]},
}

print("\nCon print() normal (todo en una línea):")
print(cursos)

print("\nCon pprint() (acomodado, como print_r dentro de <pre>):")
pprint(cursos, width=60)
