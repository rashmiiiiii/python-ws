#number divisible by 9 but not 5
lb = int(input("enter the lower bound:"))
ub = int(input("enter the upper bound:"))
for i in range(lb,ub + 1):
    if i % 9 == 0 and i % 5 != 0:
        print(i,end= ' ')

'''res = " ".join([str(i) for i in range(lb,ub + 1) if i % 9 == 0 and i % 5 != 0])'''