lst = []
def add(ele):
    lst.append(ele)
def pop():
    if len(lst) == 0:
        print("list is empty")
    else:
        r=lst.pop()
        print(f"element {r} is popped")
def search(ele):
    if len(lst) == 0 :
        print("search not possible")
    else:
        if ele in lst:
            print(f"element{ele} found")
        else:
            print(f"element {ele} not found")
def display():
    if len(lst) == 0:
        print("list empty")
    else:
        for ele in lst:
            print(ele)
while True:
    print("1.add 2.pop 3.search 4.display 5.exit")
    ch = int(input("enter the choice"))
    if ch == 1:
        ele = int(input("enter the element to add"))
        add(ele)
    elif ch == 2:
        pop()
    elif ch == 3:
        ele = int(input("enter the element to search"))
        search(ele)
    elif ch == 4:
        print("elements are:")
        display()
    else:
        break