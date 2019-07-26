def biggest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))
res = biggest(num1,num2,num3)
print(f"biggest of the three numbers {num1},{num2} and {num3}:{res}")
