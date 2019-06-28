while True:
    txt = input("enter your name?")
    print(txt)
    if txt.isdigit():
         print("this is not a name")
    else:
        print("this is your name")
        break