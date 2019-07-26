#sum of the elements of the list
def biggest(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
ls =[2,5,4,1,3]
res = sum(ls)
print(f"the sum of the elements in the list{ls} is :{res}")