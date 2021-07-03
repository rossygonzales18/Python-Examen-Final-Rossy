
cantidad = float(input('Ingrese la cantidad de dinero depositado: '))
interes=0.04
año1=round(cantidad*(1+interes),2)
año2=round(año1*(1+interes),2)
año3=round(año2*(1+interes),2)
print('Ahorro del primer año es: {}'.format(año1))
print('Ahorro del segundo año es: {}'.format(año2))
print('Ahorro del stercer año es: {}'.format(año3))
