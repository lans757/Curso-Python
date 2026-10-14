-- Base de datos de prueba: la misma tabla "usuarios" de los cursos de PHP y C#,
-- adaptada a SQLite (el motor que viene incluido en Python).
--
-- Diferencias con el prueba.sql original (MySQL / phpMyAdmin):
--   int(11) AUTO_INCREMENT + PRIMARY KEY  ->  INTEGER PRIMARY KEY AUTOINCREMENT
--   varchar(255)                          ->  TEXT
--
-- conexion.py ejecuta este archivo automáticamente. "IF NOT EXISTS" e
-- "INSERT OR IGNORE" permiten ejecutarlo muchas veces sin duplicar datos.

CREATE TABLE IF NOT EXISTS usuarios (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email  TEXT NOT NULL
);

INSERT OR IGNORE INTO usuarios (id, nombre, email) VALUES
    (1, 'Lans', 'lans@lans.com'),
    (2, 'luis', 'luis@luis.com');
