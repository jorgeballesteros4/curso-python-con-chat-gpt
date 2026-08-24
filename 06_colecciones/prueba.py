from random import randint

print("*** aleatorio ***")

numero_secreto = randint(1,50)
numero =None
intento_maximo = 7
intento = 1

numero= int(input("digite pues: "))

while numero != numero_secreto and intento < intento_maximo:
    intento += 1
    if numero < numero_secreto:
        
        print("es mayor")
    elif numero > numero_secreto:
        print("es menor") 
    
    numero= int(input("digite pues: "))
if numero == numero_secreto:
    print(" buena parc")
else: 
    print("no mono" )