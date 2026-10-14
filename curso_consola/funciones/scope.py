# ============================================================================
# SCOPE (ÁMBITO) DE LAS VARIABLES EN PYTHON
# ============================================================================
# Equivale a: funciones/scope.php · scope.js · Scope.cs · PSeInt módulo 6 (ámbito)
#
# El ámbito es la zona del programa donde una variable existe.
#
# Cómo lo trata cada lenguaje:
# - PSeInt: una función NO puede ver nada de afuera. Todo llega por parámetro.
# - PHP:    una función no ve las variables de afuera salvo que uses "global".
# - JS/C#:  una función sí ve las variables (o campos) de afuera.
# - Python: una función puede LEER las variables de afuera sin pedir permiso,
#           pero para MODIFICARLAS tiene que declararlo con "global".
# ============================================================================

# ÁMBITO GLOBAL: variable declarada fuera de cualquier función.
mensaje = "Hola desde fuera de la función"


def mostrar_mensaje():
    # ÁMBITO LOCAL: esta variable SOLO existe dentro de la función.
    mensaje_local = "Hola desde DENTRO de la función"

    print("LOCAL:", mensaje_local)
    # Leer una variable global funciona directamente (en PHP haría falta "global").
    print("GLOBAL (solo lectura, sin palabra clave):", mensaje)


print("Demostración de Scope")
mostrar_mensaje()
print("----------")
print("FUERA:", mensaje)

# Si intentáramos usar mensaje_local aquí afuera:
# print(mensaje_local)   # NameError: name 'mensaje_local' is not defined


# ----------------------------------------------------------------------------
# La trampa: ASIGNAR dentro de la función crea una variable local NUEVA
# con el mismo nombre. La global no se entera.
# ----------------------------------------------------------------------------
contador = 0


def incrementar_mal():
    contador = 100           # esto es OTRA variable, local, que tapa a la global


incrementar_mal()
print("\nDespués de incrementar_mal(), contador vale:", contador)      # sigue en 0


# ----------------------------------------------------------------------------
# Con "global" sí se modifica la variable de afuera (como en PHP)
# ----------------------------------------------------------------------------
def incrementar_con_global():
    global contador
    contador += 1


incrementar_con_global()
print("Después de incrementar_con_global(), contador vale:", contador)  # 1


# ----------------------------------------------------------------------------
# LA FORMA RECOMENDADA: no usar global. Recibir por parámetro y devolver.
# Es lo que PSeInt obligaba a hacer, y es buena práctica en cualquier
# lenguaje: la función se entiende sola y es más fácil de probar.
# ----------------------------------------------------------------------------
def incrementar(valor):
    return valor + 1


contador = incrementar(contador)
print("Después de contador = incrementar(contador):", contador)         # 2

# ----------------------------------------------------------------------------
# Diferencia con JS y C#: en Python los bloques if / for / while NO crean
# un ámbito nuevo. Una variable creada dentro de un if sigue existiendo
# después. Solo las funciones (y las clases) crean ámbito.
# ----------------------------------------------------------------------------
if True:
    creada_en_el_if = "Sigo existiendo fuera del if"

print("\n" + creada_en_el_if)
