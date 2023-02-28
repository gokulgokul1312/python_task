print("I will add up the numbers you give me.\n")
sum=0
num=int(input("Enter the number:\n"))
print("The total so far is {}".format(num+sum))
while num != 0:
    sum += num
    num=int(input("Enter the number:\n"))
    print("The total so far is {}".format(num+sum))
print("The total is {}".format(sum))
