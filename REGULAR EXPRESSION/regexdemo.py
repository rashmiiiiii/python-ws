import re
data = "House number 198 and pincode 560070"
res = re.search(r"\d+", data)
print(data[res.start():res.end()])
print()
