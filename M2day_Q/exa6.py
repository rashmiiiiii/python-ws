lst_1 = [1,2,3,4]
lst_2 = [4,5,6,7]
lst_3 = []
for i in range(len(lst_1)):
    lst_3.append(lst_1[i] + lst_2[i]) # or lst_3 =list(map(lambda a,b : a + b ,list_1,list_2))
print(lst_3)