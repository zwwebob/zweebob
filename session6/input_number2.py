while True:
    txt = input("please enter your password?")
    print(txt)
    if ((txt.isalpha() == False) and len(txt) >= 8):
        print("the password is correct")
        break
    else:
        print("the password is incorrect")