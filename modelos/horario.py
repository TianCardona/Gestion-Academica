"""Horario para un grupo académico."""


class Horario:
    """Representa el día, hora de inicio, hora fin y aula de un grupo."""

    def __init__(self, dia, hora_inicio, hora_fin, aula):
        self._dia = dia
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
        self._aula = aula

    def get_dia(self):
        return self._dia

    def get_hora_inicio(self):
        return self._hora_inicio

    def get_hora_fin(self):
        return self._hora_fin

    def get_aula(self):
        return self._aula

    def set_aula(self, aula):
        if not str(aula).strip():
            print("Error: el aula no puede estar vacía.")
            return False
        self._aula = aula.strip()
        return True

    def mostrar_horario(self):
        print(f"Horario: {self._dia} | {self._hora_inicio} - {self._hora_fin} | Aula: {self._aula}")

    def __str__(self):
        return f"{self._dia} {self._hora_inicio}-{self._hora_fin} (Aula {self._aula})"
