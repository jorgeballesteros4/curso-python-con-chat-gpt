print("*** sistemas de descuentos vip ***")

cantidad = 10
productos = int(input("cuatos productos lleva hoy: "))
eres_miembro = input("eres miembro vip: si/no ")

aplicas_al_descuento = productos >= cantidad and eres_miembro == "si"
print(f"obtienes el desucento = {aplicas_al_descuento}")