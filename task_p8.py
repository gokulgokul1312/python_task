name=input("What's your name? ")
age=int(input("Ok, {}, how old are you? ".format(name)))
if age<16:
    print("You can't drive.")
    print("You can't vote")
    print("You can't rent a car")
elif age<18:
    print("You can drive but You can't vote.")
else:
    print("You can't rent a car")

