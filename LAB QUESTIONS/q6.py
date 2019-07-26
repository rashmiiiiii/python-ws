str = input("enter the string:")
str = str.lower()
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    else:
        print(i,end ="")
