numPizza = int(input("How many pizzas would you like to order? "))
numBread = int(input("How many garlic breads would you like to order? "))
pricePizza = 10*numPizza
priceBread = 4*numBread
cost = pricePizza + priceBread
tax = .2
totalTax = cost*.2
totalCost = cost + totalTax
print("initial cost: ", cost)
print("tax: ", totalTax)
print("Total Cost: ", totalCost)
