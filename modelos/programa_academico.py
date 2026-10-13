"""Programa académico de la universidad."""


class ProgramaAcademico:
    """Representa un programa de formación (pregrado, posgrado, etc.)."""

    def __init__(self, codigo, nombre, facultad, numero_semestres):
        self._codigo = codigo
        self._nombre = nombre
        self._facultad = facultad
        self._numero_semestres = None
        self.set_numero_semestres(numero_semestres)

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_facultad(self):
        return self._facultad

    def get_numero_semestres(self):
        return self._numero_semestres

    def set_nombre(self, nombre):
        if not str(nombre).strip():
            print("Error: el nombre del programa no puede estar vacío.")
            return False
        self._nombre = nombre.strip()
        return True

    def set_facultad(self, facultad):
        if not str(facultad).strip():
            print("Error: la facultad no puede estar vacía.")
            return False
        self._facultad = facultad.strip()
        return True

    def set_numero_semestres(self, numero_semestres):
        """El número de semestres debe ser mayor que cero."""
        try:
            valor = int(numero_semestres)
        except (TypeError, ValueError):
            print("Error: el número de semestres debe ser un entero mayor que cero.")
            return False
        if valor <= 0:
            print("Error: el número de semestres debe ser mayor que cero.")
            return False
        self._numero_semestres = valor
        return True

    def mostrar_informacion(self):
        print(
            f"Programa {self._codigo}: {self._nombre} | "
            f"Facultad: {self._facultad} | Semestres: {self._numero_semestres}"
        )
