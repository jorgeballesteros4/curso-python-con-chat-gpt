print("Tienda en linea")

#preguntar si son miembros de la tienda
vip = input("eres miembro de la tienda: si/no: ")
compra = float(input("cuato es el monto de la compra: $"))
diez_porciento = compra * 0.9
cinco_porciento = compra * 0.95


if vip == "si" and compra >= 1000:
    print(f"eres miembro vip: {vip}")
    print("tienes un descuento del 10%")
    print(f"tu compra es de {compra} y queda en: ${diez_porciento}" )
elif vip == "si" and compra > 1000:
    print(f"eres miembro vip: {vip}")
    print("tienes un descunto del 5%")
    print(f"tu compra es de {compra} y queda en: ${cinco_porciento}" )
else:
    print(f"ya que no eres miembro te el valor de la compra es de: ${compra}  ")    