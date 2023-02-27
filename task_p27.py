print("Ye Olde Keychain Shoppe\n")

add=0
reduce=0
price=0

def add_keychains():
    global add
    global reduce
    add=int(input("You have {} keychains. How many to add? ".format(reduce)))
    reduce +=add 
    print("You now have {} keychains.".format(reduce))

def remove_keychain():
    global reduce
    remove=int(input("You have {} keychains. How many to remove? ".format(reduce)))
    reduce -=remove
    print("You have {} keychains.".format(reduce))

def view_order():
    global reduce
    global price
    price=10*reduce
    print("You have {}.".format(reduce))
    print("Keychains start $10 each.")
    print("Total price is ${}.".format(price))

def check_out():
    name=input("What is your name? ")
    print("You have {} keychains.")
    print("Keychains cost $10 each.")
    print("Total cost is ${}.".format(price))
    print("Thanks for your order, {}!".format(name))

while True:
    print("1. Add keychains to order.")
    print("2. romove keychins from order.")
    print("3. view current order.")
    print("4. Checkout")
    choice=int(input("Please enter your choice: "))
    if choice==1:
        add_keychains()
    elif choice==2:
        remove_keychain()
    elif choice==3:
        view_order()
    elif choice==4:
        check_out()
        break
    else:
        print("Please enter invalid number.")