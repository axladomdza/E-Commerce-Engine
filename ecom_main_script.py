# For this project we are creating an E-Commerce Engine for Apple that trakcs orders from customers and also keeps an inventory (dictionary) in check
# Dictonaries will be used for the inventory
# Lists will be used for incoming orders
# Sets will be used for unique customer names 
# Functions will be used for the actions of the customers

def main():
    # Dictionary of models in inventory.
    inventory = {
        "PROD001": {'model': "Iphone 15 Pro Max", 'storage': "512GB", "price": 600, "stock": 200},
        "PROD002": {'model': "Iphone 16", "storage" : "128GB", "price": 700, "stock": 200},
        "PROD003": {'model': "Iphone 16 Pro", "storage" : "256GB", "price": 900}, 
        "PROD004": {'model': "Iphone 17 Pro Max", "storage": "512GB", "price": 1900}}

    order_queue = [] 

    unique_customers = set()
    
    user_order = input("Do you want to")