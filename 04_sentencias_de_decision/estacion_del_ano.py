print("identifica la estacion del años***")

#preguntamos al cliente que mes del año estamos

mes = int(input("ingrese el numero en el mes que estamos: "))

if mes == 1 or mes == 2 or mes ==  12:
    print("estamso en la estacion de invierno! ")
elif mes == 3 or mes == 4 or mes == 5:
    print("estamo en la estacion de primavera")    
elif mes == 6 or mes == 7 or mes == 8:
    print("estamos en la estción de verano ")
elif mes == 10 or mes == 10 or mes == 11:
    print("estamos en la estación otoño ")
else:
    print("ingrese un numero verdadero del 1 al 12")            