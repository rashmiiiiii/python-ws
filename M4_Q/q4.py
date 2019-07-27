
'''4.	Write a program to read data from the file story.txt and determine the following:
•	Total number of words in the file
•	The word that occurs maximum number of times
•	The number of conjunctions of various types (example: and, but, if)'''

try:
    line_count = 0
    word_count = 0
    with open("data.txt") as f:
        lines = f.readlines()
        w_c = {}
        for line in lines:
            words = line.split(" ")
            for word in words:
                word = word.strip().strip("\n".replace(',','')).upper()
                
                try:
                    w_c[word] += 1
                except KeyError:
                    count = 0
                    w_c[word] = 1
                    if word in ['AND','BUT','IF']:
                        count += 1
                  
        max_val = max(w_c.values())
        for k,v in w_c.items():
            if v == max_val:
                print(f"{k} : {v}")
    print(f"count of conjunctions:{count}")          
except Exception as e:
    print(f"file not found please check path {e}")