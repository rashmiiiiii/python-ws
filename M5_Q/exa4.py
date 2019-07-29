#using json
import json
data_dict = [
      {"id":1001,"wname":"python","year":"2019","status":1,"company":"hearizen"},
      {"id":1002,"wname":"web","year":"2018","status":0,"company":"spaneos"}
      ]
    
try:
    with open("ws3.json","w",newline = '') as file:
        json.dump(data_dict,file,indent = 4)
        
except Exception as e:
    print(str(e))

#dump -  writting into the file
#dumps - returns string json object
#json.dumps(dat_dict,file,indent = 4)
#json is used when data needs to be exchanged between the two servers