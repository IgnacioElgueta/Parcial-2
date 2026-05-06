print ("Bienvenido al grupo santander")

while True:


    rut = input ("Ingrese su rut sin digito verificador: ")

    if rut.isdigit() and len(rut) ==8:
        break

    else:
         print("Escriba solo 8 digitos")

while True:

    dv = input ("Ingrese su digito verificador: ").upper()

    if len(dv) == 1 and (dv.isdigit() or dv =="k"):

        break

    else:
        print("Error")   

while True:
    clave = input("Ingrese su clave: ")

    if clave.isdigit() and len(clave) <= 10:
        print("Clave válida")
        break
    else:
        print("Clave inválida (máximo 10 dígitos)")

