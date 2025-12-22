# 5. Оператор if

# 5.1
# sport = 'volleyball'
# print("Is her favorite sport volleyball? I predict False")
# print(sport == 'volleyball')
# print("But I don't think her favorite sport is soccer. I predict False again")
# print(sport == 'soccer')

# 5.2
# word = 'sword'
# print(word=='sword')
# print(word.upper=='Sword')
# age = 18
# print(age > 18)
# players = ['jack', 'john', 'dustin']
# if 'jack' in players: print("John, you'll play")
# if 'mike' not in players: print("Mike, today you'll stay at home")
# primaryNumbers = [7, 19]
# if (primaryNumbers[0]/primaryNumbers[0]==1) and (primaryNumbers[1]/primaryNumbers[1]==1): print('Both numbers are primary')
# primaryNumbers[0] = 16
# if (primaryNumbers[0]/primaryNumbers[0]==1) or (primaryNumbers[1]/primaryNumbers[1]==1): print('At least one of this numbers is primary')

# 5.3
# alienColor = ['green', 'yellow', 'red']
# if 'green' in alienColor: print('You got 5 points')
# if 'blue' in alienColor: print('You got 5 points')

# 5.4
# alienColor = ['green', 'yellow', 'red']
# if 'green' in alienColor: print('You got 5 points')
# else: print('You got 10 points')
# if 'blue' in alienColor: print('You got 5 points')
# else: print('You got 10 points')

# 5.5
# alienColor = ['green', 'yellow', 'red']
# color = 'blue'
# if color == 'green': print('You got 5 points')
# elif color == 'yellow': print('You got 10 points')
# elif color == 'red': print('You got 15 points')
# else: print('You missed')

# 5.6
# age = 21
# if age >= 2 and age < 4: print('baby')
# elif age >= 4 and age < 13: print('kid')
# elif age >= 13 and age < 20: print('teenager')
# elif age >= 20 and age < 65: print('adult')
# elif age >= 65: print('elderly') 

# 5.7
# favoriteFruits = ['banana', 'apple', 'grape', 'orange']
# if 'banana' in favoriteFruits: print('You love bananas very much!')
# if 'passion fruit' in favoriteFruits: print('You love passion fruits very much!')
# if 'peach' in favoriteFruits: print('You love peaches very much!')
# if 'grape' in favoriteFruits: print('You love grape very much!')

# 5.8
# users = ['max', 'admin', 'henry', 'alice', 'cobe']
# for user in users:
#     if user == 'admin': print(f"Hello, {user}, want to get the work status?")
#     else: print(f"Hello, {user}, thanks for logining in our system")

# 5.9
# users = ['jessica']
# if users:
#     for user in users: print(f"Hello, {user}")
# else: print("We need to add some users")

# 5.10
# currentUsers = ['mike', 'lukas', 'will', 'dustin', 'eleven']
# newUsers = ['Max', 'Steve', 'Dustin', 'Mike', 'Nancy']
# for user in newUsers:
#     if user.lower() in currentUsers:
#         print("You should choose other name")
#     else: 
#         print("Welcome!")

# 5.11
# for num in range(1, 10):
#     if num == 1:
#         print(f"{num}st")
#     elif num == 2:
#         print(f"{num}nd")
#     elif num == 3:
#         print(f"{num}rd")
#     else: print(f"{num}th")
