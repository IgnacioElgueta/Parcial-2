intento = 3
while intento > 0:

    password = input("Ingrese su clave: ")

    if password =="1234":

        print ("bienvenido")

        break
    else:

        intento = intento-1

        print(f"Intento fallido. Tienes, {intento} intentos restantes")

        if intento == 0:
            print("Acceso denegado")