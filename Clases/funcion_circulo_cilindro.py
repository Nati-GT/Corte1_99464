def area(r):
    from math import pi as pi
    area= pi*(r**2)
    return area

def volumen(h,a):
    v=a*h
    return v


r=int(input('ingrese el radio: '))
h=int(input('ingrese la altura: '))

a=area(r)
A=round(a,2)
v=volumen(h,a)
V=round(v,2)

print(f'el area es {A} y el volumen es {V}')

