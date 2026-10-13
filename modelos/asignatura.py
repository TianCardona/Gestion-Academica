"""Asignatura asociada a un programa académico."""


class Asignatura:
    """Materia que pertenece a un programa académico."""

    def __init__(self, codigo, nombre, creditos, programa):
        self._codigo = codigo
        self._nombre = nombre
        self._creditos = None
        self._programa = programa
        self.set_creditos(creditos)

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_creditos(self):
        return self._creditos

    def get_programa(self):
        return self._programa

    def set_nombre(self, nombre):
        if not str(nombre).strip():
            print("Error: el nombre de la asignatura no puede estar vacío.")
            return False
        self._nombre = nombre.strip()
        return True

    def set_creditos(self, creditos):
        """El número de créditos debe ser mayor que cero."""
        try:
            valor = int(creditos)
        except (TypeError, ValueError):
            print("Error: el número de créditos debe ser un entero mayor que cero.")
            return False
        if valor <= 0:
            print("Error: el número de créditos debe ser mayor que cero.")
            return False
        self._creditos = valor
        return True

    def set_programa(self, programa):
        if programa is None:
            print("Error: la asignatura debe pertenecer a un programa académico.")
            return False
        self._programa = programa
        return True

    def mostrar_informacion(self):
        nombre_programa = self._programa.get_nombre() if self._programa else "Sin programa"
        print(
            f"Asignatura {self._codigo}: {self._nombre} | "
            f"Créditos: {self._creditos} | Programa: {nombre_programa}"
        )
