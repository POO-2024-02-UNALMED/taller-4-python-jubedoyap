from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grupo 12" #Es un atributo de clase público (convención) para que al llamarlo desde el main se pueda imprimir

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]): #asignaturas y estudinates se crean como listas 
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes #Se declara el atributo como público (simbólicamente) ya que se accede desde el main 

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):#Es necesario poner el None, para que se trabaje con diferentes listas según el grupo
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo #De esta manera cuando se puede imprimir el atributo grupo de un objeto de tipo Grupo, cuando se llame 

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
