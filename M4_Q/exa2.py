try:
    #f = open("data.txt","w")
    #data = "line one \r\n"
    num = 100 / 0
    #f.write(data)
except ZeroDivisionError as e:
    print("except block")
    print(f"{e}")
finally:            #finally blocks are also called as resource handler
    print("finally block...")