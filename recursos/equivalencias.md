# 🔁 Equivalencias: PSeInt ↔ PHP ↔ JavaScript ↔ C# ↔ Python

Tabla puente entre los cinco cursos. Si ya sabes hacer algo en uno de ellos, búscalo en su columna y lee la de Python.

## 1. Estructura básica

| Concepto | PSeInt | PHP | JavaScript | C# | Python |
|---|---|---|---|---|---|
| Inicio y fin | `Algoritmo x` … `FinAlgoritmo` | `<?php … ?>` | *(nada)* | clase + `Main` | *(nada)* |
| Fin de instrucción | `;` | `;` | `;` | `;` | salto de línea |
| Bloques | `Fin…` | `{ }` | `{ }` | `{ }` | **sangría** + `:` |
| Comentario | `//` | `//` o `#` | `//` | `//` | `#` |
| Mostrar | `Escribir "Hola";` | `echo "Hola";` | `console.log("Hola")` | `Console.WriteLine("Hola");` | `print("Hola")` |
| Mostrar sin salto | `Escribir Sin Saltar` | `echo` | `process.stdout.write` | `Console.Write` | `print("Hola", end="")` |
| Pedir un dato | `Leer x;` | `readline()` / formulario | `prompt()` | `Console.ReadLine()` | `x = input("…")` |

## 2. Variables, tipos y constantes

| Concepto | PSeInt | PHP | JavaScript | C# | Python |
|---|---|---|---|---|---|
| Declarar y asignar | `Definir e Como Entero; e <- 16;` | `$e = 16;` | `let e = 16;` | `int e = 16;` | `e = 16` |
| Entero | `Entero` | `int` | `number` | `int` | `int` |
| Decimal | `Real` | `float` | `number` | `double` | `float` |
| Texto | `Texto` | `string` | `string` | `string` | `str` |
| Lógico | `Logico` (`Verdadero`) | `bool` (`true`) | `boolean` (`true`) | `bool` (`true`) | `bool` (`True`) |
| Nulo | *(no existe)* | `null` | `null` / `undefined` | `null` | `None` |
| Constante | *(por convención)* | `define("PI", 3.14)` | `const PI = 3.14` | `const double Pi` | `PI = 3.14` *(por convención)* |
| Tipado | estático | dinámico y débil | dinámico y débil | estático y fuerte | dinámico y **fuerte** |
| ¿Distingue mayúsculas? | No | Sí en variables | Sí | Sí | Sí |
| Texto con variables | `"Hola ", n` | `"Hola $n"` | `` `Hola ${n}` `` | `$"Hola {n}"` | `f"Hola {n}"` |
| Texto a número | `ConvertirANumero(t)` | `(int)$t` | `Number(t)` | `int.Parse(t)` | `int(t)` |
| Ver el tipo | *(paso a paso)* | `gettype($x)` | `typeof x` | `x.GetType()` | `type(x)` |

## 3. Operadores

| Concepto | PSeInt | PHP | JavaScript | C# | Python |
|---|---|---|---|---|---|
| Potencia | `^` | `**` | `**` | `Math.Pow` | `**` |
| División entera | `TRUNC(a / b)` | `intdiv(a, b)` | `Math.floor(a / b)` | `a / b` (enteros) | `a // b` |
| Residuo | `%` o `MOD` | `%` | `%` | `%` | `%` |
| Incrementar | `i <- i + 1` | `$i++` | `i++` | `i++` | `i += 1` |
| Igual | `=` | `==` / `===` | `==` / `===` | `==` | `==` |
| Distinto | `<>` | `!=` / `!==` | `!=` / `!==` | `!=` | `!=` |
| Y lógico | `Y` | `&&` | `&&` | `&&` | `and` |
| O lógico | `O` | `\|\|` | `\|\|` | `\|\|` | `or` |
| NO lógico | `NO` | `!` | `!` | `!` | `not` |
| Concatenar | `+` | `.` | `+` | `+` | `+` |
| ¿Está en la lista? | *(ciclo)* | `in_array($x, $a)` | `a.includes(x)` | `a.Contains(x)` | `x in a` |

## 4. Estructuras de control

| Concepto | PSeInt | PHP / JS / C# | Python |
|---|---|---|---|
| Condicional | `Si c Entonces … FinSi` | `if (c) { … }` | `if c:` |
| Doble | `SiNo` | `else { … }` | `else:` |
| Encadenado | `Si` dentro de `SiNo` | `else if` | `elif` |
| Selección múltiple | `Segun x Hacer` | `switch (x) { case 1: … break; }` | `match x:` + `case 1:` |
| Caso por defecto | `De Otro Modo:` | `default:` | `case _:` |
| Ternario | *(no existe)* | `c ? a : b` | `a if c else b` |
| Valor por defecto | *(no existe)* | `$x ?? "y"` | `x or "y"` · `d.get("k", "y")` |
| Ciclo contado | `Para i <- 1 Hasta 10 Hacer` | `for (i = 1; i <= 10; i++)` | `for i in range(1, 11):` |
| Ciclo condicional | `Mientras c Hacer` | `while (c) { … }` | `while c:` |
| Al menos una vez | `Repetir … Hasta Que c` | `do { … } while (!c);` | `while True:` … `if c: break` |
| Recorrer colección | `Para i <- 1 Hasta n` | `foreach` / `for…of` | `for x in coleccion:` |
| Con posición | *(el índice `i`)* | `foreach ($a as $i => $x)` | `for i, x in enumerate(a):` |
| Salir del ciclo | bandera | `break` | `break` |
| Saltar una vuelta | envolver en `Si` | `continue` | `continue` |

> ⚠️ **`range(1, 11)` llega hasta el 10.** El último número nunca se incluye. Es la diferencia que más errores causa al venir de PSeInt.

## 5. Arreglos

| Concepto | PSeInt | PHP | JavaScript | C# | Python |
|---|---|---|---|---|---|
| Lista | `Dimension a[3]` | `[10, 20, 30]` | `[10, 20, 30]` | `List<int>` | `[10, 20, 30]` |
| Primera posición | `a[1]` | `$a[0]` | `a[0]` | `a[0]` | `a[0]` |
| Última posición | `a[n]` | `end($a)` | `a.at(-1)` | `a[^1]` | `a[-1]` |
| Cantidad | *(variable `n`)* | `count($a)` | `a.length` | `a.Count` | `len(a)` |
| Agregar al final | *(manual)* | `$a[] = x` | `a.push(x)` | `a.Add(x)` | `a.append(x)` |
| Quitar el último | *(manual)* | `array_pop($a)` | `a.pop()` | `a.RemoveAt(…)` | `a.pop()` |
| Clave-valor | arreglos paralelos | array asociativo | objeto `{ }` | `Dictionary<K,V>` | `dict` `{ }` |
| Matriz | `m[f, c]` | `$m[f][c]` | `m[f][c]` | `m[f, c]` | `m[f][c]` |
| Ordenar | burbuja a mano | `sort($a)` | `a.sort()` | `a.Sort()` | `a.sort()` · `sorted(a)` |
| Unir con separador | *(ciclo)* | `implode("-", $a)` | `a.join("-")` | `string.Join("-", a)` | `"-".join(a)` |
| Filtrar | ciclo + `Si` | `array_filter` | `a.filter(…)` | `a.Where(…)` | `[x for x in a if …]` |
| Transformar | ciclo | `array_map` | `a.map(…)` | `a.Select(…)` | `[f(x) for x in a]` |
| Sumar | acumulador | `array_sum($a)` | `a.reduce(…)` | `a.Sum()` | `sum(a)` |

## 6. Funciones

| Concepto | PSeInt | PHP | JavaScript | C# | Python |
|---|---|---|---|---|---|
| Sin retorno | `SubProceso f(x)` | `function f($x) { }` | `function f(x) { }` | `void F(int x) { }` | `def f(x):` |
| Con retorno | `Funcion r <- f(x)` | `return $r;` | `return r;` | `return r;` | `return r` |
| Valor por defecto | *(no existe)* | `$x = 5` | `x = 5` | `int x = 5` | `x=5` |
| Por referencia | `x Por Referencia` | `&$x` | *(objetos)* | `ref x` | *(listas y diccionarios)* |
| Variable global dentro | *(no existe)* | `global $x;` | *(directo)* | campo `static` | `global x` *(solo para modificar)* |
| Función corta | *(no existe)* | `fn($x) => $x * 2` | `x => x * 2` | `x => x * 2` | `lambda x: x * 2` |
| Dividir en archivos | *(un solo archivo)* | `include` / `require` | `import` | `using` | `import` |

## 7. Funciones integradas

| Qué hace | PSeInt | PHP | JavaScript | C# | Python |
|---|---|---|---|---|---|
| Raíz cuadrada | `RAIZ(x)` | `sqrt($x)` | `Math.sqrt(x)` | `Math.Sqrt(x)` | `math.sqrt(x)` |
| Valor absoluto | `ABS(x)` | `abs($x)` | `Math.abs(x)` | `Math.Abs(x)` | `abs(x)` |
| Redondear | `REDON(x)` | `round($x, 2)` | `x.toFixed(2)` | `Math.Round(x, 2)` | `round(x, 2)` |
| Hacia arriba | *(con `TRUNC`)* | `ceil($x)` | `Math.ceil(x)` | `Math.Ceiling(x)` | `math.ceil(x)` |
| Quitar decimales | `TRUNC(x)` | `intval($x)` | `Math.trunc(x)` | `(int)x` | `int(x)` |
| Al azar entre 1 y 10 | `ALEATORIO(1, 10)` | `rand(1, 10)` | `Math.floor(Math.random()*10)+1` | `rnd.Next(1, 11)` | `random.randint(1, 10)` |
| Longitud | `Longitud(t)` | `strlen($t)` | `t.length` | `t.Length` | `len(t)` |
| Mayúsculas | `Mayusculas(t)` | `strtoupper($t)` | `t.toUpperCase()` | `t.ToUpper()` | `t.upper()` |
| Quitar espacios | *(no existe)* | `trim($t)` | `t.trim()` | `t.Trim()` | `t.strip()` |
| Trozo de texto | `Subcadena(t, 1, 3)` | `substr($t, 0, 3)` | `t.slice(0, 3)` | `t.Substring(0, 3)` | `t[0:3]` |
| Reemplazar | *(no existe)* | `str_replace(a, b, $t)` | `t.replace(a, b)` | `t.Replace(a, b)` | `t.replace(a, b)` |
| Separar | *(no existe)* | `explode(",", $t)` | `t.split(",")` | `t.Split(',')` | `t.split(",")` |

## 8. Objetos

| Concepto | PHP | JavaScript | C# | Python |
|---|---|---|---|---|
| Clase | `class Persona { }` | `class Persona { }` | `class Persona { }` | `class Persona:` |
| Constructor | `__construct()` | `constructor()` | `Persona()` | `__init__(self)` |
| El objeto actual | `$this->nombre` | `this.nombre` | `this.Nombre` | `self.nombre` |
| Crear un objeto | `new Persona()` | `new Persona()` | `new Persona()` | `Persona()` |
| Herencia | `extends` | `extends` | `:` | `class Hija(Padre):` |
| Llamar al padre | `parent::__construct()` | `super()` | `base()` | `super().__init__()` |
| Estático | `static` | `static` | `static` | `@staticmethod` |
| Privado | `private` | `#campo` | `private` | `_campo` *(convención)* |
| Abstracta | `abstract class` | *(no existe)* | `abstract class` | `ABC` + `@abstractmethod` |
| Interfaz | `interface` | *(no existe)* | `interface` | `ABC` o `Protocol` |
| Trait | `trait` + `use` | *(mixins)* | interfaz con método por defecto | mixin (herencia múltiple) |
| Namespace | `namespace A\B;` | módulos | `namespace A.B;` | carpeta `a/` + `b.py` |

PSeInt no tiene objetos: es un lenguaje estructurado.

## 9. Errores, archivos y depuración

| Concepto | PHP | JavaScript | C# | Python |
|---|---|---|---|---|
| Intentar | `try { }` | `try { }` | `try { }` | `try:` |
| Capturar | `catch (Exception $e)` | `catch (e)` | `catch (Exception e)` | `except Exception as e:` |
| Siempre | `finally { }` | `finally { }` | `finally { }` | `finally:` |
| Lanzar | `throw new Exception("…")` | `throw new Error("…")` | `throw new Exception("…")` | `raise Exception("…")` |
| Mensaje del error | `$e->getMessage()` | `e.message` | `e.Message` | `str(e)` |
| Leer un archivo | `file_get_contents($f)` | `fs.readFileSync(f)` | `File.ReadAllText(f)` | `Path(f).read_text()` |
| Escribir un archivo | `fopen($f, 'w')` | `fs.writeFileSync(f, t)` | `new StreamWriter(f)` | `open(f, "w")` |
| Cerrar solo | *(manual)* | *(manual)* | `using` | `with` |
| Ver una variable | `var_dump($x)` | `console.log(x)` | depurador | `print(f"{x=}")` · `type(x)` |
| Ver una estructura | `print_r($x)` | `console.table(x)` | depurador | `pprint(x)` |
| Detener el programa | `die("…")` | `process.exit()` | `Environment.Exit()` | `sys.exit("…")` |

En PSeInt los errores se evitaban validando antes con `Si` y `Repetir`, y la depuración se hacía con la prueba de escritorio y la ejecución paso a paso.

## 10. Web y base de datos

| Concepto | PHP | C# (ASP.NET Core) | Python (Flask) |
|---|---|---|---|
| Servidor | Apache (XAMPP) | Kestrel, dentro del programa | Flask, dentro del programa |
| Una página | un archivo `.php` | `app.MapGet("/ruta", …)` | `@app.route("/ruta")` |
| Dato por GET | `$_GET['x']` | `Request.Query["x"]` | `request.args.get("x")` |
| Dato por POST | `$_POST['x']` | `Request.Form["x"]` | `request.form.get("x")` |
| Archivo subido | `$_FILES['x']` | `Request.Form.Files` | `request.files.get("x")` |
| Cookie | `setcookie()` / `$_COOKIE` | `Response.Cookies` / `Request.Cookies` | `set_cookie()` / `request.cookies` |
| Sesión | `$_SESSION` | `HttpContext.Session` | `session` |
| Escapar HTML | `htmlspecialchars()` | `WebUtility.HtmlEncode()` | automático · `html.escape()` |
| Hash de contraseña | `password_hash()` | `Rfc2898DeriveBytes.Pbkdf2` | `hashlib.pbkdf2_hmac` |
| Base de datos | PDO | ADO.NET + MySqlConnector | DB-API: `sqlite3`, `mysql.connector` |
| Consulta segura | `prepare()` + `execute([$x])` | `MySqlCommand` + parámetros | `execute("… ?", (x,))` |

## 11. El mismo programa en los cinco lenguajes

**Factorial de 5.**

PSeInt:
```
Funcion resultado <- factorial(n)
    Definir resultado, i Como Entero;
    resultado <- 1;
    Para i <- 2 Hasta n Con Paso 1 Hacer
        resultado <- resultado * i;
    FinPara
FinFuncion

Algoritmo ejemplo
    Escribir "5! = ", factorial(5);
FinAlgoritmo
```

PHP:
```php
<?php
function factorial($n) {
    $resultado = 1;
    for ($i = 2; $i <= $n; $i++) {
        $resultado = $resultado * $i;
    }
    return $resultado;
}
echo "5! = " . factorial(5);
```

JavaScript:
```js
function factorial(n) {
    let resultado = 1;
    for (let i = 2; i <= n; i++) {
        resultado = resultado * i;
    }
    return resultado;
}
console.log("5! = " + factorial(5));
```

C#:
```csharp
static int Factorial(int n)
{
    int resultado = 1;
    for (int i = 2; i <= n; i++)
    {
        resultado = resultado * i;
    }
    return resultado;
}
Console.WriteLine("5! = " + Factorial(5));
```

Python:
```python
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado

print("5! =", factorial(5))
```

La lógica es idéntica en los cinco: un acumulador que empieza en 1 y un ciclo que lo multiplica. Solo cambia cómo se escribe.
