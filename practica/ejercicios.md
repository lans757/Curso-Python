# ✏️ Práctica por niveles

Los archivos de `curso_consola/` se **leen y se ejecutan**; estos ejercicios se **escriben desde cero**. Es la parte que viene del curso de pseudocódigo: allí cada módulo traía su hoja de ejercicios por niveles, y aquí se repite la idea con Python.

**Cómo trabajar**

1. Antes de escribir, responde: ¿qué **entra**?, ¿qué se **calcula**?, ¿qué **sale**?
2. Crea un archivo por ejercicio (`tarjeta.py`, `bisiesto.py`...) y ejecútalo con `python nombre.py`.
3. Prueba con un caso normal, uno **en el borde** y uno incorrecto.
4. Solo después compara con `soluciones/`. Hay muchas formas correctas de resolver cada uno.

Niveles: ⭐ básico · ⭐⭐ medio · ⭐⭐⭐ reto.

---

## 1. Fundamentos

> Antes: `fundamentos/variables.py`, `operadores.py`, `constantes.py` y `entrada_salida.py`.

1. ⭐ **Tarjeta de presentación.** Pide nombre, apellido y ciudad. Muestra los tres datos dentro de un marco hecho con guiones.
2. ⭐ **Rectángulo.** Pide la base y la altura (pueden tener decimales) y muestra el área y el perímetro.
3. ⭐⭐ **Compra con IVA.** Pide el precio de un producto y la cantidad. Con el IVA del 16 % guardado en una constante, muestra subtotal, IVA y total con dos decimales.
4. ⭐⭐ **Minutos y horas.** Pide una cantidad de minutos y muéstrala como horas y minutos (`135` → `2 horas y 15 minutos`). Usa `//` y `%`.
5. ⭐⭐⭐ **Reloj.** Pide una cantidad de segundos (por ejemplo `98765`) y muéstrala como días, horas, minutos y segundos.
6. ⭐⭐⭐ **Invertir.** Pide un número de tres cifras y muéstralo invertido (`472` → `274`) **como número**, usando solo operaciones aritméticas.

## 2. Condicionales

> Antes: `condicionales/condicionales.py`, `shorthand.py` y `switch.py`.

1. ⭐ **Positivo, negativo o cero.** Pide un número y di cuál de los tres es.
2. ⭐ **Par o impar.** Pide un número entero y di si es par o impar. Resuélvelo con un `if` normal y luego en una línea con el operador ternario.
3. ⭐⭐ **Nota cualitativa.** Pide una nota. Si no está entre 0 y 20, avisa que es inválida. Si es válida, muestra `Excelente` (19–20), `Muy bueno` (16–18), `Aprobado` (10–15) o `Reprobado` (0–9).
4. ⭐⭐ **Calculadora con menú.** Muestra un menú con sumar, restar, multiplicar y dividir. Usa `match` y valida que no se divida entre cero.
5. ⭐⭐⭐ **Año bisiesto.** Un año es bisiesto si es divisible entre 4, excepto los divisibles entre 100, que solo lo son si también son divisibles entre 400.
6. ⭐⭐⭐ **Piedra, papel o tijera.** El usuario escribe su jugada y la computadora elige la suya con `random.choice`. Muestra quién gana.

## 3. Ciclos

> Antes: toda la carpeta `ciclos/`.

1. ⭐ **Tabla de multiplicar.** Pide un número y muestra su tabla del 1 al 10.
2. ⭐ **Suma de 1 a n.** Pide `n` y calcula `1 + 2 + ... + n` con un acumulador. Luego compáralo con `sum(range(1, n + 1))`.
3. ⭐⭐ **Promedio de la clase.** Pide cuántos estudiantes hay y luego la nota de cada uno. Muestra el promedio y cuántos aprobaron (nota ≥ 10).
4. ⭐⭐ **Validar edad.** Pide una edad y repite la pregunta hasta que esté entre 1 y 120. Debe aguantar que el usuario escriba letras (pista: `try` / `except ValueError`).
5. ⭐⭐⭐ **Número primo.** Pide un número y di si es primo.
6. ⭐⭐⭐ **Adivina el número.** La computadora piensa un número del 1 al 20. El jugador tiene 5 intentos; después de cada uno se le dice `Muy alto` o `Muy bajo`.

## 4. Arreglos

> Antes: toda la carpeta `arreglos/` y `funciones/funciones_arreglos.py`.

1. ⭐ **Al revés.** Pide 5 números, guárdalos en una lista y muéstralos en orden inverso.
2. ⭐ **Resumen.** Con la lista del ejercicio anterior, muestra la suma, el promedio, el mayor y el menor.
3. ⭐⭐ **Por encima del promedio.** Con una lista de 8 notas, calcula el promedio y muestra solo las notas que lo superan.
4. ⭐⭐ **Búsqueda.** Con una lista de nombres, pide uno al usuario y di en qué posición aparece por primera vez y cuántas veces está. No debe importar si se escribe en mayúsculas o minúsculas.
5. ⭐⭐⭐ **Ranking.** Guarda cinco estudiantes como una lista de diccionarios (`nombre` y `nota`). Muestra el listado ordenado de mayor a menor nota, con el puesto de cada uno.
6. ⭐⭐⭐ **Tabla de notas.** Con una matriz de 4 estudiantes × 3 materias, muestra el promedio de cada estudiante, el promedio de cada materia y la nota más alta de toda la tabla.

## 5. Funciones

> Antes: toda la carpeta `funciones/` y `funciones_matematicas/matematicas.py`.

1. ⭐ **Par.** Escribe `es_par(numero)` que devuelva `True` o `False`. Úsala dentro de un `if`.
2. ⭐ **Mayor de tres.** Escribe `mayor_de_tres(a, b, c)` sin usar `max()`.
3. ⭐⭐ **Calificación.** Escribe `calificacion(nota)` que devuelva un **texto** (`"Excelente"`, `"Muy bueno"`, `"Aprobado"` o `"Reprobado"`). Úsala para mostrar la calificación de una lista de notas.
4. ⭐⭐ **Contar vocales.** Escribe `contar_vocales(frase)`. Debe contar mayúsculas y minúsculas.
5. ⭐⭐⭐ **Biblioteca de matemáticas.** Escribe `es_primo(n)`, `factorial(n)` y `mcd(a, b)` (máximo común divisor con el algoritmo de Euclides).
6. ⭐⭐⭐ **Palíndromo.** Escribe `es_palindromo(frase)` que ignore espacios y mayúsculas (`Anita lava la tina` → `True`).

---

## Cómo ejecutar las soluciones

Cada archivo de `soluciones/` reúne los seis ejercicios de su tema:

```bash
cd practica/soluciones
python fundamentos.py        # muestra la lista y pregunta cuál ejecutar
python ciclos.py 6           # ejecuta directamente el ejercicio 6
```
