items = [12, 45, 23, 27, 69, 40, -52]
i = int(input("Enter a number:"))
if i in items:
    print(items.index(i)) 
else:
    print("Not found in the list")

    