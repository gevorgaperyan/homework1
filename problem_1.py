n = [5, 1, 2, 1, 4,]
newList = set()
for i in n:
    if n.count(i) >= 2:
        newList.add(i)
print(list(newList))



n = [4, 1, 2]
newlist = []
duplist = []
a = None

for i in n:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)
print("List of duplicates", a)
print("List of unique", newlist)       

n = []
newlist = []
duplist = []
a = None

for i in n:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)

print("List of duplicates", a)
print("List of unique", newlist)


n = [6, 2, 5, 2, 6, 2]
newList = set()
for i in n:
    if n.count(i) >= 2:
        newList.add(i)
print(list(newList))

n = [42, 42, 42, 42]
newList = set()

for i in n:
    if n.count(i) >= 2:
        newList.add(i)
print(list(newList))        