def bubble(t):
    n = len(t)
    for i in range (1, n):
        for j in range(i):
            print(j)
            if (t[j] > t[j+1]):
                temp = t[j]
                t[j] = t[j+1]
                t[j+1] = temp
    return t 
t =[20,5,1,9,60,30]       
resultat =bubble(t) 
print(resultat)        

# Use a Python function to sort it 
# sorted sans modifier la liste d'origine      
res = sorted(t)
print(res)

