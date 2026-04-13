items = [ 
{   
    "name": "Vivitar VECXX101 4K Digital Camera",
    "price": 99.99,
    "department": "camera",
    "description": "Take picture."  
},
{
    "name":"HP 14' Intel Processor N150 2025 Laptop",
    "price": 179.99,
    "department": "laptop",
    "description": "Type."
},
{
    "name": "Apple iPad Air 11-inch",
    "price": 549.00,
    "department": "iPad",
    "description": "Press."
},
{    "name": "AirPods 4 Apple",
    "price": 129.00,
    "department": "AirPods",
    "description": "Listen."
}
]


cart = []
prices = []
cost = 0
shop = 0
def show_items(items):
    for index, items in enumerate(items):
        print(index, ":", items["name"])
show_items(items)

""" ask = int(input("Select item # to purchase: "))
print(items[ask]) """

while shop == 0:
    ask = int(input(" Select item # to purchase: "))
    cart.append(items[ask]["name"])
    print(items[ask])

    shop = (input("Would you like to continue shopping?: "))
    while shop != "done":
        ask = int(input("Select item # to purchase: (type 'done' to finish): "))
        cart.append(items[ask]["name"])
        cart.append(items[ask][""])
    print(items[ask])