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
total = 0

def show_items(items):
    for index, items in enumerate(items):
        print(index, ":", items["name"])
show_items(items)

""" ask = int(input("Select item # to purchase: "))
print(items[ask]) """

while True:
    ask = int(input("Select item # to purchase: (type 'done' to finish): "))
    if ask == "done":
        break
    ask = int(ask)

    cart.append(items[ask])
    total += items[ask]["price"]
    print("In cart: ", items[ask]["name"])

print("Items purchased: ")
for item in cart:
    print(item["name"])
print("Total: $", total)