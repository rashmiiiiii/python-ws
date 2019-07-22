'''7.	Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.'''
num = int(input("enter the number:"))
while num > 0:
    sum = 0
    rem = num % 10
    sum = sum + rem
    num = num // 10
    if  sum >= 0 and sum <=9:
        print(sum)




