def funcion_decoradora(funcion2):
    def funcion3(*args):
        print("la nomina es:")
        funcion2(*args)
    return funcion3

@funcion_decoradora
def nomina(salario, horas_extra):
    sueldo_hora=salario/(35*7)
    salario_total=salario
    for i in range(horas_extra):
        if i<9:
            salario_total+=sueldo_hora*1,25
        else:
            salario_total+=sueldo_hora*1,5
    print(salario_total)

salario=int(input("El salario bruto mensual es:"))
horas_extra=int(input("La cantidad de horas extra trabajadas es:"))

nomina(salario, horas_extra)

