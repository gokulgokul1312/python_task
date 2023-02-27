print("Ye Olde Keychains Shoppe\n")

def add_keychains():
    print("Add keychains.\n")
def remove_keychains():
    print("Remove keychains.\n")
def view_order():
    print("View order.\n")
def checkout():
    print("Checkout.\n")

while True:
    print("1. Add keychains to order.")
    print("2. Remove keychains from order.")
    print("3. View current order.")
    print("4. Checkout.\n")
    choice=int(input("Please enter your choice: "))
    print("\n")
    if choice==1:
        add_keychains()
    if choice==2:
        remove_keychains()
    if choice==3:
        view_order()
    if choice==4:
        checkout()
        break
else:
    print("Please enter invalid number.")