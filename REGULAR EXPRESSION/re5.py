import re
emails = """krishna.t@wipro.com
    lakshman.a@spaneos.com
    lakshman.a@heraizen.edu"""
lst = re.findall(r"@([A-z]+).",emails)
print(lst)
