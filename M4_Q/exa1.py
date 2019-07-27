try:
    num2 = int(input("enter the number2:"))
    num1 = int(input("enter the number1:"))
    print(num1 ** num2)
    print(num1 + num2)
    print(num2 / num1)
    print(f"sum is:"+num1+num2)
except ZeroDivisionError:
    print(f"{num2} can't be divided by zero")
except ValueError:
    print("please enter only numbers...")
except Exception as e:
    print(f"something went wrong {e}")
