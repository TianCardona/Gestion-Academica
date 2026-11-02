"""Paquete con las clases del Sistema de Gestión Académica."""

from .programa_academico import ProgramaAcademico
from .asignatura import Asignatura
from .persona import Persona
from .estudiante import Estudiante
from .docente import Docente
from .administrativo import Administrativo
from .horario import Horario
from .grupo_academico import GrupoAcademico
from . import excepciones

__all__ = [
    "ProgramaAcademico",
    "Asignatura",
    "Persona",
    "Estudiante",
    "Docente",
    "Administrativo",
    "Horario",
    "GrupoAcademico",
    "excepciones",
]

