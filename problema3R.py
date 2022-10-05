from random import randint

nr0 = 0
nr1 = 0
nr2 = 0
nr3 = 0
nr4 = 0
nr5 = 0
nr6 = 0
nr7 = 0
nr8 = 0
nr9 = 0
n = randint(0,999999999)
print(n)

for j in [i for i in str(n)]:
    if j =='0':
        nr0+=1
    if j =='1':
        nr1+=1
    if j =='2':
        nr2+=1
    if j =='3':
        nr3+=1
    if j =='4':
        nr4+=1
    if j =='5':
        nr5+=1
    if j =='6':
        nr6+=1
    if j =='7':
        nr7+=1
    if j =='8':
        nr8+=1
    if j =='9':
        nr9+=1

print(" 0 apare de",nr0,"ori")
print(" 1 apare de",nr1,"ori")
print(" 2 apare de",nr2,"ori")
print(" 3 apare de",nr3,"ori")
print(" 4 apare de",nr4,"ori")
print(" 5 apare de",nr5,"ori")
print(" 6 apare de",nr6,"ori")
print(" 7 apare de",nr7,"ori")
print(" 8 apare de",nr8,"ori")
print(" 9 apare de",nr9,"ori")