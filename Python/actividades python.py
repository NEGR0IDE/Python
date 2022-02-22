def max(a,b):
    if a> b:
        return a
    else:
        return b
        

a=100
b=500
print(max(a,b))

def max_de_tres(a,b,c):
    if a > b and a > c:
        return a
    elif a < c and b < c:
        return c
    else:
        return b
c=0
print(max_de_tres(a,b,c))

def longitud (cadena):
    