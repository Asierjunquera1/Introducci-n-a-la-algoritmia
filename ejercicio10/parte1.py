def funcion_decoradora(funcion2):
    def funcion3(*args):
        print("El area del triangulo es:")
        funcion2(*args)
    return funcion3

@funcion_decoradora
def area(altura, lado):
    a=altura*lado/2
    print(a)

lado=int(input("La longitud de un lado es:"))
altura=int(input("La altura con respecto a ese lado es:"))


area(altura, lado)
