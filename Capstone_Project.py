while True: 
    try: 
        #making a menu for a table 
        table_number = int(input("Insert your table number correctly: ")) 
        if 1 <= table_number <= 10: 
            print(f"\n Table {table_number} selected successfully!") 
            print("\n" + "-" * 20) 
            print("AKHIM KOPITIAM".upper()) 
            print("----------------") 
            print("1 : Foods")
            print("2 : Dessert") 
            print("3 : Drinks") 
            print("4 : Delete Order") 
            print("5 : Payment") 
            print("6 : Exit") 
            break  
        else: 
            # this line will running if you dont input the correct number 
            print(" TABLE NUMBER MUST BE BETWEEN 1 AND 10") 
    except ValueError:  
        print(" PLEASE INSERT THE CORRECT NUMBER") 
 
#Dict for order and prices 
orders = [] 
menu_prices = { 
    #Food prices 
    "Hokkien Noodles": 30000, 
    "Char Kway Teow": 25000, 
    "Fuyunghai": 30000, 
     
    #Dessert Prices  
    "Wonton": 20000, 
    "Siu Mai": 20000, 
    "Egg Tart": 30000, 

    #Drinks prices 
    "Liang Tea": 5000, 
    "Coffee O": 5000, 
    "Coffee Tarik": 5000 
} 

#Converting price to rupiah 
def price_format(price): 
    return f"Rp {price:,}".replace("," , ".") 
     
#adding some order
def adding_order(menu_name, menu_price): 
    while True:
        try:
            quantity = int(input(f"Enter quantity for {menu_name}: "))
            if quantity > 0:
                orders.append({"Menu Name": menu_name, "Price": menu_price, "Quantity": quantity})
                total_price_item = menu_price * quantity
                print(f"\n{quantity} x {menu_name} has been added to your order!")
                print(f"Subtotal: {price_format(total_price_item)}")
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
# Foods menu 
def foods_menu(): 
    while True: 
        print("\n" + "-" * 30)
        print("FOOD MENU") 
        print("-" * 30) 
        print("1 : Hokkien Noodles - Rp. 30.000") 
        print("2 : Char Kway Teow  - Rp. 25.000")
        print("3 : Fuyunghai       - Rp. 30.000") 
        print("4 : Back to MAIN MENU") 
        print("-" * 30) 
         
        #error handling 
        try:
            choice = int(input("Choose your food (1-4): "))
            if choice == 1:
                adding_order("Hokkien Noodles", menu_prices["Hokkien Noodles"])
                break
            elif choice == 2:
                adding_order("Char Kway Teow", menu_prices["Char Kway Teow"])
                break
            elif choice == 3:
                adding_order("Fuyunghai", menu_prices["Fuyunghai"])
                break
            elif choice == 4:
                print("Returning to main menu")
                break
            else:
                print("INVALID CHOICE! Please Select 1-4.")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
        

#Dessert menu 

def dessert_menu(): 
    while True: 
        print("\n" + "-" * 30)
        print("DESSERT MENU") 
        print("-" * 30) 
        print("1 : Wonton   - Rp. 20.000") 
        print("2 : Siu Mai  - Rp. 20.000")
        print("3 : Egg Tart - Rp. 30.000") 
        print("4 : Back to MAIN MENU") 
        print("-" * 30) 
         
        #error handling 
        try:
            choice = int(input("Choose your dessert (1-4): "))
            if choice == 1:
                adding_order("Wonton", menu_prices["Wonton"])
                break
            elif choice == 2:
                adding_order("Siu Mai", menu_prices["Siu Mai"])
                break
            elif choice == 3:
                adding_order("Egg Tart", menu_prices["Egg Tart"])
                break
            elif choice == 4:
                print("Returning to main menu")
                break
            else:
                print("INVALID CHOICE! Please Select 1-4.")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
             
#Drinks menu
def drinks_menu(): 
    while True: 
        print("\n" + "-" * 30)
        print("DRINKS MENU") 
        print("-" * 30) 
        print("1 : Liang Tea    - Rp. 5.000") 
        print("2 : Coffee O     - Rp. 5.000")
        print("3 : Coffee Tarik - Rp. 5.000") 
        print("4 : Back to MAIN MENU") 
        print("-" * 30) 
         
        #error handling 
        try:
            choice = int(input("Choose your drinks (1-4): "))
            if choice == 1:
                adding_order("Liang Tea", menu_prices["Liang Tea"])
                break
            elif choice == 2:
                adding_order("Coffee O", menu_prices["Coffee O"])
                break
            elif choice == 3:
                adding_order("Coffee Tarik", menu_prices["Coffee Tarik"])
                break
            elif choice == 4:
                print("Returning to main menu")
                break
            else:
                print("INVALID CHOICE! Please Select 1-4.") 
                input("Press Enter to Continue")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!") 
            input("Press Enter to Continue")
#delete order 
def delete_order():
    if not orders: 
        print("\n NO ORDERS YET") 
        return 
    print("\n" + "=" * 50) 
    print("YOUR CURRENT ORDERS:")
    print("-" * 50)
    for i, order in enumerate(orders, 1):
        print(f"{i}. {order['Menu Name']} (x{order['Quantity']})")
    print("-" * 50)

    try:
        choice = int(input("Enter the number of the item you want to delete (or 0 to cancel): "))
        if choice == 0:
            print("Deletion cancelled.")
        elif 1 <= choice <= len(orders):
            removed_item = orders.pop(choice - 1)
            print(f"\n{removed_item['Menu Name']} has been removed from your order.")
        else:
            print("INVALID CHOICE! Please select a valid number.")
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER!")

     
#Payment Function 
def payment(table_number):
    if not orders: 
        print("\n  NO ORDERS TO PAY FOR!") 
        return  
    print("\n" + "=" * 50)  
    print(f" PAYMENT - TABLE {table_number}")  
    print("-" * 50 )  
     
    total = sum(order['Price'] for order in orders) 
    for i, order in enumerate(orders, 1): 
        print(f"{i}. {order['Menu Name']} - {price_format(order['Price'])}") 
    print("-" * 50 )   
    print(f" TOTAL AMOUNT: {price_format(total)}") 
    print("=" * 50) 

    confirm = input("\n Confirm Payment? (y/n): ").lower() 
    if confirm == 'y': 
        print("\n Payment Successful!") 
        print("Receipt has been sent to your email.") 
        print("Your Food will be served shortly!") 
        orders.clear() #to clear orders after payment
    else: 
        print("PAYMENT CANCELLED.") 
         
#main program loop 
def main_program(table_number):
    while True: 
        print("\n" + "-" * 20) 
        print("AKHIM KOPITIAM".upper()) 
        print("----------------") 
        print("1 : Foods")
        print("2 : Dessert") 
        print("3 : Drinks") 
        print("4 : Delete Order") 
        print("5 : Payment") 
        print("6 : Exit")  
        print("-" * 20)   

        try:
            main_choice = int(input("Select Option (1-6): "))
            if main_choice == 1:
             foods_menu()
            elif main_choice == 2:
             dessert_menu()
            elif main_choice == 3:
             drinks_menu()
            elif main_choice == 4:
             delete_order()
            elif main_choice == 5:
                payment(table_number)
            elif main_choice == 6:
                if orders:
                    confirm_exit = input("YOU HAVE UNPAID ORDERS. Are you sure you want to exit? (y/n): ").lower()
                    if confirm_exit == 'y':
                        print("Thank you for visiting! Have a great day!")
                        break
                else:
                    print("Thank you for visiting! Have a great day!")
                    break
            else:
                print("INVALID CHOICE! Please Select 1-6.") 
                input("\nPress Enter to continue...")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
            input("\nPress Enter to continue...")

# run the main program
if __name__ == "__main__": 
    main_program(table_number)
     
     