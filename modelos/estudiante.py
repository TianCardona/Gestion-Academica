"""Estudiante de la universidad."""

from .persona import Persona


class Estudiante(Persona):
    """Persona que cursa un programa académico."""

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        codigo_estudiantil,
        programa,
        semestre,
        promedio_acumulado,
    ):
        super().__init__(identificacion, nombre, correo)
        self._codigo_estudiantil = codigo_estudiantil
        self._programa = programa
        self._semestre = semestre
        self._promedio_acumulado = promedio_acumulado

    def get_codigo_estudiantil(self):
        return self._codigo_estudiantil

    def get_programa(self):
        return self._programa

    def get_semestre(self):
        return self._semestre

    def get_promedio_acumulado(self):
        return self._promedio_acumulado

    def set_semestre(self, semestre):
        try:
            valor = int(semestre)
        except (TypeError, ValueError):
            print("Error: el semestre debe ser un entero mayor que cero.")
            return False
        if valor <= 0:
            print("Error: el semestre debe ser mayor que cero.")
            return False
        self._semestre = valor
        return True

    def set_promedio_acumulado(self, promedio):
        try:
            valor = float(promedio)
        except (TypeError, ValueError):
            print("Error: el promedio acumulado debe ser un número entre 0.0 y 5.0.")
            return False
        if valor < 0.0 or valor > 5.0:
            print("Error: el promedio acumulado debe estar entre 0.0 y 5.0.")
            return False
        self._promedio_acumulado = valor
        return True

    def mostrar_informacion(self):
        nombre_programa = self._programa.get_nombre() if self._programa else "Sin programa"
        print(
            f"Estudiante | ID: {self._identificacion} | Nombre: {self._nombre} | "
            f"Correo: {self._correo} | Código: {self._codigo_estudiantil} | "
            f"Programa: {nombre_programa} | Semestre: {self._semestre} | "
            f"Promedio: {self._promedio_acumulado}"
        )

    def realizar_actividad_principal(self):
        nombre_programa = self._programa.get_nombre() if self._programa else "un programa"
        print(
            f"{self._nombre} cursa {nombre_programa} y se encuentra en el "
            f"semestre {self._semestre}."
        )
