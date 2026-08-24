from random import randint

print("*** aleatorio ***")

numero_secreto = randint(1,50)
numero =None
intento_maximo = 7
intento = 1

numero = int(input("ingrese un numero del 1 al 50; "))

while numero != numero_secreto and intento < intento_maximo:
    intento +=1
    if numero < numero_secreto:
        print("el numro es mayor")
    elif numero > numero_secreto:
       print("el numero es menor")
    numero = int(input("ingrese un numero del 1 al 50; "))  
if numero == numero_secreto:
    print(f"que bueno lo adivinaste en {intento} intentos")    
else:
    print("no viejo no adivinaste")    