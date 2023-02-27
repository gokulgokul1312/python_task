name=input("Hey, What's your name? (Sorry, I keep forgetting.)")
age=int(input("Ok, {}, How old are you?".format(name)))
if age<16:
    print("You can't drive.")
elif age==16 or age==17:
    print("You can drive but not vote.")
elif age==18 or age<25:
    print("You can vote but not rent a car.")
else:
    print("You can do pretty much anything.")