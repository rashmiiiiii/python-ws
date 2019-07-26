#prime numbers
def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
Lb = int(input("enter the lo;wer bound:"))
Ub = int(input("enter the upper bound"))
for i in range(Lb,Ub + 1):
    if prime(i):
        print(i)

'''
for numm in range(lb,ub + 1):
    is_prime = True
    if num > 2 and num % 2 != 0:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False'''
