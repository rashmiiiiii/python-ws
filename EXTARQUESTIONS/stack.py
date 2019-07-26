class Stack:
    def __init__(self):
        self.st = [ ]
    
    def push(self,ele):
        self.st.append(ele)
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            ele = self.st.pop()   #queue self.st.pop(0)
            print(f"element {ele} is removed from the stack")
    def search(self,searchele):
        if self.is_empty():
            print("stack is empty")
        else:
            for index,ele in enumerate(self.st):
                if ele == searchele:
                    return index
            return -1
        
    def  show(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.st)


    def is_empty(self):
        return len(self.st) == 0

if __name__ == "__main__":
    st = Stack()
    while True:
        print("1.push 2.pop 3.display 4.search 5.exit")
        try:
            ch = int(input("enter your choice:"))
            if ch == 1:
                ele = int(input("enter the element to be pushed:"))
                st.push(ele)
            elif ch == 2:
                st.pop()
            elif ch == 3:
                st.show()
            elif ch == 4:
                ele = int(input("enter the element to be search:"))
                res = st.search(ele)
                if res != -1:
                    print(f"element {ele} found at location:{res}")
                else:
                    print(f"element {ele} not found")
            
            elif ch == 5:
                exit()
            else:
                raise ValueError
        except ValueError:
            print("enter the numbers only 1 to 5")

'''# opt_dic = { 1:st.push,2:st.pop,3:st.search,4:st.show,5:exit}
   # while True:
   #    print("1.push 2.pop 3.display 4.search 5.exit")
   #    try:
   #        ch = int(input("enter your choice:"))
   #        ref = opt_dic[ch]
   #       ref()
   #  except(ValueError,KeyError):
   #      print("enter only numbers 1 to 5")
   #  except:
   #     print("something went wrong")'''