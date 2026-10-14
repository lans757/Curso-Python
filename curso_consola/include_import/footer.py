# Equivalente a footer.php: el pie de página, en su propio archivo.

from datetime import date


def mostrar_footer():
    print("--------------------------------------")
    print(f"(c) {date.today().year} Curso de Python")


if __name__ == "__main__":
    print("Probando footer.py por separado:")
    mostrar_footer()
