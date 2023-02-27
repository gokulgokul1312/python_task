pin=12345
tries=0
print("Wellcome To The Bank Of Mitchell.")
while tries<3:
    entry=int(input("Enter Your Pin: "))
    tries += 1
    if entry==pin:
        print("Pin Accepted. You Have Access To Your Account.")
        break
    else:
        print("Incorrect Pin. Try Again.")
else:
    print("You put the pin 3 times, So your account is locked.")