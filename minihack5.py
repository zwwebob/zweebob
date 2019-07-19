a = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
b = [150300, 247100, 333300, 266800, 420900, 318000] 
print(a)
print(b)
print(max(b))
print(min(b))
n = len(b)
for m in range(n):
    if b[m] == max(b):
        print ("Quan co dan so lon nhat:", a[m])
for m in range(n):
    if b[m] == min(b):
        print ("Quan co dan so nho nhat:", a[m])
