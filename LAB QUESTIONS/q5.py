num = int(input("enter the number"))
new = 0
count = 1
while True:
    if num == 0:
        break
    temp = num%10
    num = num//10
    if temp == 9:
        temp = 0
        new=new+(temp*count)
        count=count*10
    else:
        temp = temp+1
        new=new+(temp*count)
        count=count*10
print(new)

''' or
num = tnum =int(input("enter the number:"))
n = 4
res = 0
while tnum >= 0:
    q = tnum // (10 ** n)
    tnum = tnum % (10 ** n)
    if q == 9:
        q = 0
    else:
        q += 1
    res += q * (10 ** n)
    n = n - 1
print(res)'''



