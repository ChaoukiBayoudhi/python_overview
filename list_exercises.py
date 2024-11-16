L1=[2,4,5,11,6,9]
#print the list using indexes
print('The list of integer :')
for i in range(len(L1)):
    print(L1[i])
#print the list using contain
print('The list of integer :')
for x in L1:
    print(x)

#modify the second value by a value from the keyboard
x=int(input('Enter an integer : '))
L1[1]=x

print('The list of integer after update :')
for x in L1:
    print(x)

def square_list(n:int)->list:
    L=[]
    for i in range(1,n+1):
        L.append(i*i)
    return L

def square_list_v2(n:int)->list:
    L=[i**2 for i in range(1,n+1)]
    return L

#Execute the function square_list
n=int(input('Enter an integer :'))
Ls=square_list(n)
print(Ls)

#Execute the function square_list_v2

n=int(input('Enter an integer :'))
Ls=square_list(n)
print(Ls)