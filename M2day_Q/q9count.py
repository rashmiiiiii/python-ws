''' 9.	Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. Also, display those words next to their respective count.

Input:
"Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3."
Output:	
Word appearing maximum times: abcdefg; x times
Word appearing minimum times: pqrstuv; y times
(Where abcdefg and pqrstuv are words from the given paragraph; x and y are the number of instances these words appear in the paragraph.)
'''

data = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it\
     Comprehensions are constructs that allow sequences to be built from other sequences\
     Several types of comprehensions are supported in both Python 2 and Python 3".lower()

d = dict()
count = 0
lst = []
words = data.split()
for word in words:
    if d.get(word) == None:
        d[word] = 1
    else :
        d[word] +=1
print(d)
cmax = -9999
max = ' '
cmin = 9999
min = ' '
for i in d:
    if d[i] > cmax:
        cmax = d[i]
        max = i
for i in d:
    if d[i] < cmin:
        cmin=d[i]
        min = i

print(f"Word appearing maximum times: {max};{cmax} times")
print(f"Word appearing minimum times: {min};{cmin} times")
    



    
