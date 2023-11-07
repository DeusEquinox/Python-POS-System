foodList = []
priceList = []

with open("Stock.txt", 'r') as file:
    for line in file:
        (food, price) = line.strip().split(",")
        foodList.append(food)
        priceList.append(price)
