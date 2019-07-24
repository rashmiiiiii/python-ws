def result(name,*args):
    res = 0
    for i in args:
        res += i
    print(f"name:{name} total:{res}")

result("rajesh",56,96,63,89)