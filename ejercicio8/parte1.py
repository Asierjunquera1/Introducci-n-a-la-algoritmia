def funcion_decoradora(funcion2):
    def funcion3(*args):
        print("El precio total, con todos los impuestos es:")
        funcion2(*args)
    return funcion3

@funcion_decoradora
def precio_con_TII(precio_sin_impuestos, porcentaje_IVA):
    dinero_IVA=porcentaje_IVA/100*precio_sin_impuestos
    precio_total=dinero_IVA+precio_sin_impuestos
    print(precio_total)

precio_sin_impuestos=int(input("El precio sin impuestos es:"))
porcentaje_IVA=int(input("El porcentaje de IVA es:"))


precio_con_TII(precio_sin_impuestos, porcentaje_IVA)

