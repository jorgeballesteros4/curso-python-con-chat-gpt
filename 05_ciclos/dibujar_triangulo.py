print("*** dibujar un triangulo ***")


numero_de_filas = int(input("cuantas columnas quiere el triangulo: "))

for fila in range(1,numero_de_filas + 1):
        espacio_en_blanco = " " * (numero_de_filas )
        caracteres = "*" *( fila-1)
        print(f"{espacio_en_blanco}{caracteres}")