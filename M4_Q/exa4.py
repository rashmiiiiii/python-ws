class MaxLimitError(Exception):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"

c = 0
def login(username,password):
    global c
    if username == "abc" and password =="cba":
        print("login successful......")
    else:
        print("invalid credentials")
    c += 1
    if c > 2 :
        raise MaxLimitError("you have reached maximum number of attempts...")

login("ABC","ABC")
#login("ac","ca")
#login("zx","xz")
login("abc","cba")
