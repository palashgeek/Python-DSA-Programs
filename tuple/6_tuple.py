items = (1,2,3,4,5,6,7,8)
target = int(input("enter a target no to check:"))
res = False
for i in range(len(items)):
    if target == items[i]:
        res = True
        break
print(str(res))
    