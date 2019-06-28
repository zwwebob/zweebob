while True:
    txt = input("please enter your password?")
    print(txt)
    if txt.isdigit():
         print("the password is correct")
         break
    else:
        print("the password is incorrect")
        