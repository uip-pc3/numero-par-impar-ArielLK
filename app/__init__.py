from app.parOimpar import verificar

if __name__ == "__main__":

    print("Validacion de un numero para determinar si es par o impar")
    num = int(input("Favor introducir un numero: "))

    if verificar(num):
        print("El numero " + str(num) + " es un numero par")
    else:
        print("El numero " + str(num) + " es un numero impar")
