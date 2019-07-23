'''7.Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.'''

sum = 0

count = 0
num = int(input("enter the number:"))
while num > 0:
    rem = num % 10
    count += 1
    sum = sum + rem
    num = num // 10
while count != 0:
    tsum = 0
    rem = sum % 10
    tsum +=rem
    sum = sum //10
    while tsum >=0 and tsum <=9:
        rem = tsum % 10
        
        
    print(tsum)


    




