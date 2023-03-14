num=int(input("indique la cantidad de numeros primos: "))
j=2
n=2
x=0
print('1')
while x<=num-2:
   div = n%j
   if div==0:
        if n==j:
           print(n, end=',')
           x=x+1
        
        j=2
        n+=1
   else:
        j+=1
       
     
   