# For this project we are creating an E-Commerce Engine for Apple that trakcs orders from customers and also keeps an inventory (dictionary) in check
# Dictonaries will be used for the inventory
# Lists will be used for incoming orders
# Sets will be used for unique customer names
# Functions will be used for the actions of the customers


def place_order(inv, queue):
    print("\nYou are placing an order. Here is the selection of products here at Apple:")
    for product_id, prod_specs in inv.items():
        print(prod_specs["model"])




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
            place_order(inventory, order_queue)

main()
