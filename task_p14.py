print("Wellcome To The Mitchell's Tiny Adventure")
adv=input("You are in a greepy house! Would you like to go 'upstairs' or into the 'kitchen'?\n")
if adv=="kitchen":
    kit=input("There is long countertop with dirty dishes everywhere.off to one side there is, as you'd expect , a refrigerator. you may open the 'refrigerator' or look in a cabinet.\n")
    if kit=="refrigerator":
        ref=input("Inside the refrigerator you see food and stuff. It looks pretty tasty. Would you like to eat some of the food? (yes or no)\n")
        if ref=="yes":
            print("Survive for long times...")
        elif ref=="no":
            print("You die of starvation.... eventually.")
    if kit=="cabinet":
        cab=input("Are you need salt.\n")
        if cab=="yes":
            print("Yes,I need salt.\n")
        elif cab=="no":
            print("No, I don't need.")
if adv=="upstairs":
    ups=input("Going through the upstairs and you will see bedroom on the right side or go on the left side to balcony.\n")
    if ups=="room":
        print("You take the rest")
    elif ups=="balcony":
        print("you breath fresh air.")