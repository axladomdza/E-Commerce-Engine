# For this project we are creating an E-Commerce Engine for Apple that trakcs orders from customers and also keeps an inventory (dictionary) in check
# Dictonaries will be used for the inventory
# Lists will be used for incoming orders
# Sets will be used for unique customer names
# Functions will be used for the actions of the customers


def place_order(inv):
    order_process = True
    username = input("\nYou are placing an order. What's your name? ") 

    print(f"Welcome {username}! Here is the selection of products here at Apple:")

    while order_process:
    #Printing product list and prompting user to choose
        for prod_num, (product_id, prod_specs) in enumerate(inv.items(), start =1):
            print(prod_specs)
            print(f"{prod_num}. {prod_specs["model"]}")
        order_num_input = input('Which product would you like to order? (Input the product number):  ')
        try:
            order_num = int(order_num_input)
        except ValueError:
            print("\nPlease select a number.")
            continue

    #Error handling user input
        if 1 <= order_num <= len(inv):
            print("\nNumber found." )
        else:
            print("\nPlease input a number from the list of products.")
            continue

    #Describing info to user from product
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
        order_yn = input("Would you like to order this item? (y/n)")
        if order_yn == "y":
            print(f"Order placed. Thank you {username}!")
            user_order = (username, inv[order_num])
            order_process = False 
            return user_order
            
        if order_yn == "n":
            continue 
            
        




running = True  #introducing a variable to loop the main function

def main(): 
    # Dictionary of models in inventory.
    inventory = {
        "PROD001": {'model': "Iphone 15 Pro Max", 'storage': "512GB", "price": 600, "stock": 550},
        "PROD002": {'model': "Iphone 16", "storage" : "128GB", "price": 700, "stock": 260},
        "PROD003": {'model': "Iphone 16 Pro", "storage" : "256GB", "price": 900, "stock": 400},
        "PROD004": {'model': "Iphone 17 Pro Max", "storage": "512GB", "price": 1900, "stock": 500}}

    order_queue = []

    unique_customers = set()

    print("You're placing an order. Which Iphone fits best for you:")
    while running:      #using earlier variable for the loop
        user_direction_input = input("""Welcome to Apple.com, would you like to:

1. Place an order
2. View our inventory

Please input the number associated with your choice: """)

        try:
            user_direction = int(user_direction_input)
        except ValueError:
            print("Please input a number")
            continue

        if user_direction == 1:
            place_order(inventory)
            order_queue.append(user_order)

main()