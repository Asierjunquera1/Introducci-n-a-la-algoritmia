def funcion_decoradora(funcion2):
    def funcion3(*args):
        print("la media aritmeica es:")
        funcion2(*args)
    return funcion3

@funcion_decoradora
def media_aritmetica(num1, num2, num3):
    media=(num1+num2+num3)/3
    print(media)

num1=int(input("El numero 1 es:"))
num2=int(input("El numero 2 es:"))
num3=int(input("El numero 3 es:"))



media_aritmetica(num1,num2,num3)
