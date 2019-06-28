# check = True

# while check:
#      txt = input("enter a number")
#      if txt.isdigit():
#           inputLength = txt.length()
#           print("a number")
#           check = False
#      elif txt.isalpha():
#         print("not a number")

txt = input("Enter your number")

if txt.isdigit():
     checkInput = len(txt)
     print(checkInput)
else:
     print("try AGAIN")