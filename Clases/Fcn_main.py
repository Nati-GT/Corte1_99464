import Fcn_ext

def main():
    nombre = input('escriba su nombre: ')
    Fcn_ext.Saludo(nombre)
    print('funcion: ', __name__)

if __name__=="__main__":
    main()
