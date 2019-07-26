tnum=num = int(input("enter the number:"))
while num > 9 :
    num = num % 10 + num // 10 
print(f"the sum of digits of {tnum} is {num}")
'''def sum (num):
    sum = 0
    while num > 0 or sum > 9:
        if num == 0:
            num = sum
            sum = 0
        sum += num % 10
        num = num // 10
    return sum
num = int(input("enter the number:"))
res = sum(num)
print(f"result = {res}")'''


'''
tnum=num = int(input("enter the number:"))
while num > 9:
    sum = (num % 10 + num // 10)   or num = num % 10 + num // 10 
    num = sum
print(f"the sum of digits of {tnum} is :{num}")'''