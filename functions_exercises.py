
def Max(x,y):
    if x>y:
        return x
    else:
        return y

m=Max(5,7)
print(m)  # Output: 7

#appel de la fonction
a=int(input('Donner x : '))

b=int(input('Donner y :'))
m=Max(a,b)
exp1=3*m +5
print("expression = ",exp1)