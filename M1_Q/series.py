'''program to print the series 1+1/2+....+1/n'''
n = int(input("enter the number:"))
sum = 0
for i in range (1, n+1):
    sum = sum + (1/i)
print(f"sum = {sum}")