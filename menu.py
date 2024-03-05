# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# create a dictionary named order list with values for item_name, item price and order quantity
# create variables for item name, item price and item quantity
order_list= {}
item_name= input()
# def select_catagory():
#     while True:
#         print("Snacks, Meals, Drinks, or Dessert?")
#         menu_selection = input()
#         if menu_selection in menu.keys():
#             return menu_selection
#         else:
#             print("Please enter a valid option")
# def get_selection():
#     print(menu.select_catagory.keys())
#     menu_item = input(f"which {select_catagory()} would you like to order?")
#     print(menu.select_catagory.values())
#     if menu_item in menu.select_catagory.keys():
#         return menu_item
#     else:
#         print("Please enter a valid option")
# def get_item_quantity():
#     print(menu.select_catagory.keys())
#     quantity = input(f"How many {get_selection()} would you like to order?")
#     print(menu.select_catagory.values())
#     if menu_item in menu.select_catagory.keys():
#         return menu_item
#     else:
#         print("Please enter a valid option")

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    print(menu.keys())
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input(f'what {menu_category_name} item would you like to order?')

            # 3. Check if the customer typed a number
            if bool(menu_selection.isdigit()):
                print("lalalal")

                # Convert the menu selection to an integer
                menu_secection = int(menu_selection)

                # 4. Check if the menu selection is in the menu itemsn
                if menu_secection in menu_items.keys():


                    # Store the item name as a variable
                    item_name = menu_items[menu_secection]["Item name"]

                    # Store the item price as a variable
                    item_price = menu_items[menu_secection]["Price"]

                    # Print out the item name and price
                    quantity = input(f"How many {item_name} for ${item_price} would you like? input will default to 1 if a valid number is not entered: ")

                    # Ask the customer for the quantity of the menu item
                    if quantity.isdigit():

                        # Convert the quantity to an integer
                        quantity = int(quantity)

                        # 5. Check if the quantity is valid
                        if quantity > 0:
                            total_price = item_price * quantity

                            # Add the item name, price, and quantity to the order list
                            order_list = {"Item Name":item_name,"Item Price":total_price,"Item Quantity":quantity}

                            # Tell the customer that their input is valid
                            print(f"You ordered {quantity} {item_name} for ${total_price}.")

                             # Tell the customer that their input isn't valid
                        else:
                            print("please enter a valid quantity")
                       
                    # Tell the customer that their input isn't valid
                    else:
                        order_list = {"Name" : item_name, "Item Price" : item_price, "Item Quantity" : 1}

                #tell the customer to enter a number in the menu
                else:
                    print("Please enter a number in the menu")
            
            #tell the customer to enter a digit
            else:
                print("please enter a digit")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while place_order:
        # Ask the customer if they would like to order anything else
        keep_ordering = bool(input("Press enter to exit or anything else to keep ordering: "))

        # 5. Check the customer's input
        # if keep_ordering.lower() != "y" and keep_ordering.lower() != "n":
        #     print("Please say (Y)es or (N)o")
        if keep_ordering == False:
            # Exit the keep ordering question loop
            place_order = False
            break

                # Complete the order, 
        

                # Since the customer decided to stop ordering, thank them for
                # their order
        print("Thank you for your order")

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
# 9. Create space strings
item_spaces = 26 - len(item_name)
quantity_spaces = 10 - len(str(order_list["Item Quantity"]))
# 6. Loop through the items in the customer's order
for key in order_list:
    key2 = order_list["Item Price"]
    key3 = order_list["Item Quantity"]
    price = key2 * key3
    price_spaces = 8 - len(str(price))
    # 7. Store the dictionary items as variables
    # 8. Calculate the number of spaces for formatted printing
    # 10. Print the item name, price, and quantity
    item_spaces = 26 - len(item_name)
    print(f'{item_name} {(26 - len(item_name))}|{price}{price_spaces - len(str(price))}|{quantity_spaces - len(str(quantity))}')

# 11. Calculate the cost of the order using list comprehension
for key in order_list["Item Price"]:
    #add up the values of the Price key in order list
    total = 0
    total += order_list["Item Price"].value()
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print(f"Your Total is total {total}")
