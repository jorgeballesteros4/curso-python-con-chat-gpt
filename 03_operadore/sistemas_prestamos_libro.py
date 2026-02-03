print("*** sistemas prestamos de libros ***")

credencial = input("tienes credencial de estudiante: si/no ")
kilometros = float(input("a cuanto kilometros vives de la institución: "))

prestamos = credencial == "si" or kilometros <= 3

print(f"su prestamo del libro es:  {prestamos} ")


