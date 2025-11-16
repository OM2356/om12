#RESTAURAT MANU ORDERING SYSTEM
menu={
    "Burger":50,
    "Pizza":180,
    "Pasta":60,
    "Salad":40,
    "Fries":45,
    "Soda":30
}
# function to display the menu
def diaplay_menu():
    print("\n----menu----")
    for item,price in menu.items():
        print(f"{item}:₹{price:.2f}")

def take_order():
    order={}
    while True:
        diaplay_menu()
        choice=input("Please enter the name of the item you'd like to order(or 'Done' to finish):").capitalize()
        if choice =='Done':
            break
        elif choice in menu:
            quantity=int(input(f"How many{choice}s world you like?"))
            if choice in order:
                order[choice]+=quantity
            else:
                order[choice]=quantity
        else:
            print("Item not available on the menu .please choose again.")
    return order
def calculate_bill(order):
    total=0
    print("\n---Receipt---")
    for item,quantity in order.items():
        price=menu[item]*quantity
        total+=price
        print(f"{item}x{quantity}:₹{price:.2f}")
    print(f"Total:₹{total:.2f}")
    return total

def main():
    print("Welcome to the Resturant!")
    order=take_order()
    if order:
        calculate_bill(order) 
    else:
        print("No items were ordered.")
    print("Thank you for visiting!")

if __name__ =="__main__":
    main()                              
          
