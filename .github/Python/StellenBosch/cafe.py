# Craete a list containing 4 items i sell in my cafe, and cast to the variable 'menu'
menu = ['coffee', 'tea', 'milkshake', 'still_water']

# Create a dictionary countaining 4 items (keys) and the relative stock level of each (values)
# Assign this dictionary the name 'stock'
stock = {
        'coffee': 4,
        'tea': 12,
        'milkshake': 20,
        'still_water': 7
        }

# Create a dictionary countaining 4 items (keys) and the relative price of each (values)
# Assign this dictionary the name 'price'
price = {
        'coffee': 22,
        'tea': 16,
        'milkshake': 35,
        'still_water': 8
        }

# Create a for loop the goes through the values in the stock dictionary
# Create a variable (total_stock) to store the sum of the values found in the stock dictionary
for values in stock:
    
    total_stock = sum(stock.values())
# Use the print function to tell the user how much stock is remaining in the Cafe
print(f"\nMy Cafe currently has {total_stock} items in stock")

# Create a for loop that goes through the values of both the price and stock dictionaries respectively
# Create a variable to use as accumulator of the values created in the for loop
total_value = 0
for values in price and stock:
    
    # Multiply the stock value with the price value, and save this in the variable total_worth
    # At every iteration, add the total_worth to the total_value variable...
    # ... the iterations will add together to calculate the total value of all items currently in stock
    total_worth = (stock[values] * price[values])
    total_value = total_value + total_worth
# Use the print function to tell the user how much is the stock is remaining in the Cafe worth in Raands
print(f"\nThere is a total value of R{total_value} in stock in my cafe\n")