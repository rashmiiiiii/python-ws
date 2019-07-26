num = int(input("enter the numbeer:"))
count = 0
while num > 0:
    rem = num % 10
    num = num // 10
    for i in range (2, rem // 2 + 1):
        if rem % i != 0:
            count += 1
print(count)

'''
count = 0
num =int(input())
while num > 0:
    digit = num % 10
    if digit in [2,3,5,7]:
        count += 1
    num //= 10'''