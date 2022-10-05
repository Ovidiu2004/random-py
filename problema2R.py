from random import randint
n = int(input ('Introduceti un numar:'))
v = []

while n>0:
    for i in range(1):
        x =randint (1, 6)
        v.append(x)
        print(x) 
    n -= 1

print("Valoarea 6 a aparut de ",v.count(6),"ori.")       