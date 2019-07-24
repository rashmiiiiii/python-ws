data ="rajesh,krish,ramesh,suresh"
print(list(map(lambda x:x.capitalize(),data.split(","))))

#to filter the names start with "A"
#x=list(map(lambda x:x.capitalize(),data.split(",")))
#print(list(filter(lambda x:x.startswith("A"),x)))