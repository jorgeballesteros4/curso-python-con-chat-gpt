print("*** dibujar un triangulo ***")

dibujo = "*"
cantidad = int(input("cuantas columnas quiere el triangulo: "))

for _ in range(1,cantidad + 1):
    cantidad += 2
    print(dibujo)
