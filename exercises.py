# 7. Ввод данных и цикл while

# 7.1
# car = input("What car would you like to drive: ")
# print(f"Searching {car} in your city...")

# 7.2
# seats = int(input("How many seats do you need? "))
# if seats <= 8: print("The table is ready")
# else: print("Sorry, you should to wait for a free tables")

# 7.3
# num = int(input("Enter the number: "))
# if num % 10 == 0:
#     print("Число кратно 10")
# else: 
#     print("Число делится на 10 с остатком")

# 7.4
# topping = ''
# while True:
#     topping = input("Enter topping to add in your order\nEnter 'quit' to end: ")
#     if topping == 'quit': break 
#     print(f"{topping} have been added in your order\n")

# 7.5
# while True:
#     age = int(input("Enter your age to get a price: "))
#     if age < 0: break
#     elif age >= 0 and age < 3: print("Ticket is free")
#     elif age >= 3 and age < 13: print("Ticket is 10$")
#     elif age > 12: print("Ticket is 15$")

# 7.6
# active = True
# while active:
#     message = input("Enter your age to get a price: ")
#     if message == 'quit': 
#         action = False
#         break
#     else:
#         age = int(message)
#         if age >= 0 and age < 3: print("Ticket is free")
#         elif age >= 3 and age < 13: print("Ticket is 10$")
#         elif age > 12: print("Ticket is 15$")

# 7.7 
# while True: print(99)

# 7.8, 7.9
# sandwichOrders = ['cheeseburger', 'pastrami', 'crubsburger','pastrami', 'chickenburger', 'maestro', 'pastrami']
# print("Pastrami isn't availible right now")
# finishedSandwiches = []
# for sandwich in sandwichOrders:
#     print(f"Cooking {sandwich}...\n{sandwich} is done.\n")
#     if sandwich != 'pastrami': finishedSandwiches.append(sandwich)
# print("\nFinished sandwiches:")
# for sandwich in finishedSandwiches:
#     print(sandwich)

# 7.10
members = 5
poll = {}
while members >= 0:
    name = input("What's your name: ")
    poll[name] = input("If you could to visit any place in the world, what place would it be? ")
    members -= 1
print
for name, place in poll.items():
    print(f"{name} would like to visit {place}")


