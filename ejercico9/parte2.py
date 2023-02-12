def funcion_decoradora(funcion2):
    def funcion3(*args):
        print("la media ponderada es:")
        funcion2(*args)
    return funcion3

@funcion_decoradora
def media_ponderada(num1, num2, num3, coeficiente1, coeficiente2, coeficiente3):
    media=(num1+coeficiente1+num2+coeficiente2+num3+coeficiente3)/(coeficiente1+coeficiente2+coeficiente3)
    print(media)

num1=int(input("El numero 1 es:"))
coeficiente1=int(input("Y su coeficiente de ponderacion es:"))
num2=int(input("El numero 2 es:"))
coeficiente2=int(input("Y su coeficiente de ponderacion es:"))
num3=int(input("El numero 3 es:"))
coeficiente3=int(input("Y su coeficiente de ponderacion es:"))

media_ponderada(num1, num2, num3, coeficiente1, coeficiente2, coeficiente3)
