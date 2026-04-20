nombre = input("Escriba su nombre: ")

intento = 5
while intento > 0:

    password = input("Ingrese su clave: ")

    if password =="3524":

        print (f"bienvenido, {nombre}")

        break
    else:

        intento = intento-1

        print(f"Intento fallido. Tienes, {intento} intentos restantes")

        if intento == 0:
            print("Porfavor comuniquese con nuestro call center")