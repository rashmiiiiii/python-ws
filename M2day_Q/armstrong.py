def amstrong_num(num):
    res = 0
    num_1 = num
    while num != 0:
        r = num % 10
        res = res + r ** 3
        num = num // 10
    return num_1 == res

input_num = int(input("enter the number"))
if (amstrong_num(input_num)):
    print(f"given number {input_num} is amstrong")
else:
    print(f"given number {input_num} is not an amstrong")
