#simple interest
principle = float(input("enter the principle amount:"))
rt = float(input("enter the rate of interest:"))
time = float(input("enter the time:"))
si = (principle * rt * time ) / 100
print(f"simple interest = {si}")