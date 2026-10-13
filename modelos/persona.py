"""Persona vinculada a la universidad (clase base)."""


class Persona:
    """Información común de cualquier integrante de la comunidad académica."""

    def __init__(self, identificacion, nombre, correo):
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = None
        self.set_correo(correo)

    def get_identificacion(self):
        return self._identificacion

    def get_nombre(self):
        return self._nombre

    def get_correo(self):
        return self._correo

    def set_nombre(self, nombre):
        if not str(nombre).strip():
            print("Error: el nombre no puede estar vacío.")
            return False
        self._nombre = nombre.strip()
        return True

    def set_correo(self, correo):
        """El correo electrónico no puede reemplazarse por una cadena vacía."""
        if correo is None or not str(correo).strip():
            print("Error: el correo electrónico no puede estar vacío.")
            return False
        self._correo = str(correo).strip()
        return True

    def mostrar_informacion(self):
        print(
            f"Persona | ID: {self._identificacion} | "
            f"Nombre: {self._nombre} | Correo: {self._correo}"
        )

    def realizar_actividad_principal(self):
        print(f"{self._nombre} forma parte de la comunidad universitaria.")
