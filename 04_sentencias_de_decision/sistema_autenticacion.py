print("*** Sistermas de autenticación ***")

user = "jorgeballesteros4"
password = "lina"

usuario = input("digite su usuario: ")
contraseña = input("digite su contraseña: ")

if user == usuario and password == contraseña:
    print("vinvenido al sistmea")
elif user != usuario and password == contraseña:
    print("tu usuario es invalido")
elif user == usuario and password != contraseña:
    print("tu contraseña es invalida")    
elif user != usuario and password != contraseña:  
    print("usuario y contraseña son invalidos")  