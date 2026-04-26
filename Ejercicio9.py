#TRY

try:
    num1 = float(input("Por favor, ingresa un numero: "))
    num2 = float(input("Por favor, ingresa un numero: "))

    if num2 == 0:
        raise ZeroDivisionError # Lanza el error o proboca el error manual
    
    resultado = num1 / num2
    print(f"El resultado de esta division es: {resultado}")

except ValueError:
    print("¡Error! Ingresa un nuevo numero")

except ZeroDivisionError:
    print("¡Error! no se puede dividir por cero.")

    print("Fin del programa", resultado)

print("Fin del programa")