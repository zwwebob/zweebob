color = ["blue", "red",'teal','green']
print(color)
#create(2)
#i = int(input("Enter a position:"))
#print(color[i])
#delete
i = input("color to delete:")
if i.isalpha():
    color.remove(i)
    print("Our new color list:")
    print(color)
elif i.isdigit():
    color.pop(int(i))
    print("Our new color list:")
    print(color)
