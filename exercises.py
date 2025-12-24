# 9. Классы

# 9.1, 9.2
# class Restaurant:
#     def __init__(self, restaurantName, cuisineType):
#         self.name = restaurantName
#         self.cuisine = cuisineType
#     def describeRestaurant(self):
#         print(f"There are dishes of {self.cuisine} cuisine in {self.name} restaurant")
#     def openRestaurant(self):
#         print(f"{self.name} is open now!")
    
# chivalry = Restaurant('Chivalry', 'England')
# print(f"I'm working in {chivalry.name} restaurant. There are dishes of {chivalry.cuisine} cuisine.")
# chivalry.describeRestaurant()
# chivalry.openRestaurant()

# verity = Restaurant('Verity', 'Wales')
# print()
# verity.describeRestaurant()

# regal = Restaurant('Regal', 'German')
# print()
# regal.describeRestaurant()

# 9.3
# class User:
#     def __init__(self, firstName, lastName, age, sex):
#         self.fName = firstName
#         self.lName = lastName
#         self.age = age
#         self.sex = sex
#     def describeUser(self):
#         if (self.sex).lower() == 'female':
#             print(f"{(self.fName).title()} {(self.lName).title()} is a {self.age} years old woman")
#         elif (self.sex).lower() == 'male':
#             print(f"{(self.fName).title()} {(self.lName).title()} is a {self.age} years old man")
#         else:
#             print(f"{(self.fName).title()} {(self.lName).title()} is {self.age} years old")
#     def greetUser(self):
#         print(f"Nice to meet you, {(self.fName).title()}!")

# kate = User('kate', 'dusfill', 23, 'female')
# kate.describeUser()
# kate.greetUser()
# print()

# fil = User('filipp', 'fuko', 56, 'Male')
# fil.describeUser()
# fil.greetUser()
# print()

# fitz = User('fitz', 'chivalry', 16, '')
# fitz.describeUser()
# fitz.greetUser()
        
# 9.4
# class Restaurant:
#     def __init__(self, restaurantName, cuisineType):
#         self.name = restaurantName
#         self.cuisine = cuisineType
#         self.served = 0
#     def describeRestaurant(self):
#         print(f"There are dishes of {self.cuisine} cuisine in {self.name} restaurant")
#     def openRestaurant(self):
#         print(f"{self.name} is open now!")
#     def setServed(self, num):
#         self.served = num
#     def incrementServed(self, inc):
#         self.served += inc
    
# chivalry = Restaurant('Chivalry', 'England')
# print(f"I'm working in {chivalry.name} restaurant. There are dishes of {chivalry.cuisine} cuisine.")
# chivalry.describeRestaurant()
# chivalry.openRestaurant()
# print(chivalry.served)
# chivalry.served = 2
# print(chivalry.served)
# chivalry.setServed(16)
# print(chivalry.served)
# chivalry.incrementServed(130)
# print(chivalry.served)

# 9.5
# class User:
#     def __init__(self, firstName, lastName, age, sex):
#         self.fName = firstName
#         self.lName = lastName
#         self.age = age
#         self.sex = sex
#         self.loginAttempts = 0
#     def describeUser(self):
#         if (self.sex).lower() == 'female':
#             print(f"{(self.fName).title()} {(self.lName).title()} is a {self.age} years old woman")
#         elif (self.sex).lower() == 'male':
#             print(f"{(self.fName).title()} {(self.lName).title()} is a {self.age} years old man")
#         else:
#             print(f"{(self.fName).title()} {(self.lName).title()} is {self.age} years old")
#     def greetUser(self):
#         print(f"Nice to meet you, {(self.fName).title()}!")
#     def incAttempt(self):
#         self.loginAttempts += 1
#     def resetAttempts(self):
#         self.loginAttempts = 0 

# kate = User('kate', 'dusfill', 23, 'female')
# print("The password id 'Katie123'")
# kate.greetUser()
# while True:
#     password = input("Please, enter the password: ")
#     if password == 'Katie123': 
#         print("Welcome!")
#         kate.resetAttempts()
#         break
#     else:
#         print("Password isn't correct, try again")
#         kate.incAttempt()
#         print(f"Failed login attempts: {kate.loginAttempts}")

# 9.6
# class Restaurant:
#     def __init__(self, restaurantName, cuisineType):
#         self.name = restaurantName
#         self.cuisine = cuisineType
#         self.served = 0
#     def describeRestaurant(self):
#         print(f"There are dishes of {self.cuisine} cuisine in {self.name} restaurant")
#     def openRestaurant(self):
#         print(f"{self.name} is open now!")
#     def setServed(self, num):
#         self.served = num
#     def incrementServed(self, inc):
#         self.served += inc
    
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurantName, cuisineType, flavors):
#         super().__init__(restaurantName, cuisineType)
#         self.flavors = flavors
    
#     def showFlavors(self):
#         print(f"In {self.name} we have this ice cream flavors:")
#         for flavor in self.flavors:
#             print(f"- {flavor}")
    

# lincoln = IceCreamStand('Lincoln', 'Ice cream', ['fistachio', 'chocolate', 'raspberry'])
# lincoln.describeRestaurant()
# print()
# lincoln.showFlavors()
# lincoln.openRestaurant()

# 9.7, 9.8
# class User:
#     def __init__(self, firstName, lastName, age, sex):
#         self.fName = firstName
#         self.lName = lastName
#         self.age = age
#         self.sex = sex
#     def describeUser(self):
#         if (self.sex).lower() == 'female':
#             print(f"{(self.fName).title()} {(self.lName).title()} is a {self.age} years old woman")
#         elif (self.sex).lower() == 'male':
#             print(f"{(self.fName).title()} {(self.lName).title()} is a {self.age} years old man")
#         else:
#             print(f"{(self.fName).title()} {(self.lName).title()} is {self.age} years old")
#     def greetUser(self):
#         print(f"Nice to meet you, {(self.fName).title()}!")

# class Admin(User):
#     def __init__(self, firstName, lastName, age, sex):
#         super().__init__(firstName, lastName, age, sex)
#         self.priv = Privileges()

# class Privileges:
#     def __init__(self, privileges=''):
#         self.priv = privileges
#     def showPriveleges(self):
#         print(f"Admin has this privileges:")
#         for p in self.priv:
#             print(f" - {p}")


# ray = Admin('Ray', 'Ollback', 30, 'male')
# ray.priv.priv = ['Use data', 'Ban users', 'Add rules']
# ray.greetUser()
# ray.describeUser()
# ray.priv.showPriveleges()

# 9.9
# class Car:
#     """Simple car type"""
#     def __init__(self, firm, model, year):
#         self.firm = firm
#         self.model = model
#         self.year = year
#         self.run = 0
    
#     def getInfo(self):
#         info = f"{self.year} {(self.firm).title()} {(self.model).title()}"
#         return info
            
#     def getRun(self):
#         return self.run
    
# class ElectricCar(Car):
#     """Electric car type"""
#     def __init__(self, firm, model, year):
#         super().__init__(firm, model, year)
#         self.battery = Battery()

# class Battery:
#     def __init__(self, battery = 40):
#         self.battery = battery
#     def describeBattery(self, car):
#         print(f"{car} has a {self.battery}-kWh battery")
#     def batteryRange(self):
#         powerReserve = 300
#         if self.battery <= 40 and self.battery > 10:
#             powerReserve = 300
#         elif self.battery > 40 and self.battery < 60:
#             powerReserve = 500
#         elif self.battery > 60:
#             powerReserve = 800
#         print(f"Its' power reserve is {powerReserve} kWh")
#     def upgradeBattery(self):
#         if self.battery < 80:
#             self.battery = 80
#             print(f"Battery upgraded. Now it's {self.battery} kWh")
    
# zeekr = ElectricCar('Zeekr', '001', '2025')
# print(zeekr.getInfo())
# zeekr.battery.describeBattery(zeekr.getInfo())
# zeekr.battery.batteryRange()
# print()
# zeekr.battery.upgradeBattery()
# zeekr.battery.batteryRange()

# 9.10
# from modulClass import Restaurant as R
     
# chivalry = R('Chivalry', 'England')
# print(f"I'm working in {chivalry.name} restaurant. There are dishes of {chivalry.cuisine} cuisine.")
# chivalry.describeRestaurant()
# chivalry.openRestaurant()

# 9.11 
# from modulClass import Admin, User, Privileges

# ray = Admin('Ray', 'Ollback', 30, 'male')
# ray.priv.priv = ['Use data', 'Ban users', 'Add rules']
# ray.greetUser()
# ray.describeUser()
# ray.priv.showPriveleges()

# 9.13
# from random import randint 

# class Die:
#     def __init__(self, sides = 6):
#         self.sides = sides
#     def rollDie(self):
#         rand = randint(1, self.sides)
#         print(f"Rolling... There is {rand}")

# cube1 = Die()
# cube2 = Die(10)
# cube3 = Die(20)

# cubes = [cube1, cube2, cube3]

# for cube in cubes:
#     for i in range(10):
#         cube.rollDie()
#     print()

# 9.14, 9.15
from random import choice

lotery = [5, 't', 6, 9, 'o', 1, 2, 7, 'v', 4, 3, 'w', 'x', 8]
win = ''
for i in range(4): win += str(choice(lotery))
print(f"Ticket '{win}' is winning!")

myTicket = ''
for i in range(4): myTicket += str(choice(lotery))
loteryAnalysis = 0

while True:
    win = ''
    for i in range(4): win += str(choice(lotery))
    if win == myTicket: break
    loteryAnalysis += 1

print(f"Your ticket was {myTicket}. It took {loteryAnalysis} generations to your ticket was winning")

