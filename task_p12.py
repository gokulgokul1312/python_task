quiz=input("Are you for a quiz? ")
if quiz=="yes":
    print("here it comes")
else:
    print("quit the quiz")
    
print("Q1) What is the capital of Alaska?")
print("  1)Melbourne")
print("  2)London")
print("  3)Juneau")

q1=int(input())
if q1==1:
    print("It's wrong answer.\n")
elif q1==2:
    print("That's wrong answer.\n")
elif q1==3:
    print("It's correct answer.\n")
else:
    print("Please enter invalid number.\n")

print("Q2) Can you store the value 'cat' in a variable of type int?")
print("  1) yes")
print("  2) no")

q2=int(input())
if q2==2:
    print("That's correct answer.\n")
elif q2==1:
    print("Sorry, cat is a string. ints can only store numbers.\n")
else:
    print("Please enter invalid number.\n")

print("Q3) What is the result of 9+6/3?")
print("   1)5")
print("   2)11")
print("   3)15/3")

q3=int(input())
if q3==1:
    print("wrong, Simply waste!\n")
elif q3==3:
    print("wrong answer\n")
elif q3==2:
    print("Perfect, It's a correct answer.\n")
else:
    print("Please enter invalid number.\n")

def result():
    if q1==3 and q2==2 and q3==2:
        print("Overall ,you got 3 out of 3......congragulations!!!!")
    elif q1==3 and q2==2:
        print("Overall ,you got 2 out of 3")
    elif q1==3 and q3==2:
        print("Overall ,you got 2 out of 3")
    elif q3==2 and q2==3:
        print("Overall ,you got 2 out of 3")
    elif q1==3 or q2==2 or q3==2:
        print("Overall ,you got 1 out of 3")
    else:
        print("OOPS!!!sorry yoo got 0 out of 3")
result() 
