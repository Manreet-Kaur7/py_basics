menu = {
    "Pizza(M)" : 189,
    "Burger" :60,
    "Pasta" :80,
    "Veg-wrap" : 79,
    "Fries" : 99,
    "Coffee" : 80,
    "Soft-drink" : 30 
}
total_bill = 0

print("--Welcome to Friends restaurant--")
for key,value in menu.items():
    print(key,"$",value)
order1 = input("Enter your order:")
if order1 in menu:
    total_bill += menu[order1]
    print(f"Your order {order1} has been added to your order.")
else:
    print(f"ordered food {order1} is not in our menu.\n Sorry !!")

another_order = input("Do you want another item?")
if another_order=="Yes":
    order2 = input("Enter your second order:")
    if order2 in menu:
        total_bill += menu[order2]
        print(f" Your order {order2} has been addedto your oder.")
    else:
        print(f"Ordered item {order2} is not in our menu.")   

print(f"The total bill amount is: {total_bill}") 
