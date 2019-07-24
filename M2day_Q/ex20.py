'''progrm to find sum of even numbers out of 1-10 numbers square'''
from functools import reduce
lst = [1,2,3,4,5,6,7,8,9,10]
res = reduce(lambda a,b : a + b,list(filter(lambda x:x % 2 == 0,(list(map(lambda a: a*a,lst))))))
print(res)

