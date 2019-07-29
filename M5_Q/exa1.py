#with list
data_list = [
    [1001,"python",2018,1,"hearizen"],
    [1002,"web",2018,1,"spaneos"],
    [1003,"java",2020,1,"hearizen"]
    ]

try:
    with open("ws.txt","w") as file:
        for d in data_list:
            line = f'{d[0]},{d[1]},{d[2]},{d[3]},{d[4]}\n'
            file.write(line)
except Exception as e:
    print(str(e))
