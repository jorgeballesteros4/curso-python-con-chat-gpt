print("*** Sistemas de Envios ***")

#pedimos al usuario el destino del paquete y cuanto kilos pesa

destino = input("el envio es nacinal internacional: nacional/internacional  ")
peso = float(input("cuantos kilogramos pesa el paquete "))

nacional = 10 * peso
internacional = 20 * peso

if nacional == destino:
    print(f"El valor del envio nacional es de: ${nacional}")
elif destino == internacional:
    print(f"Ele valor del envio internacional es de: ${internacional}  ")    