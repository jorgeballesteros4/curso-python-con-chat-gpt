print("*** progrma que me invente en operadores 1 ***")

#vamos hacer un programa donde se puede hacer trabajos de alturas cuando cumple 3 condiciones
#1 que tenga salud al dia
#2 que tenga arl al dia
#3 curso de alturas al dia

salud = input("tienes la salud al dia: si/no  ")
arl = input("tienes la arl al dia:  si/no  ")
curso_de_altura = input("tienes la curso de altura:  si/no  ")


apto = salud == "si" and arl == "si" and curso_de_altura == "si"

print(f"eres apto para trabajar en alturas: {apto}")