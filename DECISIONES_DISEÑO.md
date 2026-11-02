# Documento de Decisiones de Diseño - Actividad Colaborativa N°2

## Proyecto: Sistema de Gestión Académica
**Repositorio:** https://github.com/TianCardona/Gestion-Academica  
**Rama:** cursor/sistema-gestion-academica

## 1. Clases Abstractas

**Decisión:** Convertir la clase `Persona` en una clase abstracta utilizando `abc.ABC` y el decorador `@abstractmethod`.

**Justificación:**
- `Persona` representa un concepto genérico de la comunidad universitaria, no tiene sentido instanciar un objeto "Persona" sin un rol específico (Estudiante, Docente o Administrativo).
- Al declarar `realizar_actividad_principal()` como método abstracto, obligamos a todas las clases hijas a implementarlo, garantizando que cada tipo de persona defina su propia actividad principal.
- Se mantiene la lógica de encapsulamiento y herencia ya desarrollada en la Actividad N°1.

**Implementación:** `modelos/persona.py`

## 2. Composición

**Decisión:** Crear la clase `Horario` de forma independiente y componerla dentro de `GrupoAcademico` mediante el atributo `self._horario`.

**Justificación:**
- Un `GrupoAcademico` **"tiene"** un `Horario`, no **"es"** un `Horario`. Por ello se utiliza **composición**, no herencia.
- Esto permite reutilizar la clase `Horario` si en el futuro se necesita en otros contextos.
- La relación queda clara: el grupo agrupa `Asignatura`, `Docente`, `Horario` y una lista de `Estudiante`.

**Implementación:** `modelos/horario.py` y `modelos/grupo_academico.py`

## 3. Excepciones Personalizadas

**Decisión:** Crear una jerarquía de excepciones con `GestionAcademicaException` como clase base.

**Excepciones implementadas:**
- `CupoMaximoException`: Se lanza al intentar matricular cuando ya se alcanzó el cupo máximo del grupo.
- `EstudianteYaMatriculadoException`: Se lanza al intentar matricular un estudiante que ya se encuentra en la lista.
- `EstudianteNoMatriculadoException`: Se lanza al intentar retirar un estudiante que no está matriculado.
- `DatosInvalidosException`: Excepción base para futuras validaciones de datos.

**Justificación:**
- Permiten dar mensajes de error claros y específicos al usuario.
- Facilitan el control de flujo con `try/except` diferenciando cada tipo de error.
- Siguen el principio de POO: crear errores propios acorde al dominio del problema (Sistema de Gestión Académica).

**Implementación:** `modelos/excepciones.py`, `modelos/grupo_academico.py` y `main.py`

## 4. Matrícula, Retiro y Consulta

**Decisión:** Implementar los métodos `matricular()`, `retirar()` y `consultar_estudiantes()` en `GrupoAcademico`.

**Justificación:**
- `matricular()`: Valida duplicados por identificación y verifica el cupo antes de agregar al estudiante.
- `retirar()`: Busca al estudiante por identificación y lo elimina de la lista, lanzando excepción si no existe.
- `consultar_estudiantes()`: Muestra de forma ordenada los estudiantes matriculados con su información relevante.

## 5. Coherencia con la Actividad N°1

**Decisión:** Mantener todo el código de la Actividad Colaborativa N°1 intacto (herencia, encapsulamiento, sobreescritura, polimorfismo).

**Justificación:**
- Se trata de una **evolución**, no de un sistema nuevo.
- Se ampliaron las funcionalidades sin reemplazar las clases ni la lógica ya desarrollada.
- El recorrido polimórfico con una única lista sigue presente tal como se pidió en la actividad anterior.

## Conclusión

La solución integra correctamente clases abstractas, composición y excepciones personalizadas, cumpliendo con los requerimientos de la Actividad Colaborativa N°2. Además, se conserva la estructura, organización y filosofía del proyecto original.
