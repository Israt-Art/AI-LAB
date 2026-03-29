"""Problem 8: Dictionary Filtering
1 Given products = {'Laptop':1200,'Phone':800,'Tablet':450,'Monitor':300,'Keyboard':100}.
2 Create a new dictionary containing only products with price greater than 500."""

products = {
    'Laptop': 1200,
    'Phone': 800,
    'Tablet': 450,
    'Monitor': 300,
    'Keyboard': 100
}

expensive_products = {}


keys = list(products.keys())

for i in range(len(keys)):
    product = keys[i]       
    price = products[product]  
    
    if price > 500:
        expensive_products[product] = price

print("Products with price > 500:", expensive_products)



#another way



products = {'Laptop': 1200, 'Phone': 800, 'Tablet': 450, 'Monitor': 300, 'Keyboard': 100}


expensive_products = {} 

for product, price in products.items():
    if price > 500:
        expensive_products[product] = price


print("Products with price > 500:", expensive_products)






