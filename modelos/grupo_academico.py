"""Grupo académico con matrícula, retiro y consulta de estudiantes."""

from .excepciones import (
    CupoMaximoException,
    EstudianteNoMatriculadoException,
    EstudianteYaMatriculadoException,
)


class GrupoAcademico:
    """Agrupa estudiantes para una asignatura con docente, horario y cupo."""

    def __init__(self, codigo_grupo, asignatura, docente, horario, cupo_maximo):
        self._codigo_grupo = codigo_grupo
        self._asignatura = asignatura
        self._docente = docente
        self._horario = horario  # Composición: el grupo TIENE un horario
        self._cupo_maximo = int(cupo_maximo)
        self._estudiantes = []

    def get_codigo_grupo(self):
        return self._codigo_grupo

    def get_asignatura(self):
        return self._asignatura

    def get_docente(self):
        return self._docente

    def get_horario(self):
        return self._horario

    def get_cupo_maximo(self):
        return self._cupo_maximo

    def get_estudiantes(self):
        return list(self._estudiantes)

    def matricular(self, estudiante):
        """Matricula un estudiante validando cupo y duplicados."""
        # Validar si ya está matriculado
        for est in self._estudiantes:
            if est.get_identificacion() == estudiante.get_identificacion():
                raise EstudianteYaMatriculadoException(
                    f"El estudiante {estudiante.get_nombre()} ya se encuentra matriculado en el grupo {self._codigo_grupo}."
                )

        # Validar cupo máximo
        if len(self._estudiantes) >= self._cupo_maximo:
            raise CupoMaximoException(
                f"No hay cupo disponible en el grupo {self._codigo_grupo}. Cupo máximo: {self._cupo_maximo}."
            )

        self._estudiantes.append(estudiante)
        print(
            f"Matrícula exitosa: {estudiante.get_nombre()} fue matriculado en "
            f"{self._asignatura.get_nombre()} ({self._codigo_grupo})."
        )
        return True

    def retirar(self, estudiante):
        """Retira un estudiante del grupo."""
        for i, est in enumerate(self._estudiantes):
            if est.get_identificacion() == estudiante.get_identificacion():
                self._estudiantes.pop(i)
                print(
                    f"Retiro exitoso: {estudiante.get_nombre()} fue retirado del grupo {self._codigo_grupo}."
                )
                return True

        raise EstudianteNoMatriculadoException(
            f"El estudiante {estudiante.get_nombre()} no se encuentra matriculado en el grupo {self._codigo_grupo}."
        )

    def consultar_estudiantes(self):
        """Muestra la lista de estudiantes matriculados."""
        print(
            f"\nEstudiantes matriculados en grupo {self._codigo_grupo} - {self._asignatura.get_nombre()}"
        )
        if not self._estudiantes:
            print("No hay estudiantes matriculados.")
            return

        for idx, est in enumerate(self._estudiantes, 1):
            print(
                f"{idx}. {est.get_nombre()} | Código: {est.get_codigo_estudiantil()} | ID: {est.get_identificacion()}"
            )

    def mostrar_informacion_grupo(self):
        print("\n" + "=" * 70)
        print(f"INFORMACIÓN DEL GRUPO ACADÉMICO - {self._codigo_grupo}")
        print("=" * 70)
        print(f"Asignatura: {self._asignatura.get_nombre()} ({self._asignatura.get_codigo()})")
        print(f"Docente: {self._docente.get_nombre()} | {self._docente.get_correo()}")
        print(f"Horario: {self._horario}")
        print(f"Cupo: {len(self._estudiantes)}/{self._cupo_maximo} estudiantes matriculados")
