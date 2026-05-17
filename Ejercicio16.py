nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0

print("\n======Calificacion de notas======")

while True:

    print("\nAsignaturas Registradas")
    
    print("1. Matematicas")
    print("2. Fundamentos de programacion")
    print("3. Inteligencia artificial")
    print("4. Devops")
    print("5. Ciencia de datos")
    print("6. ¿Quiere terminar la seleccion de notas?")

    try:
        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            nota1 = float(input("Ingrese nota de matematicas: "))

        elif opcion == 2:
            nota2 = float(input("Ingrese nota de Fundamentos de programacion: "))

        elif opcion == 3:
            nota3 = float(input("Ingrese nota de Inteligencia artificial: "))

        elif opcion == 4:
            nota4 = float(input("Ingrese nota de Devops: "))

        elif opcion == 5:
            nota5 = float(input("Ingrese nota de Ciencia de datos: "))
        
        elif opcion == 6:
            break
        else:
            print("Selecciona una opcion del 1 al 6")

    except:
        print("Ingrese un numero valido")
    

print("Calificaciones")

print("Matematicas: ", nota1)
print("Fundamentos de programacion: ", nota2)
print("Inteligencia artificial: ", nota3)
print("Devops: ", nota4)
print("Ciencia de datos: ", nota5)

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Promedio de las notas: ", promedio)

if promedio < 4:
    print("Reprobado")

elif promedio >= 4:
    print("Aprobado")
