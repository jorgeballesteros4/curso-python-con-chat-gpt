from random import randint
print("*** Juego de adivinanza ***")

numero_secreto = randint(1,50)
intnetos_maximo = 7
intentos = 0
numero = None

numero = int(input("ingrese un numero del 1 al 50: "))
while numero != numero_secreto and intentos < intnetos_maximo:
    intentos += 1
    if numero < numero_secreto:
        print("el numero es mayor")
    elif numero > numero_secreto:
        print("El numero es menor")
    numero = int(input("ingrese un numero del 1 al 50: "))    
if numero == numero_secreto:
    print(f"Felicidanes lo hizo en {intentos} y el numero secreto era {numero}")
else:
    print("se te agoto el numero de intentos")            