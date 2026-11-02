"""Excepciones personalizadas para el Sistema de Gestión Académica."""


class GestionAcademicaException(Exception):
    """Excepción base del sistema."""
    pass


class CupoMaximoException(GestionAcademicaException):
    """Se lanza cuando se intenta matricular un estudiante y el cupo está lleno."""
    pass


class EstudianteYaMatriculadoException(GestionAcademicaException):
    """Se lanza cuando el estudiante ya se encuentra matriculado en el grupo."""
    pass


class EstudianteNoMatriculadoException(GestionAcademicaException):
    """Se lanza cuando se intenta retirar un estudiante que no está matriculado."""
    pass


class DatosInvalidosException(GestionAcademicaException):
    """Se lanza cuando se detectan datos inválidos al crear objetos."""
    pass
