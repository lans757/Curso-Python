# ============================================================================
# SEGURIDAD: PREVENCIÓN DE XSS (Cross-Site Scripting) EN PYTHON
# ============================================================================
# Equivale a: seguridad/sanitizacion_xss.php · SanitizacionXss.cs
#
# El ataque XSS ocurre cuando alguien malintencionado inyecta HTML o
# JavaScript (por ejemplo, en un comentario o un formulario) y ese código se
# ejecuta en el navegador de otros usuarios.
#
# SOLUCIÓN: siempre "escapar" los datos antes de mostrarlos en una página.
#   PHP:     htmlspecialchars($texto)
#   C#:      WebUtility.HtmlEncode(texto)
#   Python:  html.escape(texto)
#
# El ejemplo real con un formulario web está en curso_web/ (ruta /formularios).
# Aquí simulamos el dato "recibido" para ver la diferencia.
# ============================================================================

import html

# Simulamos que esto llegó de un formulario (igual que $_POST['comentario'])
input_usuario = "<script>alert('HACKEADO')</script> Hola, este es mi comentario"

print("Intenta escribir código HTML o JS en un formulario real.")
print("Ejemplo malicioso: <h1 style=\"color:red\">HOLA</h1> o <script>alert('XSS')</script>\n")

# 1. DATO INSEGURO (tal cual llega)
# Si esto se imprimiera directo en una página web, el navegador interpretaría
# las etiquetas y ejecutaría el script.
comentario_sin_limpiar = input_usuario

# 2. DATO SEGURO (sanitizado)
# Convierte los caracteres especiales en entidades HTML:
#   <  se convierte en  &lt;       >  se convierte en  &gt;
#   &  se convierte en  &amp;      "  se convierte en  &quot;
# Así el navegador solo MUESTRA el texto; no lo ejecuta.
comentario_limpio = html.escape(input_usuario)

print("Resultado SIN protección (inseguro):")
print(comentario_sin_limpiar)

print("\nResultado CON protección (sanitizado):")
print(comentario_limpio)

# ----------------------------------------------------------------------------
# El camino inverso (por si necesitas recuperar el texto original)
# ----------------------------------------------------------------------------
print("\nDe vuelta al original con html.unescape():")
print(html.unescape(comentario_limpio))

# ----------------------------------------------------------------------------
# En la práctica casi nunca se llama html.escape() a mano: los motores de
# plantillas de Flask y Django (Jinja2) escapan TODO automáticamente. El
# peligro aparece cuando alguien desactiva ese escape a propósito (el filtro
# "|safe") con un dato que vino del usuario.
#
# La otra inyección clásica es la de SQL: se evita con consultas
# parametrizadas. Ver conexion/conexion.py.
# ----------------------------------------------------------------------------
