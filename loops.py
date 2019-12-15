# 42:00
# loops

x = 0
while x < 5:
    print(x, end = ' ')
    x+=1
print('cabou while')

for i in range(5):
    print(i, end = ' ')
print('cabou for i')

for j in range(0,10,2):
    print(j, end=' ')
print('cabou for j')

list = [1, 2, 3, 4]
for x in list:
    if (x == 3):
        continue
    print(x, end=' ')
print('cabou for list')

for x in range(5):
    if x == 3:
        break
else:
    print('entered else')
