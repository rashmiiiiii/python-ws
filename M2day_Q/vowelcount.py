name =  input("enter the name")
name = name.lower()
c = 0
lst = ['a','e','i','o','u']
vowel = list(filter(lambda x:x in lst,name))
print(vowel)
print(len(vowel))
