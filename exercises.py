# 6. Словари

# 6.1
# person = {'firstName': 'Simeon', 'lastName': 'Nikolov', 'age': 19, 'city': 'Novosibirsk'}
# for key in person:
#     print(person[key])

# 6.2 
# number = {
#     'marsel': 4,
#     'mike': 11,
#     'dustin': 666,
#     'lucas': 12,
#     'will': 3
# }
# for key in number:
#     print(f"{key} favorite number is {number[key]}")

# 6.3, 6.4
# prog = {
#     'Цикл': 'Повторяющийся при истинном условии блок кода до момента утрачивания условия истинности',
#     'Условный оператор': 'Выполняет блок кода при истинном условии',
#     'Кортеж': 'Контейнер, хранящий любое количество значений, которые нельзя изменить',
#     'Переменная': 'Ссылка на значение любого типа данных',
#     'Срез': 'Часть словаря'
# }
# for key in prog:
#     print(f"{key} - {prog[key]}\n")

# 6.5
# rivers = {'nile': 'egypt', 'amazonka': 'brazil', 'Volga': 'Russia'}
# for key, value in rivers.items():
#     print(f"{key.title()} goes across the {value.title()}")
# print()
# for key in rivers:
#     print(key.title())
# print()
# for value in rivers.values(): 
#     print(value.title())

# 6.6
# passed = ['robin', 'steve', 'nancy']
# names = {}

# for p in passed:
#     names[p] = 'passed' 

# names['jonathan'] = 'no'
# names['Eddie'] = 'no'

# for k, v in names.items():
#     if(v == 'passed'): print(f"Thanks for taking part, {k.title()}")
#     else: print(f"Please, take part, {k.title()}")

# 6.7 
# player1 = {'firstName': 'Simeon', 'lastName': 'Nikolov', 'age': 19, 'city': 'Novosibirsk'}
# player2 = {'firstName': 'Maxim', 'lastName': 'Mikhailov', 'age': 33, 'city': 'Kazan'}
# player3 = {'firstName': 'Earvin', 'lastName': 'Ngapeth', 'age': 34, 'city': 'Paris'}

# players = [player1, player2, player3]
# for player in players:
#     print(f"My name is {player['firstName']} {player['lastName']}, I'm {player['age']} years old and I'm living in {player['city']}")

# 6.8
# pet1 = {'animal': 'cat', 'owner': 'Mike', 'name': 'Jessy'}
# pet2 = {'animal': 'dog', 'owner': 'Kyle', 'name': 'Sparky'}
# pet3 = {'animal': 'fox', 'owner': 'Rebecca', 'name': 'Fenec'}

# pets = [pet1, pet2, pet3]
# for pet in pets:
#     print(f"This is the {pet['animal']} {pet['name'].title()}, {pet['owner']} is its owner")


# 6.9
# player1 = {'firstName': 'Simeon', 'lastName': 'Nikolov', 'age': 19, 'city': 'Novosibirsk'}
# player2 = {'firstName': 'Maxim', 'lastName': 'Mikhailov', 'age': 33, 'city': 'Kazan'}
# player3 = {'firstName': 'Earvin', 'lastName': 'Ngapeth', 'age': 34, 'city': 'Paris'}

# favoritePlaces = ['egypt', 'maldives', 'spain', 'fiji']
# player1['place'] = [favoritePlaces[0]]
# player2['place'] = [favoritePlaces[1], favoritePlaces[2]]
# player3['place'] = [favoritePlaces[3]]

# players = [player1, player2, player3]
# for player in players:
#     print(f"{player['firstName']} favorite places are: ")
#     for place in player['place']:
#         print(f"\t{place}")

# 6.10
# number = {
#     'marsel': [4, 19],
#     'mike': [11, 21, 31],
#     'dustin': [666],
#     'lucas': [12, 10],
#     'will': [1, 2, 3]
# }

# for k, v in number.items():
#     print(f"{k} favorite numbers are: ")
#     for i in v:
#         print(f"\t{i}")
#     print()

# 6.11
# cities = {
#     'Moscow': {
#         'country': 'russia',
#         'population': '13000000',
#         'fact': 'There are more than 100 parks and gardens in Moscow'
#     },
#     'Rome': {
#         'country': 'Italy',
#         'population': '2700000',
#         'fact': 'There are more than 2000 fontains in Rome'
#     },
#     'Madrid': {
#         'country': 'Spain',
#         'population': '3500000',
#         'fact': 'Madrid located on a height if 650m over the sea'
#     }
# }

# for k, v in cities.items():
#     print(f"{k} is a city in the {v['country']}. Population there is {v['population']} people. {v['fact']}")

# 6.12
number = {
    'marsel': [4, 19],
    'mike': [11, 21, 31],
    'dustin': [666],
    'lucas': [12, 10],
    'will': [1, 2, 3]
}

for k, v in number.items():
    print(f"{k} has {len(v)} favorite naumbers. The sum of this numbers is {sum(v)}")