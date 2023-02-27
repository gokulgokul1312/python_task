height=float(input("Your height in M: "))
weight=float(input("Your weight in KG: "))
print("\n")
bmi=weight/height**2
print("Your BMI is {}".format(bmi))
if bmi<18.5:
    print("BMI Category: Underweight")
elif bmi==18.5 or bmi<25:
    print("BMI Category: Normalweight")
elif bmi==25 or bmi<30:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")