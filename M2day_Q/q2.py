''' 2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row

Example:
Input: 
[[0 1 2 3]
 [3 4 5 5]
 [6 7 8 8]
 [9 0 1 9]]

Output:
	minimum value element in the array: 0
	maximum value element in the array: 9
	elements with minimum values column-wise: [0 0 1 3]
	elements with maximum values column-wise: [9 7 8 9]
	elements with minimum values row-wise: [0 3 6 0]
	elements with maximum values row-wise: [3 5 8 9]

'''
lst=[[0,1,2,3],
[3,4,5,5],
[6,7,8,8],
[9,0,1,9]]

maxele=-9999
minele=9999

for ele in lst:
    for item in ele:
        if item>maxele:
            maxele=item

for ele in lst:
    for item in ele:
        if item<minele:
            minele=item
lst1=[]
lst2=[]
for ele in lst:
    maxelem=-9999
    for item in ele:
        if item>maxelem:
            maxelem=item
    lst1.append(maxelem)

for ele in lst:
    minelem=9999
    for item in ele:
        if item<minelem:
            minelem=item
    lst2.append(minelem)


lst3=[]
lst4=[]

for i in range(0,len(lst)):
    maxcolumn=-9999
    for ele in lst:
        if ele[i]>maxcolumn:
            maxcolumn=ele[i]
    lst3.append(maxcolumn)

for i in range(0,len(lst)):
    mincolumn=9999
    for ele in lst:
        if ele[i]<mincolumn:
            mincolumn=ele[i]
    lst4.append(mincolumn)

print(f"minimum value element in the array:{minele}") 
print(f"maximum value element in the array:{maxele}") 
print(f"elements with minimum values column-wise:{lst4}") 
print(f"elements with maximum values column-wise:{lst3}")
print(f"elements with minimum values row-wise:{lst2}") 
print(f"elements with maximum values row-wise:{lst1}")