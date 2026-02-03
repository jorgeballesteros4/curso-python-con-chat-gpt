print("*** generacion  ticket de venta ***")

articulo1 = input("que producto deseas comprar: ")
valor1 = float(input(f"que precio tiene {articulo1}= "))
articulo2 = input("que producto deseas compra: ")
valor2 = float(input(f"que precio tiene {articulo2}=  "))
articulo3 = input("que producto deseas compra: ")
valor3 = float(input(f"que precio tien {articulo3}= "))

suma = valor1 + valor2 + valor3
impuesto = suma*0.19
total_a_pagar = suma + impuesto

print(f"la suma de los articulos es = {suma}")
print(f"el valor del impuesto ed de = {impuesto}")
print(f"el total a pagar es de = {total_a_pagar}")