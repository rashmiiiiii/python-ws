while True:
    str = input("enter the sentence:")
    if str == 'done' :
        break
    if str[-1] == '?':                     #if str.endswith('?'):
        print("interrogative statement")
    else:
        print("asertive statement")

