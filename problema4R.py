from random import randint
nr1=randint(1,6)
nr2=randint(1,6)
print('Numerele aruncate sunt:',nr1,'si',nr2)
while nr1!=nr2:
    nr1=randint(1,6)
    nr2=randint(1,6)
    print('Numerele aruncate sunt:',nr1,'si',nr2)
print('Suma dubletului:',nr1*2)