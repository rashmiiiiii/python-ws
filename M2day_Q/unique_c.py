'''1.	Write a program to count the number of unique words and the number of occurrences of each of those words from the question provided below.
Input:
"How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
Output:
Number of unique words: x
abcd: p times
efgh: q times
rstu: t times
……
(Where abcd, efgh and stuv are words from the given input question; p, q and t are the number of instances these words appear in the input.)
 '''

data = "How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
d = list()
count = 0
words = data.split()
for word in words:
    if not word in d:
        d.append(word)
        count += 1
for i in d:
    
