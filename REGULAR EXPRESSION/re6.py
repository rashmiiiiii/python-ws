import re
data = "Learning- Python, is fun. Python_programming is, easy"
data= re.sub(r"-|_|,|\s+"," ",data)
data ==re.sub(r"\s+"," ",data)
print(data)