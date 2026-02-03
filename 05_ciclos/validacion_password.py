print("*** Validacion de password ***")

password = input("ingrese un password de minimo 6 digitos: ")

while len(password)< 6:
    
    print("Tu password no es correcto")

    password = input("ingrese un password de minimo 6 digitos: ")
    print("Tu password es correcto")    


