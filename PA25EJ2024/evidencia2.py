class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        pass

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Leon(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "León")

    def hacer_sonido(self):
        return "¡Rugido!"


class Tigre(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Tigre")

    def hacer_sonido(self):
        return "¡Rugido de tigre!"


class Oso(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Oso")

    def hacer_sonido(self):
        return "¡Gruñido!"


def agregar_animal(zoo):
    print("¿Qué animal quieres agregar?")
    print("1. León")
    print("2. Tigre")
    print("3. Oso")
    opcion = input("Selecciona una opción: ")

    nombre = input("Introduce el nombre del animal: ")

    if opcion in {"1", "2", "3"}:
        if opcion == "1":
            animal = Leon(nombre)
        elif opcion == "2":
            animal = Tigre(nombre)
        else:
            animal = Oso(nombre)

        zoo.append(animal)
        print(f"{animal.nombre} ha sido agregado al mini-zoo.")
    else:
        print("Opción no válida.")


def ver_animales(zoo):
    if not zoo:
        print("No hay animales en el mini-zoo.")
    else:
        print("Animales en el mini-zoo:")
        for animal in zoo:
            print(animal)


def main():
    zoo = []

    while True:
        print("\nOpciones del programa:")
        print("1. Agregar animal")
        print("2. Ver todos los animales del mini-zoo")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_animal(zoo)
        elif opcion == "2":
            ver_animales(zoo)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
