'''COUNTING THE VOWELS INA STRING'''
name =  input("enter the name")
name = name.lower()
c = 0
lst = ['a','e','i','o','u']
for i in name:
    if i in lst:
        c += 1
print(c)

#using lambda
''' print(len(list(filter(lambda x:x in lst,name))))'''