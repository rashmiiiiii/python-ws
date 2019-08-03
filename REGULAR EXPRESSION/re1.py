import re
data = "lakshman is in 560070 works at Banglore and Krish is in 522612 and works at Guntur" 
lst= re.findall(r"at\s+([A-z]*)\s?",data)                          
print(lst)

#? = zero or one
# * = zero or more
# + = one or more