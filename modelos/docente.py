"""Docente de la universidad."""

from .persona import Persona


class Docente(Persona):
    """Persona que orienta clases en una facultad."""

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        numero_empleado,
        facultad,
        tipo_contratacion,
        horas_semanales,
    ):
        super().__init__(identificacion, nombre, correo)
        self._numero_empleado = numero_empleado
        self._facultad = facultad
        self._tipo_contratacion = tipo_contratacion
        self._horas_semanales = horas_semanales

    def get_numero_empleado(self):
        return self._numero_empleado

    def get_facultad(self):
        return self._facultad

    def get_tipo_contratacion(self):
        return self._tipo_contratacion

    def get_horas_semanales(self):
        return self._horas_semanales

    def set_facultad(self, facultad):
        if not str(facultad).strip():
            print("Error: la facultad no puede estar vacía.")
            return False
        self._facultad = facultad.strip()
        return True

    def set_horas_semanales(self, horas):
        try:
            valor = int(horas)
        except (TypeError, ValueError):
            print("Error: las horas semanales deben ser un entero mayor que cero.")
            return False
        if valor <= 0:
            print("Error: las horas semanales deben ser mayores que cero.")
            return False
        self._horas_semanales = valor
        return True

    def mostrar_informacion(self):
        print(
            f"Docente | ID: {self._identificacion} | Nombre: {self._nombre} | "
            f"Correo: {self._correo} | Empleado: {self._numero_empleado} | "
            f"Facultad: {self._facultad} | Contratación: {self._tipo_contratacion} | "
            f"Horas semanales: {self._horas_semanales}"
        )

    def realizar_actividad_principal(self):
        print(f"{self._nombre} orienta clases en la facultad de {self._facultad}.")
