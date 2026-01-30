print("*** Sistemas de calificaión ***")

#le pedimos al usuraio que ingrese la calificación.
calificaion = float(input("ingrese su calificación: "))

if 9 <= calificaion <= 10:
    print("Su calificación es A")
elif 8 <= calificaion < 9:
    print("Su calificación es B") 
elif 7 <= calificaion < 8:
    print("Su calificación es C")      
elif 6 <= calificaion < 7:
    print("Su calificación es D")
elif 0 <= calificaion < 6:
    print("Su calificaiocn es F")
else:
    print("Valor desconocido")            