def cast_vote(age):
    assert age >= 18 ,f"Age shouldn't be less than 18,it was {age}"
    print("thank you for voting")
try:
    age = int(input("enter the age"))
    cast_vote(age)
    
except AssertionError as e:
    print(e)
else:                             #else block will get executed only when there is no exception raise
    print("thank you for entering valid age...")
finally:
    print("End")



