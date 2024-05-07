class Alumno:
    def __init__(self, matricula, nombre, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def info(self):
        print("Matricula:", self.matricula)
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)
        print("Calificaciones:", self.calificaciones)
        print("Promedio:", self.promedio())


class AdminAlumnos:
    alumnos = []

    @classmethod
    def agregar_alumno(cls, nuevo_alumno):
        for alumno in cls.alumnos:
            if alumno.matricula == nuevo_alumno.matricula:
                print("La matricula ya existe. No se puede agregar el alumno.")
                return
        cls.alumnos.append(nuevo_alumno)

    @classmethod
    def buscar_alumno(cls, matricula):
        for alumno in cls.alumnos:
            if alumno.matricula == matricula:
                return alumno
        print("Alumno no encontrado.")
        return None

    @classmethod
    def modificar_alumno(cls, matricula, datos_nuevos):
        alumno = cls.buscar_alumno(matricula)
        if alumno:
            alumno.nombre = datos_nuevos.get("nombre", alumno.nombre)
            alumno.carrera = datos_nuevos.get("carrera", alumno.carrera)
            alumno.calificaciones = datos_nuevos.get("calificaciones", alumno.calificaciones)

    @classmethod
    def eliminar_alumno(cls, matricula):
        alumno = cls.buscar_alumno(matricula)
        if alumno:
            cls.alumnos.remove(alumno)
            print("Alumno eliminado.")
        else:
            print("Alumno no encontrado.")

    @classmethod
    def mostrar_todos(cls):
        if not cls.alumnos:
            print("No hay alumnos registrados.")
        else:
            for alumno in cls.alumnos:
                alumno.info()


 
while True:
    print("\nMenú:")
    print("1. Agregar Alumno")
    print("2. Buscar Alumno")
    print("3. Modificar datos alumno")
    print("4. Eliminar Alumno")
    print("5. Mostrar todos los alumnos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        matricula = input("Ingrese la matrícula del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        carrera = input("Ingrese la carrera del alumno: ")
        nuevo_alumno = Alumno(matricula, nombre, carrera)
        AdminAlumnos.agregar_alumno(nuevo_alumno)

    elif opcion == "2":
        matricula = input("Ingrese la matrícula del alumno a buscar: ")
        alumno_encontrado = AdminAlumnos.buscar_alumno(matricula)
        if alumno_encontrado:
            alumno_encontrado.info()

    elif opcion == "3":
        matricula = input("Ingrese la matrícula del alumno a modificar: ")
        nombre = input("Ingrese el nuevo nombre del alumno (dejar en blanco para mantener el actual): ")
        carrera = input("Ingrese la nueva carrera del alumno (dejar en blanco para mantener la actual): ")
        calificaciones = input("Ingrese las nuevas calificaciones del alumno (separadas por coma): ")
        datos_nuevos = {"nombre": nombre, "carrera": carrera, "calificaciones": [float(cal) for cal in calificaciones.split(",") if cal.strip()]}
        AdminAlumnos.modificar_alumno(matricula, datos_nuevos)

    elif opcion == "4":
        matricula = input("Ingrese la matrícula del alumno a eliminar: ")
        AdminAlumnos.eliminar_alumno(matricula)

    elif opcion == "5":
        AdminAlumnos.mostrar_todos()

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
