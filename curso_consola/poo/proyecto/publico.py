# Namespace para el área Pública: misma clase "Persona", módulo distinto.
# Su ruta completa es proyecto.publico.Persona, así que no choca con
# proyecto.admin.Persona.


class Persona:
    def saludar(self):
        return "Hola, soy un visitante normal."
