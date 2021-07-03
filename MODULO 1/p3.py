
a=int(input('Ingrese el primer coeficiente de la ecuacion de segundo grado'))
b=int(input('Ingrese el sebundo coeficiente de la ecuacion de segundo grado'))
c=int(input('Ingrese el tercer coeficiente de la ecuacion de segundo grado'))

if b**2-4*a*c < 0:
    print('No tiene solucion real')
else:
    if b**2-4*a*c == 0:
        x=(-b+(b**2-4*a*c))**(1/2)/(2*a)
        print('Tiene una doble solucion: {} '.forma(x))
    else:
        x1=(-b+(b**2-4*a*c))**(1/2)/(2*a)
        x2=x=(-b-(b**2-4*a*c))**(1/2)/(2*a)
        print('Tine dos soluciones diferentes: ')
        print('Solucion 1 es: {}'.format(x1))
        print('Solucion 2 es: {}'.format(x2))
