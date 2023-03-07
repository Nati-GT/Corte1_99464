def Saludo(nombre):
    print(f'Hola {nombre}')
    print('funcion: ', __name__)
#Saludo('Juan')
if __name__=="__main__":
    Saludo('Juan')