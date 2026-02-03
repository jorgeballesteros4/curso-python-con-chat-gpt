print("*** Calculadora de python ***")

salir = False
while not salir:
    print('''Opciones que puedes realizar:
          1. Suma
          2. Resta
          3. Multiplicación
          4. Division
          5. Salir''')
    
    operacion = int(input("Escoje una opcion: ") )
    if operacion == 1:
        numero1 = float(input("Dame el valor 1: "))
        numero2 = float(input("Dame el valor 2: "))
        resultaso = numero1 + numero2
        print(f"el valor de la suma es de: ${resultaso}")
    elif operacion == 2:
        numero1 = float(input("Dame el valor 1: "))
        numero2 = float(input("Dame el valor 2: "))
        resultaso = numero1 - numero2
        print(f"el valor de la resta es de: ${resultaso}")    
    elif operacion == 3:
        numero1 = float(input("Dame el valor 1: "))
        numero2 = float(input("Dame el valor 2: " ))
        resultaso = numero1 * numero2
        print(f"el valor de la multiplicación es de: ${resultaso}")      
    elif operacion == 4:
        numero1 = float(input("Dame el valor 1: "))
        numero2 = float(input("Dame el valor 2: "))
        resultaso = numero1 / numero2
        print(f"el valor de la division es de: ${resultaso}")   
    elif operacion ==5:
        salir = True
        print("saliste de la calculadora ")    
    else:
        print("Ingrese un numero correcto")       