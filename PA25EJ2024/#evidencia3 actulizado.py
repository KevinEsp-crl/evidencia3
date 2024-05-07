#evidencia3
import csv

class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones

    def imprimir_info(self):
        promedio = self.calcular_promedio()
        print("Matricula:", self.matricula)
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)
        print("Calificaciones:", self.calificaciones)
        print("Promedio:", promedio)

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

def agregar_alumno():
    matricula = input("Ingrese la matricula del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    calificaciones = [float(x) for x in input("Ingrese las calificaciones del alumno separadas por coma: ").split(',')]
    alumno = Alumno(matricula, nombre, carrera, calificaciones)
    guardar_alumno(alumno)

def guardar_alumno(alumno):
    with open('alumnos.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([alumno.matricula, alumno.nombre, alumno.carrera, *alumno.calificaciones])

def mostrar_info_alumno():
    matricula = input("Ingrese la matricula del alumno: ")
    with open('alumnos.csv', mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == matricula:
                alumno = Alumno(row[0], row[1], row[2], [float(x) for x in row[3:]])
                alumno.imprimir_info()
                break
        else:
            print("No se encontró ningún alumno con esa matrícula.")

def eliminar_alumno():
    matricula = input("Ingrese la matricula del alumno que desea eliminar: ")
    with open('alumnos.csv', mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)
    with open('alumnos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for row in rows:
            if row[0] != matricula:
                writer.writerow(row)
    print("Alumno eliminado correctamente.")

def mostrar_todos_los_alumnos():
    with open('alumnos.csv', mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            alumno = Alumno(row[0], row[1], row[2], [float(x) for x in row[3:]])
            alumno.imprimir_info()

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1.- Agregar Alumno")
        print("2.- Mostrar info del alumno")
        print("3.- Eliminar alumno")
        print("4.- Mostrar todos los alumnos")
        print("5.- Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            mostrar_info_alumno()
        elif opcion == '3':
            eliminar_alumno()
        elif opcion == '4':
            mostrar_todos_los_alumnos()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
