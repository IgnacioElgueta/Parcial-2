def saludo (nombre):
    return "¡Hola!", nombre + "!"

mensaje = saludo("Estudiante: ")

nombre = input("Dime tu nombre: ")

print(f"{mensaje}, {nombre}")