menu = {
    'Espresso' : 100,
    'Cappuccino' : 150,
    'Americano' : 120 ,
    'Mocha' : 200 ,
    'Iced Coffee' : 160, 
    'Green Tea' : 80 ,
    'Herbal Tea' : 100 ,
    'Chicken Sandwich' : 250 ,
    'Beef Burger' : 300 ,
    'Veggie Wrap' : 200 ,
    'Caesar Salad' : 220 ,
    'Grilled Cheese Sandwich' : 180 ,
    'Pasta Alfredo' : 350 ,
    'Chicken Wings 6 pieces' : 280 ,
    'Chocolate Cake Slice' : 150
}
#print(menu)
print("Welcome to my mini food store")
print("Espresso : 100 BDT\nCappuccino : 15 BDT\nAmericano : 120 BDT\nMocha : 200 BDT\nIced Coffee : 160 BDT\nGreen Tea : 80 BDT\nHerbal Tea : 100 BDT\nChicken Sandwich : 250 BDT\nBeef Burger : 300 BDT\nVeggie Wrap : 200 BDT\nCaesar Salad : 220 BDT\nGrilled Cheese Sandwich : 180 BDT\nPasta Alfredo : 350 BDT\nChicken Wings 6 pieces : 280 BDT\nChocolate Cake Slice : 150")

orderTotal = 0 # 80 + 70
item_1 = input("Enter the name of item you want: ")
if item_1 in menu:
    orderTotal += menu[item_1] # 0 + 50
    print(f"Your {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available")