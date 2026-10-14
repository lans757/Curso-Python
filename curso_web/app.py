# ============================================================================
# CURSO DE PYTHON — MÓDULO WEB (Flask)
# ============================================================================
# Equivale a: los temas del curso de PHP que solo tienen sentido dentro de
# una petición HTTP (formularios/, cookies/, sesiones/, archivos/subir_archivo.php)
# y al proyecto CursoWeb del curso de C# (ASP.NET Core).
#
# En PHP el servidor web (Apache/XAMPP) está aparte y cada archivo .php es una
# página. En Python, como en C#, el servidor forma parte del programa: este
# archivo ES el servidor. Se usa Flask, un "microframework": lo mínimo para
# recibir peticiones y responderlas.
#
#   PHP                              Flask
#   ------------------------------   --------------------------------------
#   un archivo por página            una función por ruta: @app.route("/x")
#   $_GET['dato']                    request.args.get("dato")
#   $_POST['dato']                   request.form.get("dato")
#   $_FILES['archivo']               request.files.get("archivo")
#   setcookie() / $_COOKIE           respuesta.set_cookie() / request.cookies
#   session_start() / $_SESSION      session  (un diccionario)
#   htmlspecialchars()               automático en las plantillas {{ dato }}
#   header("Location: ...")          redirect(url_for("nombre_de_la_funcion"))
#
# Cómo ejecutarlo:
#   pip install -r requirements.txt
#   python app.py
#   abrir http://localhost:4050
# ============================================================================

import os
import re
from pathlib import Path

from flask import (Flask, make_response, redirect, render_template_string,
                   request, session, url_for)
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Las sesiones de Flask se guardan en una cookie FIRMADA con esta clave: el
# usuario puede verla, pero no modificarla sin que se note. En un proyecto
# real la clave va en una variable de entorno, nunca escrita en el código.
app.secret_key = os.environ.get("CLAVE_SECRETA", "clave-solo-para-el-curso")

CARPETA_SUBIDAS = Path(__file__).parent / "uploads"
EXTENSIONES_PERMITIDAS = {"jpg", "jpeg", "png", "gif", "pdf", "txt"}
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024       # tamaño máximo: 2 MB

# ----------------------------------------------------------------------------
# PLANTILLA BASE
# Es el equivalente de header.php + footer.php (include/require): todas las
# páginas se dibujan dentro de este marco. Para no repartir el curso en
# muchos archivos, las plantillas están aquí como textos; en un proyecto real
# irían en una carpeta templates/ y se usaría render_template().
#
# Jinja2 (el motor de plantillas de Flask) usa:
#   {{ dato }}        mostrar un valor (YA ESCAPADO contra XSS)
#   {% if %} {% for %} lógica dentro del HTML, como <?php if (...): ?>
# ----------------------------------------------------------------------------
BASE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ titulo }}</title>
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f4f7f6; color: #2c3e50;
         margin: 0; padding: 24px 16px; line-height: 1.6; }
  .contenedor { max-width: 640px; margin: 0 auto; background: #fff; padding: 28px;
                border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,.05); }
  h1, h2 { color: #2c3e50; border-bottom: 2px solid #3776ab; padding-bottom: 8px; }
  label { display: block; margin-top: 12px; font-weight: 600; }
  input, textarea { width: 100%; padding: 8px; margin-top: 4px; box-sizing: border-box;
                    border: 1px solid #ccd; border-radius: 6px; font: inherit; }
  button { margin-top: 16px; padding: 10px 18px; border: 0; border-radius: 6px;
           background: #3776ab; color: #fff; font: inherit; cursor: pointer; }
  .errores { background: #fdecea; color: #c0392b; padding: 10px 14px; border-radius: 6px; }
  .exito { background: #e8f8f0; color: #1e8449; padding: 10px 14px; border-radius: 6px; }
  .nota { background: #fef9e7; padding: 10px 14px; border-radius: 6px; font-size: .92em; }
  code { background: #eef; padding: 1px 5px; border-radius: 4px; }
  .caja { border: 1px dashed #aab; padding: 10px 14px; border-radius: 6px; margin: 8px 0; }
</style>
</head>
<body>
<div class="contenedor">
CONTENIDO
<p><a href="{{ url_for('indice') }}">Volver al índice</a></p>
</div>
</body>
</html>"""


def pagina(contenido, **datos):
    """Mete el contenido dentro de la plantilla base y la dibuja."""
    return render_template_string(BASE.replace("CONTENIDO", contenido), **datos)


# ----------------------------------------------------------------------------
# ÍNDICE
# ----------------------------------------------------------------------------
@app.route("/")
def indice():
    return pagina("""
        <h1>Curso de Python — Módulo web</h1>
        <p>Equivalente a los temas del curso de PHP que dependen de una petición HTTP.</p>
        <ul>
          <li><a href="{{ url_for('formularios') }}">Formularios</a> (formulario.php + recibir.php)</li>
          <li><a href="{{ url_for('cookies') }}">Cookies</a> (cookies/index.php + texto.php)</li>
          <li><a href="{{ url_for('sesiones') }}">Sesiones</a> (sesiones/index.php)</li>
          <li><a href="{{ url_for('subir_archivo') }}">Subir archivo</a> (archivos/subir_archivo.php)</li>
          <li><a href="{{ url_for('seguridad_xss') }}">Seguridad: XSS</a> (seguridad/sanitizacion_xss.php)</li>
        </ul>
    """, titulo="Curso de Python — Módulo web")


# ----------------------------------------------------------------------------
# FORMULARIOS
# PHP separaba la lógica (formulario.php), la vista (formulario.view.php) y
# el receptor (recibir.php) en tres archivos. Aquí una sola función atiende
# las dos peticiones: GET muestra el formulario y POST lo procesa.
# ----------------------------------------------------------------------------
PATRON_CORREO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.route("/formularios", methods=["GET", "POST"])
def formularios():
    nombre = ""
    correo = ""
    errores = []
    exito = None

    if request.method == "POST":
        # request.form es un diccionario con los campos enviados.
        # .get(campo, "") evita un error si el campo no llegó: es el
        # equivalente de isset($_POST['nombre']).
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()

        # 1. Validar el nombre (equivalente a !empty($_POST['nombre']))
        if not nombre:
            errores.append("Por favor ingresa un nombre")

        # 2. Validar el correo (equivalente a FILTER_VALIDATE_EMAIL)
        if not PATRON_CORREO.match(correo):
            errores.append("Por favor ingresa un correo válido")

        if not errores:
            # Simulación de envío exitoso, igual que en el original de PHP.
            exito = "¡Mensaje enviado correctamente!"
            nombre = ""
            correo = ""

    # Los valores {{ nombre }} y {{ correo }} se escapan solos: si alguien
    # escribe <script> en el formulario, se muestra como texto.
    return pagina("""
        <h2>Déjanos tus datos</h2>
        {% if errores %}
          <div class="errores">{% for error in errores %}{{ error }}<br>{% endfor %}</div>
        {% endif %}
        {% if exito %}<div class="exito">{{ exito }}</div>{% endif %}
        <form action="{{ url_for('formularios') }}" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" placeholder="Escribe tu nombre" value="{{ nombre }}">
            <label for="correo">Correo:</label>
            <input type="text" id="correo" name="correo" placeholder="ejemplo@correo.com" value="{{ correo }}">
            <button type="submit">Enviar datos</button>
        </form>
    """, titulo="Formulario de contacto", nombre=nombre, correo=correo, errores=errores, exito=exito)


# ----------------------------------------------------------------------------
# COOKIES
# Equivalente a cookies/index.php (setcookie) + cookies/texto.php ($_COOKIE).
# Una cookie es un dato pequeño que se guarda EN EL NAVEGADOR del usuario.
# ----------------------------------------------------------------------------
@app.route("/cookies")
def cookies():
    contenido = pagina("""
        <h2>Cookies</h2>
        <p class="exito">Se creó la cookie <code>usuario</code> con el valor <code>Carlos</code>.
           Dura 1 hora.</p>
        <p><a href="{{ url_for('cookies_texto') }}">Ir a la página que la lee</a></p>
        <p class="nota">La cookie viaja en la RESPUESTA. Por eso primero se arma la respuesta
           (<code>make_response</code>) y luego se le pega la cookie.</p>
    """, titulo="Cookies")

    respuesta = make_response(contenido)
    # setcookie('usuario', 'Carlos', time() + 3600) en PHP.
    # httponly=True impide que JavaScript lea la cookie (protege contra XSS).
    respuesta.set_cookie("usuario", "Carlos", max_age=3600, httponly=True, samesite="Lax")
    return respuesta


@app.route("/cookies/texto")
def cookies_texto():
    # $_COOKIE['usuario'] en PHP. Si no existe, devuelve None.
    usuario = request.cookies.get("usuario")
    return pagina("""
        <h2>Leyendo la cookie</h2>
        {% if usuario %}
          <p class="exito">Hola de nuevo, <strong>{{ usuario }}</strong>. Leí tu nombre de la cookie.</p>
        {% else %}
          <p class="errores">No hay ninguna cookie llamada <code>usuario</code>.
             <a href="{{ url_for('cookies') }}">Créala aquí</a>.</p>
        {% endif %}
        <p><a href="{{ url_for('cookies_borrar') }}">Borrar la cookie</a></p>
    """, titulo="Leyendo la cookie", usuario=usuario)


@app.route("/cookies/borrar")
def cookies_borrar():
    respuesta = make_response(redirect(url_for("cookies_texto")))
    respuesta.delete_cookie("usuario")
    return respuesta


# ----------------------------------------------------------------------------
# SESIONES
# Equivalente a sesiones/index.php, pagina2.php y cerrar.php.
# Una sesión guarda datos del usuario ENTRE una página y otra (por ejemplo,
# que ya inició sesión). "session" se usa como un diccionario, igual que
# $_SESSION; no hace falta llamar a session_start().
# ----------------------------------------------------------------------------
@app.route("/sesiones")
def sesiones():
    session["nombre"] = "Carlos"                      # $_SESSION['nombre'] = 'Carlos';
    session["visitas"] = session.get("visitas", 0) + 1
    return pagina("""
        <h2>Sesiones</h2>
        <p class="exito">Se guardó <code>nombre = {{ session['nombre'] }}</code> en la sesión.</p>
        <p>Has visitado esta página <strong>{{ session['visitas'] }}</strong> veces en esta sesión.</p>
        <p><a href="{{ url_for('sesiones_pagina2') }}">Ir a la página 2</a> ·
           <a href="{{ url_for('sesiones_cerrar') }}">Cerrar sesión</a></p>
    """, titulo="Sesiones")


@app.route("/sesiones/pagina2")
def sesiones_pagina2():
    # Esta página no recibe el nombre por ningún formulario ni enlace: lo
    # lee de la sesión. Si la sesión se cerró, .get() devuelve None.
    nombre = session.get("nombre")
    return pagina("""
        <h2>Página 2</h2>
        {% if nombre %}
          <p class="exito">Hola <strong>{{ nombre }}</strong>: te reconocí por la sesión.</p>
        {% else %}
          <p class="errores">No has iniciado sesión.
             <a href="{{ url_for('sesiones') }}">Iniciar</a>.</p>
        {% endif %}
        <p><a href="{{ url_for('sesiones_cerrar') }}">Cerrar sesión</a></p>
    """, titulo="Página 2", nombre=nombre)


@app.route("/sesiones/cerrar")
def sesiones_cerrar():
    session.clear()                                   # session_destroy() en PHP
    return redirect(url_for("sesiones_pagina2"))      # header('Location: ...')


# ----------------------------------------------------------------------------
# SUBIR ARCHIVOS
# Equivalente a archivos/subir_archivo.php ($_FILES + move_uploaded_file).
# ----------------------------------------------------------------------------
def extension_permitida(nombre_archivo):
    return "." in nombre_archivo and nombre_archivo.rsplit(".", 1)[1].lower() in EXTENSIONES_PERMITIDAS


@app.route("/archivos/subir", methods=["GET", "POST"])
def subir_archivo():
    error = None
    exito = None

    if request.method == "POST":
        archivo = request.files.get("archivo")          # $_FILES['archivo']

        if archivo is None or archivo.filename == "":
            error = "No seleccionaste ningún archivo."
        elif not extension_permitida(archivo.filename):
            error = "Tipo de archivo no permitido. Usa: " + ", ".join(sorted(EXTENSIONES_PERMITIDAS))
        else:
            # NUNCA se usa el nombre tal cual lo envía el usuario: podría
            # venir como "../../app.py" para sobrescribir otro archivo.
            # secure_filename() lo limpia y deja solo caracteres seguros.
            nombre_seguro = secure_filename(archivo.filename)
            CARPETA_SUBIDAS.mkdir(exist_ok=True)
            archivo.save(CARPETA_SUBIDAS / nombre_seguro)     # move_uploaded_file()
            exito = f"Archivo '{nombre_seguro}' subido correctamente a la carpeta uploads/."

    return pagina("""
        <h2>Subir archivos en Python</h2>
        {% if error %}<div class="errores">{{ error }}</div>{% endif %}
        {% if exito %}<div class="exito">{{ exito }}</div>{% endif %}
        <!-- enctype="multipart/form-data" es obligatorio para enviar archivos, igual que en PHP -->
        <form action="{{ url_for('subir_archivo') }}" method="post" enctype="multipart/form-data">
            <label for="archivo">Selecciona un archivo (máximo 2 MB):</label>
            <input type="file" id="archivo" name="archivo">
            <button type="submit">Subir archivo</button>
        </form>
        <p class="nota">Extensiones permitidas: {{ extensiones }}</p>
    """, titulo="Subir archivos", error=error, exito=exito,
        extensiones=", ".join(sorted(EXTENSIONES_PERMITIDAS)))


@app.errorhandler(413)
def archivo_muy_grande(_error):
    return pagina("""
        <h2>Archivo demasiado grande</h2>
        <p class="errores">El archivo supera el máximo de 2 MB.</p>
        <p><a href="{{ url_for('subir_archivo') }}">Intentar de nuevo</a></p>
    """, titulo="Archivo demasiado grande"), 413


# ----------------------------------------------------------------------------
# SEGURIDAD: XSS
# Equivalente a seguridad/sanitizacion_xss.php. Muestra el mismo comentario
# dos veces: escapado (lo normal en Flask) y sin escapar (con el filtro
# "safe", que es justo lo que NO hay que hacer con datos del usuario).
# ----------------------------------------------------------------------------
@app.route("/seguridad", methods=["GET", "POST"])
def seguridad_xss():
    comentario = request.form.get("comentario", "")
    return pagina("""
        <h2>Seguridad: prevención de XSS</h2>
        <p>Escribe HTML en el comentario, por ejemplo:
           <code>&lt;h1 style="color:red"&gt;HOLA&lt;/h1&gt;</code></p>
        <form action="{{ url_for('seguridad_xss') }}" method="post">
            <label for="comentario">Comentario:</label>
            <textarea id="comentario" name="comentario" rows="3">{{ comentario }}</textarea>
            <button type="submit">Enviar</button>
        </form>
        {% if comentario %}
          <h3>Con protección (así lo muestra Flask por defecto)</h3>
          <div class="caja">{{ comentario }}</div>
          <h3>Sin protección (filtro <code>safe</code>: peligroso)</h3>
          <div class="caja">{{ comentario | safe }}</div>
          <p class="nota">En el primer recuadro ves el texto tal cual lo escribiste. En el segundo,
             el navegador lo interpretó como HTML: un atacante podría ejecutar su propio código.</p>
        {% endif %}
    """, titulo="Seguridad: XSS", comentario=comentario)


if __name__ == "__main__":
    # debug=True recarga el servidor al guardar cambios y muestra los errores
    # en el navegador. Es solo para aprender: NUNCA se usa en un sitio real.
    app.run(port=4050, debug=True)
