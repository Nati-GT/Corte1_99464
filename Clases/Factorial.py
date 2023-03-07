from Factorial import fcn_factorial as f
def main():
    n=int(input('ingrese el numero de grupos: '))
    m=int(input('ingrese el numero de mustras: '))
    resultado=((f(n))/(f(m)*f(n-m)))
    print(f'el numero de combinaciones posibles es: {resultado}')

if __name__=="__main__":
    main()