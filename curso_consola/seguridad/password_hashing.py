# ============================================================================
# HASHING DE CONTRASEÑAS EN PYTHON
# ============================================================================
# Equivale a: seguridad/password_hashing.php · PasswordHashing.cs
#
# NUNCA se deben guardar contraseñas en texto plano. PHP resuelve esto con
# password_hash() / password_verify() (algoritmo bcrypt por defecto).
#
# Python no trae bcrypt en la biblioteca estándar (haría falta instalar el
# paquete "bcrypt"). Lo que SÍ viene incluido es PBKDF2, en el módulo
# hashlib: un algoritmo lento a propósito y resistente a fuerza bruta. Es el
# mismo que se usó en el curso de C#, y el que usa Django por defecto.
#
# Dos ideas clave:
# - SALT: un texto aleatorio que se mezcla con la contraseña. Hace que dos
#   usuarios con la misma clave tengan hashes distintos. No es secreto; se
#   guarda junto al hash.
# - UN SOLO SENTIDO: del hash no se puede volver a la contraseña. Para
#   verificar, se calcula el hash del intento y se compara.
# ============================================================================

import hashlib
import hmac
import secrets

TAMANO_SALT = 16
ITERACIONES = 100_000          # el guion bajo es solo para leer mejor el número


# Equivalente a password_hash($password, PASSWORD_DEFAULT)
def hash_password(password):
    salt = secrets.token_bytes(TAMANO_SALT)
    hash_bytes = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERACIONES)
    # Guardamos salt + hash juntos (separados por ':') para poder verificar después.
    return salt.hex() + ":" + hash_bytes.hex()


# Equivalente a password_verify($password, $hash)
def verify_password(password, guardado):
    salt_hex, hash_hex = guardado.split(":")
    salt = bytes.fromhex(salt_hex)
    hash_esperado = bytes.fromhex(hash_hex)
    hash_candidato = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERACIONES)
    # hmac.compare_digest compara en tiempo constante para evitar "timing
    # attacks", igual que hace password_verify() por dentro. No uses ==.
    return hmac.compare_digest(hash_candidato, hash_esperado)


password_usuario = "MiContrasenaSegura123"

print("1. Generando el hash (simulando el registro)")
# Genera un hash distinto cada vez, incluso para la misma contraseña (por el
# salt aleatorio), igual que password_hash().
hash_guardado_en_bd = hash_password(password_usuario)
print("Contraseña original:", password_usuario)
print("Hash generado (lo que guardamos en la base de datos):")
print(hash_guardado_en_bd)

print("\nEl mismo texto produce otro hash la segunda vez:")
print(hash_password(password_usuario))

print("\n2. Verificando la contraseña (simulando el login)")
intento_login1 = "123456"                     # contraseña incorrecta
intento_login2 = "MiContrasenaSegura123"      # contraseña correcta


def intentar_login(password, hash_guardado):
    if verify_password(password, hash_guardado):
        return "¡Contraseña correcta! Acceso concedido."
    return "Contraseña incorrecta."


print(f"Intento con '{intento_login1}':", intentar_login(intento_login1, hash_guardado_en_bd))
print(f"Intento con '{intento_login2}':", intentar_login(intento_login2, hash_guardado_en_bd))

print("\nNOTA IMPORTANTE:")
print('No necesitas "desencriptar" la contraseña. Solo necesitas verificar si coincide.')
print("PBKDF2, igual que bcrypt, es de un solo sentido (one-way).")

# ----------------------------------------------------------------------------
# Lo que NO se debe hacer: un hash rápido y sin salt
# md5 y sha256 "a secas" se calculan millones de veces por segundo, y la misma
# contraseña da siempre el mismo resultado: existen tablas ya calculadas.
# ----------------------------------------------------------------------------
print("\nMal ejemplo (no usar para contraseñas):")
print("sha256 de '123456':", hashlib.sha256("123456".encode()).hexdigest())
