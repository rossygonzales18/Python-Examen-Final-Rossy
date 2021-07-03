#1. Realizar una función que permita la carga de n alumnos. 
#Por cada alumno se deberá preguntar el nombre completo y 
#permitir el ingreso de 3 notas. Las notas deben estar comprendidas entre 0 y 10. 
#Devolver el listado de alumnos.

n=int(input('Ingrese la cantidad de alumnos: '))
nombres=[]
notas=[]
for x in range(n):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    n1=int(input("Ingrese la primer nota:"))
    n2=int(input("Ingrese la segunda nota:"))
    n3=int(input("Ingrese la tercera nota:"))
    notas.append([n1,n2,n3])

for x in range(n):
    print(nombres[x],notas[x][0],notas[x][1],notas[x][2])


#2. Definir una función que dado un listado de alumnos evalúe cuántos aprobaron 
#y cuántos desaprobaron, teniendo en cuenta que se aprueba con 4. La nota será 
#el promedio de las 3 notas para cada alumno.

n=int(input('Ingrese la cantidad de alumnos: '))
nombres=[]
notas=[]
for x in range(n):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    n1=int(input("Ingrese la primer nota:"))
    n2=int(input("Ingrese la segunda nota:"))
    n3=int(input("Ingrese la tercera nota:"))
    notas.append([n1,n2,n3])
    prom=(n1+n2+n3)/3
    contaA=0
    contaD=0
    if prom>=4:
        contaA+=contaA
    else:
        contaD+=contaD

print('Total de estudiantes aprobados: {}'.format(contaA))
print('Total de estudiantes desaprobados: {}'.format(contaD))

#3. Informar el promedio de nota del curso total.

n=int(input('Ingrese la cantidad de alumnos: '))
nombres=[]
notas=[]
suma=0
for x in range(n):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    n1=int(input("Ingrese la primer nota:"))
    n2=int(input("Ingrese la segunda nota:"))
    n3=int(input("Ingrese la tercera nota:"))
    notas.append([n1,n2,n3])
    prom=(n1+n2+n3)/3
    suma=suma+prom

promT=suma/n
print('El promedio total del salones: ')

#4.Realizar una función que indique quién tuvo el promedio más alto y 
#quién tuvo la nota promedio más baja.
