print("Two Questions!")
print("Think of an object, and I'll try to guess it.")
print("\n")
q1=input("Q1) It is animal, vegetable, or mineral?\n")
print("\n")
q2=input("Q2) It is bigger than a breadbox?\n")
print("\n")
if q1=="animal":
    if q2=="no":
        print("My guess is that you are thinking of a squirrel.")
    else:
        print("My guess is that you are thinking of a moose.")
elif q1=="mineral":
    if q2=="yes":
        print("My guess is that you are thinking of a camaro.")
    else:
        print("My guess is that you are thinking of a paper clip")
elif q1=="vegetable":
    if q2=="yes":
        print("My guess is that you are thinking of a watermelon.")
    else:
        print("My guess is that you are thinking of a carrot.")
print("I would ask you it I'm right, but I dont't actually care.")