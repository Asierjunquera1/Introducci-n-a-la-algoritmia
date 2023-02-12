def funcion_decoradora(funcion2):
    def funcion3(*args):
        print("el importe generado por los intereses es:")
        funcion2(*args)
    return funcion3



@funcion_decoradora
def importe(capital, porcentaje_intereses, meses):
    importe_intereses=capital*porcentaje_intereses/100*meses
    print(importe_intereses)
importe(8000, 5, 12)
