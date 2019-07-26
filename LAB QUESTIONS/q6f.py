#using filter
str = input("enter the string:")
str.lower()
lst = ['a','e','i','o','u']
r = list((filter(lambda x:x not in lst,str)))
s = ''.join(r)
print(s)


'''
in_str = input("enter the string")
for ch in ['a','e','i','o','u']:
    in_str =in_str.replace(ch,' ')
print(in_str)
'''