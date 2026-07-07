'''Inventory Management
Problem Statement:
Create a dictionary to maintain the stock of products in a shop.
Example:
{
'Laptop': 15,
'Mouse': 40,
'Keyboard': 25,
'Monitor': 10
}
Implement the following:
• Add a new product.
• Update the stock of an existing product.
• Remove a product from inventory.
• Display products having stock less than 20.
• Display the total number of items available in the inventory'''
dict = {}
# Input initial stock for 5 products
for i in range(5):
    product_name = input(f"Enter name of product {i + 1}: ")
    stock = int(input(f"Enter stock for {product_name}: "))
    dict[product_name] = stock
    print(f"Added {product_name} with stock {stock}.")
# Add a new product
new_product = input("\nEnter name of new product to add: ")
new_stock = int(input(f"Enter stock for {new_product}: "))
dict[new_product] = new_stock
print(f"Added {new_product} with stock {new_stock}.")
# Update the stock of an existing product
update_product = input("\nEnter name of product to update stock: ")
if update_product in dict:
    updated_stock = int(input(f"Enter new stock for {update_product}: "))
    dict[update_product] = updated_stock
    print(f"Updated {update_product}'s stock to {updated_stock}.")
else:
    print(f"Product {update_product} not found.")
# Remove a product from inventory
remove_product = input("\nEnter name of product to remove: ")
if remove_product in dict:
    del dict[remove_product]
    print(f"Removed product {remove_product} from inventory.")
else:
    print(f"Product {remove_product} not found.")
# Display products having stock less than 20
print("\nProducts with stock less than 20:")
for product, stock in dict.items():
    if stock < 20:
        print(f"{product}: {stock}")
# Display the total number of items available in the inventory
total_items = sum(dict.values())
print(f"\nTotal number of items in inventory: {total_items}")
