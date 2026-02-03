print("*** cajero automatico ***")


saldo = 1000
salir = False

while not salir:
    print('''Operaciones que puedes realizar:
          
          1. consultar saldo
          2. Retirar
          3. Depositar
          4. Salir''')
    
    obsion = int(input("Escoja una opcion: "))

    if obsion == 1:
        print(f"Tu saldo actual es de: ${saldo:.2f}")
    elif obsion == 2:
        retiro = float(input("Cuanto desea retirar: $"))
        if retiro <= saldo:
            saldo -= retiro 
            print (f"retiraste ${retiro} y tu saldo actual es de: ${saldo:.2f}" )     
        else:
            print("Su saldo es insuficiente")
    elif obsion == 3:
         deposito = float(input("Cuanto desea depositar: $"))       
         saldo += deposito 
         print(f"tu saldo actual es de ${saldo:.2f}") 
    elif obsion == 4:
         salir = True
         print("Saliste de la operación")
    else:
        print("Ingrese una obsion valida")         