from random import randint

num1 = int(input("Ingresa limite inferior: "))
num2 = int(input("Ingresa limite superior: "))

while num1 >= num2:
    print("Error, El limite inferior debe ser menor al supeior")

    num1 = int(input)("Ingresa limite inferior: ")
    num2 = int(input)("Ingresa limite superior: ")

    # numero aleatorio.

numero = randint(num1, num2)

# ajuste en multiplo de 3

omegalul = (numero // 3) * 3


if omegalul < num1:
    omegalul = num1

    # Intento 1
intento1 = int(input("Intenta adivinar: "))

if intento1 == omegalul:
    print("Felicitaciones, adivinó en su primer intento")
else:
    if intento1 < omegalul:
        print("El numero es mayor")
    else:
        print("El numero es menor")

# Intento 2

    intento2 = int(input("Intenta de nuevo: "))

    if intento2 == omegalul:
        print("Felicitaciones, adivinaste en tu segundo intento")
    else:
        if intento2 < omegalul:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")

    # Pista
    print ("Te dare una pista: ")

    dist1 = abs (omegalul - intento1)
    dist2 = abs (omegalul - intento2)

    if dist1 < dist2:
        print(f"El numero que buscas es mas cerca de {intento1} que de {intento2}")
    elif dist2 < dist1:
        print (f"El numero es mas cerca {intento2} que de {intento1}")
    else:
        print("Ambos intentos estan en un punto medio")

        # Intento 3
    intento3 = int(input("Intenta la ultima vez: "))

    if intento3 == omegalul:
        print("Felicidades adivinaste en tu tercer y ultimo intento")
    else:
        if intento3 < omegalul:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")
    

