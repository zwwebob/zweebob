from random import randint

auto = randint(0, 100)

print(auto)
if auto<30:
    print("rainy")
elif 30<= auto <60:
    print("cloudy")
elif auto>=60:
    print("sunny")