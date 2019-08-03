import re
data = "blue shape red toy green"
data =re.sub('(blue|green|red)','color',data)
print(data)