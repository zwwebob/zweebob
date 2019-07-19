i = input ("Enter a list, separated by ',':")
m = i.split(',')
for n in m:
    if int(n) % 2 == 0:
        print (n, end=",")