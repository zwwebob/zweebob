yob = int(input("your year of birth?"))
age = 2019 - yob
print(age)
if age<=10:                     
    print("Baby")
elif 10<age<18:
    print("Teenager")
else:   
    print("Adult")
