print("*** Mayor de edad ***")

#le preguntamos al usuario cuanto años tiene

edad =int(input("cuantos años tienes "))

if edad >= 18:
    print(f"tienes {edad} entonces eres mayor de edad")
elif edad <18:
    print(f"tienes {edad} entonces eres menor de edad ")
else:
    print("ingrese su edad")        