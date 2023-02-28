pin=12345
tries=0
print("WELLCOME TO THE BANK OF MITCHELL\n")
while tries<3:
    entry=int(input("Enter your pin: "))
    tries += 1
    if entry==pin:
        print("Pin Accepted. You Now Have Access To Your Account.")
        break
    else:
        print("Incorrect pin, try again.")