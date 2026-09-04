# For this project we are creating an E-Commerce Engine for Apple that trakcs orders from customers and also keeps an inventory (dictionary) in check
# Dictonaries will be used for the inventory
# Lists will be used for incoming orders
# Sets will be used for unique customer names
# Functions will be used for the actions of the customers

def place_order(inv):
    username = input("\nYou are placing an order. What's your name? ")
    print(f"\nWelcome {username}! Here is the selection of products here at Apple:")
    while True:
        print("\n")

        for prod_id, prod_specs in inv.items():
            print(f"{prod_id}. {prod_specs["model"]}")

        order_num_input = input('Which product would you like to order? (Input the product number) (e to exit):  ')

        if order_num_input == ("e"):    # Exiting "place_order" func
            return None, None


        # User input error checking
        try:
            order_num = int(order_num_input)
        except ValueError:
            print("\nPlease select a number or 'e' to exit")
            continue


        # Exception Handling
        if order_num in inv:
            print("\nProduct found.")
        else:
            print("\nPlease input a number from the list of products.")
            continue

        user_prod = inv[order_num]      # User order is now fully loaded

        while True:
            # User orders amount of units and sees stock price
            user_units_input = input(f"\nHow many units would you like to buy? There are {user_prod["stock"]} units in stock. (Enter a number): ")
            try:
                user_units = int(user_units_input)
            except ValueError:
                print("Please select a number.")
                continue

            if user_units <= 0:
                print("Please select a valid number of units.")
                continue

            if user_prod["stock"] - user_units <= 0:
                print("\n We do not have enough stock. Please select a number of units that we currently have.")
                continue



            # Describing user's choice
            print(f"""\nYou chose the {user_prod["model"]}.
Storage: {user_prod["storage"]}
Price: ${user_prod["price"]}
Units: {user_units}
Final Price: ${user_prod["price"] * user_units}
    """)
            if user_prod["stock"] < 100:
                print(f"Hurry, only {user_prod["stock"]} left in stock!")


        # User places order & handoff to main func
            while True:
                order_yn = input("Would you like to order this item? (y/n): ")
                if order_yn == "y":
                    print(f"\nOrder for {user_prod["model"]} placed. Thank you {username}!")
                    user_order = (username, inv[order_num])
                    user_prod["stock"] = user_prod["stock"] - user_units
                    return user_order, username
                if order_yn == "n":
                    break

                else:
                    print("\nPlease enter either y or n")
                    continue

def show_inventory(inv):
    for prod_id, prod_specs in inv.items():
        print(f"{prod_specs["model"]} --- Storage: {prod_specs["storage"]} --- Price: ${prod_specs["price"]} --- Units left: {prod_specs["stock"]}\n")


def main():
    # Dictionary of models in inventory.
    inventory = {
        1: {'model': "Iphone 15 Pro Max", 'storage': "512GB", "price": 600, "stock": 550},
        2: {'model': "Iphone 16", "storage" : "128GB", "price": 700, "stock": 260},
        3: {'model': "Iphone 16 Pro", "storage" : "256GB", "price": 900, "stock": 400},
        4: {'model': "Iphone 17 Pro Max", "storage": "512GB", "price": 1900, "stock": 500}}

    order_queue = []

    customers = []

    unique_customers = set(customers)

    while True: # using var for loop
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        user_dir_1st_input = input("""\nWelcome to Apple.com, would you like to:

    1. Go to store
    2. Enter password (if admin)

Please input the number associated with your choice (q to quit): """)
        if user_dir_1st_input == "q":
            print("\n Thank you for visiting Apple. We hope to see you again soon.")
            return

        try:
            user_1st_dir = int(user_dir_1st_input)
        except ValueError:
            print("\n Please input a number or 'q' to quit.")
            continue


        if user_1st_dir == 1:   # Now in the user section
            while True:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                customer_dir_input = input("""\nWelcome to the Apple Store, would you like to:

    1. Place an order
    2. View our inventory

Please input the number associated with your choice (e to exit): """)
                if customer_dir_input == "e":
                    print("\nYou are exiting to the main menu...")
                    break
                try:
                    customer_dir = int(customer_dir_input)
                except ValueError:
                    print("Please input a number.")
                    continue

                if customer_dir == 1:
                    user_order, username = place_order(inventory)
                    if user_order is not None:
                        order_queue.append(user_order)
                        customers.append(username)
                        unique_customers.add(username)

                elif customer_dir == 2:
                    show_inventory(inventory)


        if user_1st_dir == 2: # Now in the admin section
            while True:
                password = input("Input your password (e to exit): ")

                if password == "e":
                    print("Returning to the main menu.")
                    break

                if password == "ecomscript105":
                    while True:
                        admin_dir_input = input("""\nWelcome Admin! Would you like to:

        1. View customer queue
        2. View our inventory
        3. View unique customers

Please input the number associated with your choice: (e to exit)""")

                        if admin_dir_input == "e":
                            break

                        try:
                            admin_dir = int(admin_dir_input)
                        except ValueError:
                            print("Please input a number or e to exit")
                            continue

                        # if admin_dir == 1:
                            # Print Customer queue

                        # if admin_dir == 2:
                            # Print inventory

                        # if admin_dir == 3:
                            # Print unique customers

                else:
                    print("Please input the correct password.")
                    continue



main()
