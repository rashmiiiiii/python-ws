'''4.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/23 + 1/33 + 1/43 + …… + 1/n3'''
'''program to print the series 1+1/2+....+1/n'''
n = int(input("enter the number:"))
sum = 0
for i in range (2, n+1):
    sum = sum + (1/pow(i,3))
print(f"sum = {sum}")
