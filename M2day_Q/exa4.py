import random as rn 
num = []
for i in range(1,21):
    num.append(rn.randint(1,50))
    
res = [max(num),min(num)]
print(res)


