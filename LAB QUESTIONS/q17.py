#convert all the folllowing words dfrom singular to plural
lst =['story','emergency','qualify']
for ch in lst:
    if ch.endswith('y'):         #r = ch.replace(i[-1],'ies')
        r = ch.replace('y','ies')
        print(r)
