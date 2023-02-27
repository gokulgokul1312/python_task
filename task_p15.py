l1=["inside", "outside", "both"]
l2=["yes", "no"]
print("Two more questions, Baby!\n")
print("Think of something and I'll try to guess it!\n")
q1=input("Q1) Does it stay inside or outside or both? ")
q2=input("Q2) Is it a living thing? ")
if q1=="inside" and q2=="yes":
    print("It is a house plant.")
if q1=="outside" and q2=="yes":
    print("It is a bison.")
if q1=="both" and q2=="yes":
    print("It is a dog.")
if q1=="inside" and q2=="no":
    print("It is a shower curten.")
if q1=="outside" and q2=="no":
    print("It is a billboard.")
if q1=="both" and  q2=="no":
    print("It is a cell phone.")
if (q1 not in l1) or (q2 not in l2):
    print("Sorry I could't guess it what are you thinking of")