gender=input("What is your gender (M or F): ")
Fname=input("First name: ")
Lname=input("Last name: ")
age=int(input("age: "))
print("\n")
if gender=="female" and age>=20:
    married=input("Are you married, {} (Y or N)? ".format(Fname))
    if married=="yes":
        print("Then I shall call you Mrs.{}.".format(Fname))
    else:
        print("Then I shall call you Ms.{}".format(Fname))
if gender=="male" and age>=20:
    print("Then I shall call Mr.{}".format(Fname))
elif (gender=="female" or gender=="male") and age<20:
    print("I call {} {}.".format(Fname,Lname))
