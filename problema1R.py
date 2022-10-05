from random import randint

nr=int(input('Introduceti un numar:'))
k = []
sp = 0
sn = 0

for i in range(nr):
    k.extend ([ randint(-50,50)])

for i in k:
    if i > 0:
        sp += i
    else:
        sn += i

print(k)
print("Sumavalorilor pozitive este ",sp)
print("Suma valorilor negative este" ,sn)