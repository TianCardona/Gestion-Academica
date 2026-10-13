"""Paquete con las clases del Sistema de Gestión Académica."""

from .programa_academico import ProgramaAcademico
from .asignatura import Asignatura
from .persona import Persona
from .estudiante import Estudiante
from .docente import Docente
from .administrativo import Administrativo

__all__ = [
    "ProgramaAcademico",
    "Asignatura",
    "Persona",
    "Estudiante",
    "Docente",
    "Administrativo",
]
