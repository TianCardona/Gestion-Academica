"""
Sistema de Gestión Académica - Programa principal.

Demuestra en un único proyecto las cinco fases de la actividad 1:
modelado, encapsulamiento, herencia, sobreescritura y polimorfismo.

Evolución Actividad Colaborativa N°2:
clases abstractas, composición y excepciones personalizadas.
"""

from modelos import (
    Administrativo,
    Asignatura,
    Docente,
    Estudiante,
    GrupoAcademico,
    Horario,
    ProgramaAcademico,
)
from modelos import excepciones


def mostrar_separador(titulo):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


def main():
    mostrar_separador("1. Creación de programas académicos y asignaturas")

    ingenieria_sistemas = ProgramaAcademico(
        codigo="IS001",
        nombre="Ingeniería de Sistemas",
        facultad="Ciencias e Ingenierías",
        numero_semestres=10,
    )
    administracion = ProgramaAcademico(
        codigo="AD001",
        nombre="Administración de Empresas",
        facultad="Ciencias Económicas",
        numero_semestres=8,
    )

    poo = Asignatura(
        codigo="PROG101",
        nombre="Programación Orientada a Objetos",
        creditos=4,
        programa=ingenieria_sistemas,
    )
    bases_datos = Asignatura(
        codigo="BD201",
        nombre="Bases de Datos",
        creditos=3,
        programa=ingenieria_sistemas,
    )
    contabilidad = Asignatura(
        codigo="CON110",
        nombre="Contabilidad General",
        creditos=3,
        programa=administracion,
    )

    ingenieria_sistemas.mostrar_informacion()
    administracion.mostrar_informacion()
    poo.mostrar_informacion()
    bases_datos.mostrar_informacion()
    contabilidad.mostrar_informacion()

    mostrar_separador("2. Creación de personas vinculadas (mínimo seis)")

    estudiante_1 = Estudiante(
        identificacion="1001",
        nombre="Ana Torres",
        correo="ana.torres@umanizales.edu.co",
        codigo_estudiantil="E2024001",
        programa=ingenieria_sistemas,
        semestre=3,
        promedio_acumulado=4.2,
    )
    estudiante_2 = Estudiante(
        identificacion="1002",
        nombre="Luis Gómez",
        correo="luis.gomez@umanizales.edu.co",
        codigo_estudiantil="E2024002",
        programa=administracion,
        semestre=5,
        promedio_acumulado=3.8,
    )

    docente_1 = Docente(
        identificacion="2001",
        nombre="María Restrepo",
        correo="maria.restrepo@umanizales.edu.co",
        numero_empleado="D-450",
        facultad="Ciencias e Ingenierías",
        tipo_contratacion="Tiempo completo",
        horas_semanales=20,
    )
    docente_2 = Docente(
        identificacion="2002",
        nombre="Carlos Pérez",
        correo="carlos.perez@umanizales.edu.co",
        numero_empleado="D-451",
        facultad="Ciencias Económicas",
        tipo_contratacion="Cátedra",
        horas_semanales=8,
    )

    administrativo_1 = Administrativo(
        identificacion="3001",
        nombre="Laura Mejía",
        correo="laura.mejia@umanizales.edu.co",
        numero_empleado="A-120",
        dependencia="Registro Académico",
        cargo="Coordinadora de matrículas",
        jornada="Diurna",
    )
    administrativo_2 = Administrativo(
        identificacion="3002",
        nombre="Andrés Salazar",
        correo="andres.salazar@umanizales.edu.co",
        numero_empleado="A-121",
        dependencia="Bienestar Universitario",
        cargo="Asistente administrativo",
        jornada="Mixta",
    )

    mostrar_separador("3. Consulta de información de los objetos")
    estudiante_1.mostrar_informacion()
    docente_1.mostrar_informacion()
    administrativo_1.mostrar_informacion()

    mostrar_separador("4. Modificación válida de datos encapsulados")
    print("Correo anterior de Ana:", estudiante_1.get_correo())
    estudiante_1.set_correo("ana.torres.nuevo@umanizales.edu.co")
    print("Correo actualizado de Ana:", estudiante_1.get_correo())

    print("Semestres anteriores de Ingeniería:", ingenieria_sistemas.get_numero_semestres())
    ingenieria_sistemas.set_numero_semestres(9)
    print("Semestres actualizados:", ingenieria_sistemas.get_numero_semestres())

    print("Créditos anteriores de POO:", poo.get_creditos())
    poo.set_creditos(5)
    print("Créditos actualizados de POO:", poo.get_creditos())

    mostrar_separador("5. Intentos de asignación de valores inválidos")
    print("Intento 1: correo vacío")
    estudiante_1.set_correo("")
    print("Intento 2: semestres menores o iguales a cero")
    administracion.set_numero_semestres(0)
    print("Intento 3: créditos menores o iguales a cero")
    bases_datos.set_creditos(-2)
    print("Los valores originales se conservan tras los intentos inválidos:")
    print("Correo de Ana:", estudiante_1.get_correo())
    print("Semestres de Administración:", administracion.get_numero_semestres())
    print("Créditos de Bases de Datos:", bases_datos.get_creditos())

    mostrar_separador("6. Presentación particular de cada tipo de persona")
    estudiante_2.mostrar_informacion()
    estudiante_2.realizar_actividad_principal()
    docente_2.mostrar_informacion()
    docente_2.realizar_actividad_principal()
    administrativo_2.mostrar_informacion()
    administrativo_2.realizar_actividad_principal()

    mostrar_separador("7. Recorrido polimórfico de la colección de personas")
    personas = [
        estudiante_1,
        estudiante_2,
        docente_1,
        docente_2,
        administrativo_1,
        administrativo_2,
    ]

    for persona in personas:
        persona.mostrar_informacion()
        persona.realizar_actividad_principal()
        print("-" * 70)

    # ==================== ACTIVIDAD COLABORATIVA N°2 ====================

    mostrar_separador("8. Evolución: Clases abstractas, composición y excepciones personalizadas")

    print("NOTA: La clase Persona ahora es ABSTRACTA (ABC).")
    print("No se puede instanciar directamente. Estudiante, Docente y Administrativo")
    print("deben implementar obligatoriamente realizar_actividad_principal().")
    print("Se demuestra a continuación con polimorfismo sobre los objetos creados.\n")

    # Composición: Crear Horario y asignarlo al GrupoAcadémico
    horario_poo = Horario(dia="Lunes / Miércoles", hora_inicio="08:00", hora_fin="10:00", aula="A-301")

    grupo_poo = GrupoAcademico(
        codigo_grupo="POO-G1",
        asignatura=poo,
        docente=docente_1,
        horario=horario_poo,  # COMPOSICIÓN: GrupoAcadémico TIENE un Horario
        cupo_maximo=2,
    )

    grupo_poo.mostrar_informacion_grupo()

    # Matrícula válida
    try:
        print("\n--- Intentando matricular estudiantes ---")
        grupo_poo.matricular(estudiante_1)
        grupo_poo.matricular(estudiante_2)
        grupo_poo.consultar_estudiantes()
    except excepciones.GestionAcademicaException as e:
        print("ERROR:", e)

    mostrar_separador("9. Pruebas con excepciones personalizadas (try/except)")

    # Crear un tercer estudiante para probar el cupo máximo
    estudiante_3 = Estudiante(
        identificacion="1003",
        nombre="Sofía Ramírez",
        correo="sofia.ramirez@umanizales.edu.co",
        codigo_estudiantil="E2024003",
        programa=ingenieria_sistemas,
        semestre=2,
        promedio_acumulado=4.0,
    )

    print("Prueba 1: Intentar matricular un tercer estudiante con cupo máximo = 2")
    try:
        grupo_poo.matricular(estudiante_3)
    except excepciones.CupoMaximoException as e:
        print("EXCEPCIÓN CAPTURADA [CupoMaximoException]:", e)
    except excepciones.GestionAcademicaException as e:
        print("EXCEPCIÓN CAPTURADA:", e)

    print("\nPrueba 2: Intentar matricular un estudiante ya matriculado")
    try:
        grupo_poo.matricular(estudiante_1)
    except excepciones.EstudianteYaMatriculadoException as e:
        print("EXCEPCIÓN CAPTURADA [EstudianteYaMatriculadoException]:", e)
    except excepciones.GestionAcademicaException as e:
        print("EXCEPCIÓN CAPTURADA:", e)

    print("\nPrueba 3: Retirar estudiante y volver a matricular")
    try:
        grupo_poo.retirar(estudiante_1)
        grupo_poo.consultar_estudiantes()
        grupo_poo.matricular(estudiante_1)
        grupo_poo.consultar_estudiantes()
    except excepciones.GestionAcademicaException as e:
        print("ERROR:", e)

    print("\nPrueba 4: Intentar retirar un estudiante NO matriculado")
    try:
        grupo_poo.retirar(estudiante_3)
    except excepciones.EstudianteNoMatriculadoException as e:
        print("EXCEPCIÓN CAPTURADA [EstudianteNoMatriculadoException]:", e)
    except excepciones.GestionAcademicaException as e:
        print("EXCEPCIÓN CAPTURADA:", e)

    mostrar_separador("10. Demostración final")
    print("Se evidencia:")
    print("- Clases abstractas: Persona es ABC con @abstractmethod")
    print("- Herencia: Estudiante/Docente/Administrativo heredan de Persona")
    print("- Composición: GrupoAcademico contiene un objeto Horario")
    print("- Sobreescritura y polimorfismo: métodos redefinidos por tipo")
    print("- Excepciones personalizadas: lanzadas, capturadas y tratadas con try/except")
    print("\n¡Evolución del Sistema de Gestión Académica completada con éxito!")


if __name__ == "__main__":
    main()
