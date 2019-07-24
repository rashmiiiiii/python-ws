#dictionary
names = ["pkm","aln","pvr","pkm","pln","cs"]
c_names = dict()
for name in names:
    if c_names.get(name) == None:
        c_names[name] = 1
    else:
        c_names[name] = c_names[name] + 1
print(c_names)
