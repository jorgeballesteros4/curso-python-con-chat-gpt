print("*** Sistemas de Envios ***")

#pedimos al usuario el destino del paquete y cuanto kilos pesa

destino = input("el envio es nacinal internacional: nacional/internacional  ")
peso = float(input("cuantos kilogramos pesa el paquete "))

nacio = peso * 10
inter = peso * 20

if destino == "nacional":
    print(f"El valor del envio nacional es de: ${nacio}")
elif destino == "internacional":
    print(f"Ele valor del envio internacional es de: ${inter}  ")    
else:
    print("debes de indicar si es nacional o internaciona y el peso del paquete")    