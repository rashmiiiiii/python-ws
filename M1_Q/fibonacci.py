'''5.	Write a program to print the Fibonacci series up to the number 34. 
(Example: 0, 1, 1, 2, 3, 5, 8, 13, … The Fibonacci Series always starts with 0 and 1, the numbers that follow are arrived at by adding the 2 previous numbers.)'''

fib = 0
fib1 = 1
print(fib)
print(fib1)
for i in range (3,35):
    
    fib3 = fib + fib1
    fib = fib1
    fib1 = fib3
    print(fib3)
    if fib3 == 34:
        break
    