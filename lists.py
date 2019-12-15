list = []
list.append("house")
list.append("mouse")
list.append("blouse")
print(list)
print(len(list))
print(list[1])
list.insert(1,"grouse")
print(list)
del(list[1])
print(list)

list2 =[]
list2.append("house")
list2.append("mouse")
list2.append("blouse")

list.extend(list2)
print(list)

list3 = list + list2
print(list3)

# matrix
list4 = []
list4.append(list2)
list4.append(list2)
print(list4)
print(list4[1][2])

list4[0] = 4
print(list4)