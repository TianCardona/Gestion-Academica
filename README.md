# Sistema de Gestión Académica

Este proyecto es la versión de un sistema universitario desarrollado en Python para la Actividad N.° 1 de Programación I (Universidad de Manizales). El proyecto es **un único sistema** que evoluciona a través de cinco fases: modelado, encapsulamiento, herencia, sobreescritura y polimorfismo.

## Integrantes

- Cristian Camilo Alzate Cardona - 1.192.726.014

## Descripción general

El sistema organiza información de la comunidad académica, los programas y las asignaturas:

- **Persona**: identificación, nombre y correo electrónico.
- **Estudiante**, **Docente** y **Administrativo**: especializan a `Persona` con datos y comportamientos propios.
- **ProgramaAcademico**: código, nombre, facultad y número de semestres.
- **Asignatura**: código, nombre, créditos y el programa al que pertenece.

Los atributos están encapsulados. Los cambios pasan por métodos que validan, entre otros, que el correo no quede vacío y que semestres y créditos sean mayores que cero.

## Estructura de archivos

```text
gestion-academica/
├── main.py                      # Punto de entrada y demostración de las 5 fases
├── README.md
├── .gitignore
└── modelos/
    ├── __init__.py
    ├── persona.py
    ├── estudiante.py
    ├── docente.py
    ├── administrativo.py
    ├── programa_academico.py
    └── asignatura.py
```



## Cómo ejecutar

Requisito: Python 3.10 o superior.

Desde la carpeta del proyecto:

```bash
python main.py
```

En algunos equipos de Windows puede ser:

```bash
py main.py
```

No se requieren librerías externas.

## Herencia, sobreescritura y polimorfismo

**Herencia.** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`. La identificación, el nombre, el correo y los métodos comunes se definen una sola vez. Cada subclase agrega solo lo que le es propio (código estudiantil, número de empleado, cargo, etc.).

**Sobreescritura.** Las tres subclases redefinen `mostrar_informacion()` y `realizar_actividad_principal()` con el mismo nombre, pero con un resultado distinto y coherente para cada rol.

**Polimorfismo.** En `main.py` se arma **una sola lista** con dos estudiantes, dos docentes y dos administrativos. Un **único ciclo** recorre esa colección e invoca los mismos métodos. Python ejecuta la versión correspondiente al tipo real del objeto. No hay `if`/`isinstance` por tipo, ni un ciclo por cada clase, ni llamadas manuales objeto por objeto.

## Uso de herramientas de inteligencia artificial

Se utilizó Cursor (asistente de código) como apoyo para:

- organizar la estructura del proyecto.
- verificar el esqueleto de las clases y el programa de demostración.
- revisar que las validaciones y el recorrido polimórfico cumplieran los criterios de la actividad.

Se comprende, se puede explicar y justificar las decisiones de diseño (encapsulamiento, herencia, sobreescritura y polimorfismo) y el código entregado.
