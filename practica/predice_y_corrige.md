# 🔍 Predice y corrige

Otra idea tomada del curso de pseudocódigo: **antes de ejecutar, predice**. Lee cada fragmento, anota en papel qué crees que se verá en pantalla y solo entonces compruébalo en Python. Las respuestas están al final.

Casi todos estos casos son trampas reales para quien viene de PSeInt, PHP, JavaScript o C#.

## Parte A — Predice la salida

### P1 — `range` no incluye el final

```python
for i in range(1, 5):
    print(i, end=" ")
```

### P2 — `input()` siempre devuelve texto

Supón que el usuario escribe `5`.

```python
numero = input("Número: ")
print(numero * 3)
```

### P3 — La división siempre da decimales

```python
print(10 / 2)
print(10 // 3)
print(10 % 3)
```

### P4 — Las posiciones empiezan en 0

```python
frutas = ["manzana", "pera", "uva"]
print(frutas[1])
print(frutas[-1])
print(len(frutas))
```

### P5 — Dos nombres para la misma lista

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

### P6 — `==` no convierte tipos

```python
print(10 == "10")
print(10 == 10.0)
print("Ana" == "ana")
```

### P7 — La sangría decide qué está dentro del ciclo

```python
total = 0
for precio in [10, 20, 30]:
    total += precio
print("Total:", total)
```

¿Y si la última línea tuviera cuatro espacios de sangría?

### P8 — `sort()` no devuelve la lista

```python
notas = [15, 8, 20]
ordenadas = notas.sort()
print(ordenadas)
print(notas)
```

## Parte B — Encuentra el error

Cada fragmento tiene **un** error. Di cuál es y cómo se arregla.

### E1 — Debería decir si aprobó

```python
nota = 12
if nota >= 10
    print("Aprobado")
```

### E2 — Debería mostrar la edad del próximo año

```python
edad = input("Edad: ")
print("El próximo año tendrás", edad + 1)
```

### E3 — Debería mostrar los tres nombres

```python
nombres = ["Ana", "Luis", "Marta"]
for i in range(1, 4):
    print(nombres[i])
```

### E4 — Debería contar hasta 3 y terminar

```python
contador = 1
while contador <= 3:
    print(contador)
```

### E5 — Debería sumar 1 al contador de visitas

```python
visitas = 0

def registrar_visita():
    visitas = visitas + 1

registrar_visita()
print(visitas)
```

### E6 — Debería mostrar "Mayor de edad" solo si lo es

```python
edad = 15
if edad >= 18:
    print("Verificando...")
print("Mayor de edad")
```

---

<details>
<summary>Ver las respuestas (solo después de intentarlo)</summary>

**Parte A**

- **P1:** `1 2 3 4`. El 5 no se incluye. Para llegar hasta el 5 se escribe `range(1, 6)`.
- **P2:** `555`. `input()` devuelve el texto `"5"`, y un texto multiplicado por 3 se repite tres veces. Para obtener 15 hace falta `int(input("Número: "))`.
- **P3:** `5.0`, `3` y `1`. La barra simple siempre da `float`, aunque la división sea exacta. `//` es la división entera y `%` el residuo.
- **P4:** `pera`, `uva` y `3`. La posición 1 es el **segundo** elemento; `-1` es el último.
- **P5:** `[1, 2, 3, 4]`. `b = a` no copia la lista: `a` y `b` son dos nombres para la misma. Para una copia real se usa `b = a.copy()`.
- **P6:** `False`, `True` y `False`. Python no convierte un texto en número para comparar (en PHP, `10 == "10"` daba verdadero). Sí considera iguales un entero y un decimal con el mismo valor. Y las mayúsculas cuentan.
- **P7:** `Total: 60`, una sola vez. Con sangría, el `print` quedaría **dentro** del ciclo y mostraría `Total: 10`, `Total: 30` y `Total: 60`.
- **P8:** `None` y `[8, 15, 20]`. `.sort()` ordena la lista original y no devuelve nada. Para obtener una lista nueva se usa `sorted(notas)`.

**Parte B**

- **E1:** faltan los **dos puntos** al final de la línea del `if`. Python lo señala con `SyntaxError: expected ':'`.
- **E2:** `edad` es texto y no se le puede sumar un número (`TypeError`). Corrección: `edad = int(input("Edad: "))`.
- **E3:** las posiciones van de 0 a 2, y `range(1, 4)` produce 1, 2 y 3: se salta a Ana y falla con `IndexError` en la posición 3. Corrección: `for nombre in nombres:` (o `range(len(nombres))`).
- **E4:** ciclo infinito: falta `contador += 1` dentro del `while`.
- **E5:** al asignar dentro de la función, Python trata a `visitas` como variable **local**, y como todavía no tiene valor falla con `UnboundLocalError`. Lo recomendable es recibir y devolver: `def registrar_visita(visitas): return visitas + 1` y luego `visitas = registrar_visita(visitas)`.
- **E6:** el segundo `print` no tiene sangría, así que está **fuera** del `if` y se ejecuta siempre. Debe alinearse con el primero.

</details>
