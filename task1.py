def factoriel(n):
    f = 1
    for i in range (1,n+1):
        f = f*i 
    return f
n = int(input("donner un entier:"))
res = factoriel(n)
print(res)    
    
