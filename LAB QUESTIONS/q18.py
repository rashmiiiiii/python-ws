dic ={}
def add(p_id,name):
    dic[p_id] = name
def display():
    if len(dic) == 0:
        print("dictionary is empty")
    else:
        for k,v in dic.items():
            print(f"{k},{v}")
def search(p_id):
    if len(dic) == 0:
        print("dictionary is empty")
    else:
        for k in dic:
            if k == p_id:
                print(f"product id {p_id} value {dic[p_id]}is found")
            else:
                print(f"{p_id} is not found")
    
while True:
    print("1.Add 2.Display 3.Search")
    ch = int(input("enter the choice:"))
    if ch == 1:
        p_id = int(input("enter the product id:"))
        name = input("enter the name:")
        add(p_id,name)
    elif ch == 2:
        display()
    elif ch == 3:
        p_id = int(input("enter the product id to search:"))
        search(p_id)
    else:
        exit(0)
