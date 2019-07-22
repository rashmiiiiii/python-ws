'''program to print the n prime number between the range'''
n1 = int(input("enter the range for n1:"))
n2 = int(input("enter the range for n2:"))

for i in range(n1,n2+1):
    is_prime = True
    if i < 2:
        is_prime = False
    else:
        for j in range ( 2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        print(i)

        