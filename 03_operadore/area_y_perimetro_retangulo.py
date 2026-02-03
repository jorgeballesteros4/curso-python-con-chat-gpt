print("*** area y perimetro de un retangulo *** ")

#preguntarle al cliente que medidas tiene base por altura

base = float(input("Ingrese la base del retangulo: "))
altura = float(input("Ingrese la altura del retangulo: "))

#hacer los calculos matematicos

area = base * altura
perimetro = 2 * (base + altura)

#imprimimo los resultados 

print(f"el area del retangulo es de: {area}.2")
print(f"el perimetro  del retangulo  es de: {perimetro}.2")
