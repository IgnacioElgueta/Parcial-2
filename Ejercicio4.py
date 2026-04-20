intento = 3

while intento > 0:
    password = input("Ingrese su clave: ")

    if password =="1234":
     print ("Bienvenido")

     break
    else:

     intento = intento-1

     print(f"Intento fallido. Te dalta, {intento}")

     if intento == 0:
        print("Acceso denegado")