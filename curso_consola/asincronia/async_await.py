# ============================================================================
# ASYNC / AWAIT EN PYTHON
# ============================================================================
# Idiomático de Python. Equivale a: asincronia/AsyncAwait.cs · async/await de JS
# PHP y PSeInt son síncronos: cada línea espera a que termine la anterior.
#
# Un programa normal hace UNA cosa a la vez. Si pide datos a una página web y
# tarda 2 segundos, el programa entero se queda esperando 2 segundos.
#
# Con async/await, una función puede CEDER el turno mientras espera algo
# lento (una respuesta de red, una consulta a la base de datos) para que el
# programa aproveche ese tiempo en otra tarea.
#
# Piensa en un cocinero: no se queda mirando el horno. Mete el pan (await),
# y mientras se hornea, pica la ensalada.
#
#   async def funcion():   -> define una función asíncrona ("corrutina")
#   await algo_lento()     -> "espera aquí, pero deja trabajar a los demás"
#   asyncio.run(main())    -> arranca todo (solo una vez, al principio)
#   asyncio.gather(a, b)   -> lanza varias tareas a la vez y espera a todas
#                             (Task.WhenAll en C#, Promise.all en JS)
# ============================================================================

import asyncio
import time


# Simula una operación lenta (descargar algo, consultar una base de datos).
# asyncio.sleep() NO bloquea: cede el turno durante esos segundos.
async def descargar(nombre, segundos):
    print(f"  Empezando a descargar {nombre}...")
    await asyncio.sleep(segundos)
    print(f"  {nombre} listo ({segundos} s)")
    return f"contenido de {nombre}"


# ----------------------------------------------------------------------------
# 1. Ejecución SECUENCIAL: una después de la otra
# Tiempo total = suma de todas las esperas.
# ----------------------------------------------------------------------------
async def ejemplo_secuencial():
    inicio = time.perf_counter()
    await descargar("foto.jpg", 1)
    await descargar("video.mp4", 1.5)
    await descargar("cancion.mp3", 0.5)
    print(f"  Tiempo total: {time.perf_counter() - inicio:.1f} segundos")


# ----------------------------------------------------------------------------
# 2. Ejecución CONCURRENTE: todas a la vez
# Tiempo total = lo que tarde la más lenta.
# ----------------------------------------------------------------------------
async def ejemplo_concurrente():
    inicio = time.perf_counter()
    resultados = await asyncio.gather(
        descargar("foto.jpg", 1),
        descargar("video.mp4", 1.5),
        descargar("cancion.mp3", 0.5),
    )
    print(f"  Tiempo total: {time.perf_counter() - inicio:.1f} segundos")
    print("  Resultados (en el orden en que se pidieron):", resultados)


# ----------------------------------------------------------------------------
# 3. Manejo de errores: try / except funciona igual
# ----------------------------------------------------------------------------
async def descarga_que_falla():
    await asyncio.sleep(0.2)
    raise ConnectionError("El servidor no respondió.")


async def ejemplo_con_errores():
    try:
        await descarga_que_falla()
    except ConnectionError as e:
        print("  Error capturado:", e)


async def main():
    print("1. Secuencial (una tras otra)")
    await ejemplo_secuencial()

    print("\n2. Concurrente (todas a la vez con asyncio.gather)")
    await ejemplo_concurrente()

    print("\n3. Errores en código asíncrono")
    await ejemplo_con_errores()


# Punto de entrada: una función async no se puede llamar directamente; hay
# que arrancarla con asyncio.run().
asyncio.run(main())

# ----------------------------------------------------------------------------
# ¿Cuándo sirve?
# - SÍ: cuando el programa ESPERA cosas de afuera (red, archivos, base de
#   datos). Un servidor web que atiende a 100 usuarios a la vez.
# - NO: cuando el programa hace CÁLCULOS pesados. Ahí no hay espera que
#   aprovechar, y async no lo hace más rápido.
#
# Error típico: olvidar el "await". La función no se ejecuta y Python avisa
# con "coroutine ... was never awaited".
# ----------------------------------------------------------------------------
