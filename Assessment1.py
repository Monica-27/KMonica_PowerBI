inventory = [
    # name,        category,    unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,       40,         10],
    ["Broccoli",   "Vegetable",  2.20,       25,         8],
    ["Cheddar",    "Dairy",      5.00,       18,         4],
    ["Baguette",   "Bakery",     2.80,       35,         21],
    ["Blueberry",  "Fruit",      4.00,       22,         6],
    ["Spinach",    "Vegetable",  1.80,       30,         12],
    ["Yogurt",     "Dairy",      1.20,       50,         15],
    ["Croissant",  "Bakery",     3.00,       28,         3]
]

total_revenue=0
print("Low stock items (Less than 5): ")
for i in inventory:
    total_revenue+=(i[2]*i[3])
    if i[4]<5 :
        print(i[0])
print(f'total revenue = {total_revenue}')

category_revenue={}
for i in inventory:
    category=i[1]
    val=i[2]*i[3]
    if category in category_revenue:
        category_revenue[category]+=val
    else:
        category_revenue[category]=val
print(f'Category wise revenue : {category_revenue}')