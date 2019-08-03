import re
data = "1001 DBMS 20   1002 JS 23   1003 SQL 15"
#O/P: [('1001','DBMS','20'),('1002','JS','23'),('1003','SQL','15')]
lst = re.findall(r'(\d{4})\s([A-Z]*)\s+(\d{2})',data)
print(lst)