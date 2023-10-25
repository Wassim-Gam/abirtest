def same(a):
    
   
    if a[0]  == a[-1]  :
        return True
    else:
        return False
    
       
print(same('test'))
print(same('abcab'))
print(same('abcbac'))
print(same('abcbA'))

# 3.1.c'est une fonction qui permet de lire une chaine de 2 sens : palindrome 