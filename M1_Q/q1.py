'''1.write a program to accept a number and determine whether it is prime or not'''
import math
is_prime = True
def is_prime_fun(num):
    '''if it is prime it return true otherwise false'''
    if num < 2:
        is_prime = False
    else:
        for i in range(2,int(math.sqrt(num)) + 1): #for i in range(2,num//2 + 1):
            if num % i == 0:
                is_prime = False
    return True

num = int(input("enter the number"))
is_prime = is_prime_fun(num)
if is_prime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")