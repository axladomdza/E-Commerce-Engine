# For this project we are creating an E-Commerce Engine for Apple that trakcs orders from customers and also keeps an inventory (dictionary) in check
# Dictonaries will be used for the inventory
# Lists will be used for incoming orders
# Sets will be used for unique customer names
# Functions will be used for the actions of the customers

def place_order(inv):
    order_process = True
    username = input("\nYou are placing an order. What's your name? ")

    print(f"\nWelcome {username}! Here is the selection of products here at Apple:")

    while order_process:
        print("\n")
    #Printing product list and prompting user to choose
        for prod_num, (prod_id, prod_specs) in enumerate(inv.items(), start =1):
            print(f"{prod_id}. {prod_specs["model"]}")
        order_num_input = input('Which product would you like to order? (Input the product number) (e to exit):  ')

        if order_num_input == ("e"):
            return 'None', 'None'

        # User input error checking
        try:
            order_num = int(order_num_input)
        except ValueError:
            print("\nPlease select a number or 'e' to exit")
            continue
    # Exception Handling
        if 1 <= order_num <= len(inv):
            print("\nProduct found.")
        else:
            print("\nPlease input a number from the list of products.")
            continue

    # Describing user's choice
        user_prod = inv[order_num]
        print(f"""You chose the {user_prod["model"]}.
Storage: {user_prod["storage"]}
Price: {user_prod["price"]}
""")
        if user_prod["stock"] < 100:
            print(f"Hurry, only {user_prod["stock"]} left in stock!")
        else:
            print(f"{user_prod["stock"]} left in stock.")

    # User places order & handoff to main func
        while True:
            order_yn = input("Would you like to order this item? (y/n): ")
            if order_yn == "y":
                print(f"\nOrder for {user_prod["model"]} placed. Thank you {username}!")
                user_order = (username, inv[order_num])
                user_prod["stock"] = user_prod["stock"] - 1
                order_process = False
                return user_order, username
            if order_yn == "n":
                break

            else:
                print("\nPlease enter either y or n")
            continue

def show_inventory(inv):
    for prod_num, (prod_num1, prod_specs) in inv:
        print(f"{}")








running = True  # Introducing a variable to loop the main function

def main():
    # Dictionary of models in inventory.
    inventory = {
        1: {'model': "Iphone 15 Pro Max", 'storage': "512GB", "price": "$600", "stock": 550},
        2: {'model': "Iphone 16", "storage" : "128GB", "price": "$700", "stock": 260},
        3: {'model': "Iphone 16 Pro", "storage" : "256GB", "price": "$900", "stock": 400},
        4: {'model': "Iphone 17 Pro Max", "storage": "512GB", "price": "$1900", "stock": 500}}

    order_queue = []

    customers = []

    unique_customers = set(customers)

    while running:      #using earlier variable for the loop
        user_direction_input = input("""\nWelcome to Apple.com, would you like to:

1. Place an order
2. View our inventory

Please input the number associated with your choice: """)

        try:
            user_direction = int(user_direction_input)
        except ValueError:
            print("Please input a number")
            continue

        if user_direction == 1:
            user_order, username = place_order(inventory)
            if user_order is not None:
                order_queue.append(user_order)
                customers.append(username)
                unique_customers.add(username)
                continue

        if user_direction == 2:
            show_inventory(inventory)


main()
