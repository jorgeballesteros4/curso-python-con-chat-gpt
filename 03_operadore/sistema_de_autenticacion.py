print("*** sitemas de autencicaón ***")

usuario = "jorgeballesteros4"
contraseña = "nacional04"

user = input("ingresa su usuario: ")
contra = input("ingrese su contraseña : ") 

autenticacion = user ==usuario  and contra == contraseña

print(f"tu usurio y contraseña son: {autenticacion}")