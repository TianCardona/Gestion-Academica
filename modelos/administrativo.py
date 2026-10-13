"""Personal administrativo de la universidad."""

from .persona import Persona


class Administrativo(Persona):
    """Persona que desempeña un cargo en una dependencia institucional."""

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        numero_empleado,
        dependencia,
        cargo,
        jornada,
    ):
        super().__init__(identificacion, nombre, correo)
        self._numero_empleado = numero_empleado
        self._dependencia = dependencia
        self._cargo = cargo
        self._jornada = jornada

    def get_numero_empleado(self):
        return self._numero_empleado

    def get_dependencia(self):
        return self._dependencia

    def get_cargo(self):
        return self._cargo

    def get_jornada(self):
        return self._jornada

    def set_cargo(self, cargo):
        if not str(cargo).strip():
            print("Error: el cargo no puede estar vacío.")
            return False
        self._cargo = cargo.strip()
        return True

    def set_dependencia(self, dependencia):
        if not str(dependencia).strip():
            print("Error: la dependencia no puede estar vacía.")
            return False
        self._dependencia = dependencia.strip()
        return True

    def mostrar_informacion(self):
        print(
            f"Administrativo | ID: {self._identificacion} | Nombre: {self._nombre} | "
            f"Correo: {self._correo} | Empleado: {self._numero_empleado} | "
            f"Dependencia: {self._dependencia} | Cargo: {self._cargo} | "
            f"Jornada: {self._jornada}"
        )

    def realizar_actividad_principal(self):
        print(
            f"{self._nombre} desempeña el cargo de {self._cargo} "
            f"en {self._dependencia}."
        )
