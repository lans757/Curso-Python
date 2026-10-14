# ============================================================================
# MANEJO DE ERRORES CON try - except - finally
# ============================================================================
# Equivale a: errores/try_catch.php · TryCatch.cs · try/catch de JS
# En PSeInt no existía: se validaban los datos ANTES con un Si o un Repetir.
#
# Permite controlar los errores que ocurren durante la ejecución, evitando
# que el programa se detenga de golpe.
#
#   PHP / JS / C#          Python
#   -------------------    ---------------------
#   try { }                try:
#   catch (Exception e)    except Exception as e:
#   finally { }            finally:
#   throw new Exception()  raise Exception()
#   $e->getMessage()       str(e)   o simplemente   print(e)
# ============================================================================

# ----------------------------------------------------------------------------
# Ejemplo 1: división entre cero
# ----------------------------------------------------------------------------
divisor = 0

print("Ejemplo 1: División básica")
try:
    if divisor == 0:
        # Si detectamos un error, "lanzamos" una excepción a mano.
        raise Exception("Error: No se puede dividir por cero.")

    resultado = 10 / divisor
    print("El resultado es:", resultado)
except Exception as e:
    print("Ocurrió un problema:", e)

# ----------------------------------------------------------------------------
# En realidad no hacía falta lanzarla a mano: Python ya lanza su propia
# excepción, con un tipo específico para cada clase de error.
# ----------------------------------------------------------------------------
print("\nEjemplo 1b: la excepción que lanza Python por su cuenta")
try:
    resultado = 10 / divisor
except ZeroDivisionError as e:
    print("Python avisó:", e)

print()


# ----------------------------------------------------------------------------
# Ejemplo 2: bloque finally
# Se ejecuta SIEMPRE, haya ocurrido un error o no. Útil para cerrar
# conexiones o limpiar recursos.
# ----------------------------------------------------------------------------
def verificar_edad(edad):
    try:
        print("Verificando edad...")
        if edad < 18:
            raise Exception("Eres menor de edad, acceso denegado.")
        print("Acceso concedido.")
    except Exception as e:
        print("Excepción capturada:", e)
    finally:
        print("--- Proceso de verificación terminado (esto siempre se ve) ---")


print("Ejemplo 2: Uso de finally")
verificar_edad(20)      # caso válido
print()
verificar_edad(15)      # caso con error

# ----------------------------------------------------------------------------
# Ejemplo 3: el caso más común — convertir lo que escribió el usuario
# int("doce") lanza ValueError. Aquí se captura y se da un valor por defecto.
# ----------------------------------------------------------------------------
print("\nEjemplo 3: convertir texto a número")
for texto in ["25", "doce", "3.5"]:
    try:
        numero = int(texto)
        print(f"  '{texto}' -> {numero}")
    except ValueError:
        print(f"  '{texto}' no es un número entero válido")

# ----------------------------------------------------------------------------
# Ejemplo 4: varios except y el bloque else
# - Se puede capturar cada tipo de error por separado.
# - else se ejecuta solo si NO hubo ningún error (no existe en PHP, JS ni C#).
# ----------------------------------------------------------------------------
print("\nEjemplo 4: varios tipos de error")
notas = [15, 18, 0]


def dividir_nota(posicion, divisor):
    try:
        resultado = notas[posicion] / divisor
    except IndexError:
        print("  Esa posición no existe en la lista")
    except ZeroDivisionError:
        print("  No se puede dividir entre cero")
    else:
        print("  Resultado:", resultado)


dividir_nota(0, 3)      # todo bien
dividir_nota(9, 3)      # IndexError
dividir_nota(0, 0)      # ZeroDivisionError

# ----------------------------------------------------------------------------
# Excepciones que verás a menudo:
#   ValueError         int("hola")
#   TypeError          "5" + 5
#   ZeroDivisionError  10 / 0
#   IndexError         lista[99]
#   KeyError           diccionario["no_existe"]
#   FileNotFoundError  open("no_existe.txt")
#
# Mala práctica:  except:  (sin decir qué error) -> esconde TODOS los
# errores, también los de tipeo. Captura siempre el tipo más específico.
# ----------------------------------------------------------------------------
