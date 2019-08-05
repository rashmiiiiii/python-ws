'''1.	Given a string “12, 14-15,  18, 23- 2”, produce the list “[12, 14, 15, 18, 23, 2]”.'''
data = "12, 14-15,  18, 23- 2 "
d = data.replace("-",",")
n_d = d.replace(" ","")

print(n_d)

