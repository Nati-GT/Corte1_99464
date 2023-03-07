def suma(a,b):
    resultado= a+b
    return resultado
def imprimir(nombre):
    print(nombre,'su resultado es: ')
n='si'
while n=='si': 
    nombre=input('ingrese su nombre: ')
    a=int(input('ingrese un numero: '))
    b=int(input('ingrese un numero: '))
    res=suma(a,b)
    imprimir(nombre)
    print(res)
    n=input('¿quieres sumar otro numero? (si/no)')