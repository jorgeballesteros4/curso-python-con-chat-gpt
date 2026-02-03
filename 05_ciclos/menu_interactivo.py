print("*** Menu interactivo ***")

salir = False
while not salir:
    print('''1. Crear email
         2. Eliminar email
         3. Salir del sistema''')

    menu = int(input("Ingrese una opcion: "))


    if menu == 1:
        print("crear email")
    elif menu == 2:
        print("eliminar  el email")    
    elif menu == 3:
        print("Saliste del sitema")
        salir = True
    else:
        print("ingrese un numero valido")        