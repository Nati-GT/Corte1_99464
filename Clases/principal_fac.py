def fcn_factorial(x):
    fac=1
    for i in range(1,x+1):
        fac*=i
        print(fac)
    return(fac)

if __name__=="__main__":
    fcn_factorial(7)
