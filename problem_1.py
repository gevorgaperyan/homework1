n = [5, 1, 2, 1, 4]

#print(target)#

for i in n:
    for j in n:
        if i==j & n.index(i) != n.index(j):
            print("index: ", n.index(i), "number: ",i) 
            break
    else:
        continue  # print("None")  only executed if the inner loop did NOT break
    break