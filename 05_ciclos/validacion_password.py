print("*** Validación de password ***")

#le preguntamos al usurario que itrodusaca una nueva contraseña 

password = input("Introdusca nueva contraseña de almenos 6 digitos: ")


while len(password) < 6:
    print("incorrecto la contraseña debe de ser al menos de 6 digitos")
    password = input("Introdusca nueva contraseña de almenos 6 digitos: ")
print("tu contraseña es correcta ")    