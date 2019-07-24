import random as rn 
num = []

for i in range(1,101):
    num.append(rn.randint(1,1000))
rt = []
for j in num:
    if j % 3 == 0 and j % 6 == 0 and j % 9 != 0:
        rt.append(j)
print(rt)  



