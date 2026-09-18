def multiplicar(a,b):
    if b == 1:
        return a 
    else:
        return a + multiplicar(a, b-1)

print(multiplicar(4, 100))