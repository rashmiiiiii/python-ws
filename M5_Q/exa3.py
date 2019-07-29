#using csv
import csv
data_dict = [
      {"id":1001,"wname":"python","year":"2019","status":1,"company":"hearizen"},
      {"id":1002,"wname":"web","year":"2018","status":0,"company":"spaneos"}
      ]
    
try:
    with open("ws2.csv","w",newline = '') as file:
        heading = ["id","wname","year","status","company"]
        obj = csv.DictWriter(file,fieldnames = heading)
        obj.writeheader()
        obj.writerows(data_dict)
except Exception as e:
    print(str(e))