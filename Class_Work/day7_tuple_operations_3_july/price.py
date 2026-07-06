'''WAP to create a tuple of prices of 10 products. Display the lowest price, highest price, count the number of products where price is greater than 4000.Along with the price you are required to store the name of product also.while displaying lowest price and highest price display the name of product along with the price '''
products = []
for i in range(10):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append((name, price))  # Store as a tuple of (name, price)

lowest_price = min(products)
highest_price = max(products)