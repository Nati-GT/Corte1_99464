n=int(input('ingrese  un numero de entre dos a ocho cifras'))
while n!=0:
    x=(n//10)*10
    dig= n-x
    n=x
    if dig  ==5:
        print('salto')
    else:
        print(dig)
