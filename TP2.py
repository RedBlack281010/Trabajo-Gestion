class Estudiante:
    def __init__(self, matricula: str, nombre: str, apellido: str, carrera: str):
        self.setMatricula(matricula)
        self.__nombre = nombre
        self.apellido = apellido
        self.carrera = carrera
        self.cursos_inscritos: List['Curso'] = []

    def setMatricula(self, matricula: str):
        if matricula.isdigit() and len(matricula) < 6:
            self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def inscribirCurso(self, curso):
        self.cursos_inscritos.append(curso)

    def darDeBajaCurso(self, curso):
        if curso in self.cursos_inscritos:
            self.cursos_inscritos.remove(curso)

class Curso:
    def __init__(self, nombre_curso: str, codigo: str, profesor: str, capacidad: int):
        self.nombre_curso = nombre_curso
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes_inscritos: List[Estudiante] = []

    def estaDisponible(self):
        if len(self.estudiantes_inscritos) < self.capacidad:
            return True
        else:
            return False

    def inscribir_estudiante(self, estudiante: Estudiante):
        if self.estaDisponible():
            self.estudiantes_inscritos.append(estudiante)

    def dar_de_baja_estudiante(self, estudiante: Estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)


class Facultad:
    def __init__(self):
        self.estudiantes: List[Estudiante] = []
        self.cursos: List[Curso] = []

    def getEstudiante(self, matricula: str):
        for est in self.estudiantes:
            try:
                if est.getMatricula() == matricula:
                    return est
            except AttributeError:
                continue
        return None

    def getCurso(self, codigo: str):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def agregarEstudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        matricula = input("Ingrese la matricula (hasta 5 digitos numericos): ")
        carrera = input("Ingrese la carrera: ")
        estudiante_obj = Estudiante(matricula, nombre, apellido, carrera)
        self.estudiantes.append(estudiante_obj)
        print("Estudiante agregado correctamente.")

    def agregarCurso(self):
        nombre_curso = input("Ingrese el nombre del curso: ")
        codigo = input("Ingrese el codigo del curso: ")
        profesor = input("Ingrese el nombre del profesor a cargo: ")
        curso_existente = self.getCurso(codigo)
        if curso_existente:
            capacidad_extra = int(input("El curso ya existe. ¿Cuantas vacantes desea agregar?: "))
            curso_existente.capacidad += capacidad_extra
        else:
            capacidad = int(input("Ingrese la capacidad maxima del curso: "))
            curso_obj = Curso(nombre_curso, codigo, profesor, capacidad)
            self.cursos.append(curso_obj)
            print("Curso agregado correctamente.")

    def inscribirEstudianteEnCurso(self):
        matricula = input("Ingrese la matricula del estudiante: ")
        codigo = input("Ingrese el codigo del curso: ")
        estudiante = self.getEstudiante(matricula)
        if estudiante == None:
            print("El estudiante no existe o la matricula no es valida.")
            return False
        curso = self.getCurso(codigo)
        if curso == None:
            print("El curso no existe.")
            return False
        if curso.estaDisponible():
            curso.inscribir_estudiante(estudiante)
            estudiante.inscribirCurso(curso)
            print("Inscripcion realizada con exito.")
        else:
            print("No hay cupos disponibles en este curso.")

    def darDeBajaEstudianteDeCurso(self):
        matricula = input("Ingrese la matricula del estudiante: ")
        codigo = input("Ingrese el codigo del curso a dar de baja: ")
        estudiante = self.getEstudiante(matricula)
        curso = self.getCurso(codigo)
        if estudiante == None or curso == None:
            print("Datos incorrectos. Verifique la matricula y el codigo del curso.")
            return
        curso.dar_de_baja_estudiante(estudiante)
        estudiante.darDeBajaCurso(curso)
        print("El estudiante ha sido dado de baja del curso.")

    def consultarEstadoCursos(self):
        if not self.cursos:
            print("No hay cursos registrados.")
            return
        print("\nEstado de Cursos")
        for curso in self.cursos:
            inscritos = len(curso.estudiantes_inscritos)
            disponibles = curso.capacidad - inscritos
            print(f"Codigo: {curso.codigo} \nCurso: {curso.nombre_curso} \nProfesor: {curso.profesor} \nInscritos: {inscritos} \nCupos disponibles: {disponibles} \n")

    def consultarEstadoEstudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("\nEstado de Estudiantes")
        for x in self.estudiantes:
            nombre = x._Estudiante__nombre
            try:
                matricula = x.getMatricula()
            except AttributeError:
                matricula = "No registrada correctamente"
            print(f"Nombre: {nombre} {x.apellido} \nMatricula: {matricula} \nCarrera: {x.carrera}")
            print("Cursos inscritos:")
            if not x.cursos_inscritos:
                print(" - Ningun curso inscrito.")
            else:
                for curso in x.cursos_inscritos:
                    print(f" - {curso.nombre_curso} (Codigo: {curso.codigo})")

def main():
    facultad = Facultad()
    while True:
        opcion = menu()
        if opcion == "7":
            break
        elif opcion == "1":
            facultad.agregarEstudiante()
        elif opcion == "2":
            facultad.agregarCurso()
        elif opcion == "3":
            facultad.inscribirEstudianteEnCurso()
        elif opcion == "4":
            facultad.darDeBajaEstudianteDeCurso()
        elif opcion == "5":
            facultad.consultarEstadoCursos()
        elif opcion == "6":
            facultad.consultarEstadoEstudiantes()
    print("Programa Terminado")

def menu():
    print("\nSistema de Facultad")
    print("1- Registrar Estudiante")
    print("2- Registrar Curso")
    print("3- Inscribir Estudiante a Curso")
    print("4- Dar de baja Estudiante de Curso")
    print("5- Consultar Estado de Cursos")
    print("6- Consultar Estado de Estudiantes")
    print("7- Salir")
    return input("Seleccione una opcion: ")
    
main()
