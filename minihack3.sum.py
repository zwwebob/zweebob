items = [12, 45, 23, 27, 69, 40, -52]
x = sum(items)
print(x)

cal = 0
for i in range(len(items)):
    cal = cal + items[i]
    print(cal)