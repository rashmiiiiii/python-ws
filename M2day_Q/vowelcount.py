name =  input("enter the name")
name = name.lower()
c = 0
lst = ['a','e','i','o','u']
print(len(list(filter(lambda x:x in lst,name))))