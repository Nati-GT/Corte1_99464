from math import sqrt as raizc
a=int(input('ingrese el valor de X^2: '))
b=int(input('ingrese el valor de X: '))
c=int(input('ingrese el valor del termino independiente: '))

if ((b**2)-4*a*c)/(2*a)<0:
    print('la solucion es imaginaria')
else: 
    x1= (-b+raizc((b**2)-4*a*c))/(2*a)
    x2= (-b+raizc((b**2)-4*a*c))/(2*a)
    print('el primer resultado es: ',x1)
    print('el segundo resultado es: ',x2)