#!/bin/bash
set -e
cd "$(dirname "${BASH_SOURCE[0]}")"

# En Windows el comando suele ser "python" (o "py"); en Linux y macOS, "python3".
PYTHON="python"
if ! command -v python >/dev/null 2>&1; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
  elif command -v py >/dev/null 2>&1; then
    PYTHON="py"
  else
    echo "No se encontro Python. Instalalo desde https://www.python.org/downloads/"
    exit 1
  fi
fi

echo "Curso de Python — Fundamentos y logica"
echo "======================================="
echo "1) curso_consola  — menu interactivo (fundamentos, POO, errores, archivos...)"
echo "2) curso_web      — formularios, cookies, sesiones, subida de archivos (http://localhost:4050)"
echo "3) proyecto_final — sistema de inventario"
echo ""
read -p "Que quieres iniciar? [1/2/3]: " opcion

if [ "$opcion" = "2" ]; then
  cd curso_web
  if ! "$PYTHON" -c "import flask" >/dev/null 2>&1; then
    echo "Flask no esta instalado. Instalalo una sola vez con:"
    echo "    cd curso_web && $PYTHON -m pip install -r requirements.txt"
    exit 1
  fi
  "$PYTHON" app.py
elif [ "$opcion" = "3" ]; then
  cd proyecto_final
  "$PYTHON" inventario_bodega.py
else
  cd curso_consola
  "$PYTHON" menu.py
fi
