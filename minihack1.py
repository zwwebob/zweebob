color = ["blue", "red",'teal','green']
#init color list
print(color)
#print color list
print("Our color list:")
print(*color, sep=",")
#create
new_items = input("Enter a new color:")
color.append(new_items)
print("Our new color list:")
print(*color, sep=",")