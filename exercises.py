# 8. Функции

# 8.1
# def message():
#     print('Функции в программировании призваны выполнять определнное действие, повтоярющееся в коде несколько или более раз.')

# message()

# 8.2
# def favoriteBook(title):
#     print(f"One of my favorite books is {title}")

# favoriteBook('Martin Eden')

# 8.3, 8.4
# def makeShirt(text = 'I love Python', size = 'L'):
#     print(f"You ordered {size.upper()} size shirt with text: {text}")

# makeShirt('Stay hard', 'xl')
# makeShirt()

# 8.5
# def describeCity (city, country = 'Russia'):
#     print(f"{city} located in {country}")

# describeCity('Moscow')
# describeCity(city='Kazan')
# describeCity('Rome', 'Italy')

# 8.6
# def city_country(city, country):
#     return f'{city.title()}, {country.title()}'

# print(city_country('canberra', 'australia'))
# print(city_country(country='germany', city='berlin'))
# print(city_country(city='ottawa', country='canada'))

# 8.7, 8.8
# def makeAlbum(name, title, soundtracks=None):
#     album = {'name': name, 'title': title}
#     if soundtracks: album['soundtracks'] = soundtracks
#     return album

# for i in range(0, 3):
#     musicAlbum = makeAlbum(input(), input())
#     print(f"{musicAlbum['name']} has album '{musicAlbum['title']}'")

# album = makeAlbum('Noize MC', 'Новый альбом', '21')
# print(f"{album['name']} has album '{album['title']}' and there are {album['soundtracks']} soundtracks in it")

# 8.9
# def messages(mess):
#     for m in mess: print(m)

# message = ['Hello, Dusty!', 'I hope you fed our cat.', "I'll be late today", 'Good night!']
# messages(message)

# 8.10
# def sendMessages(mess, smess):
#     for i in range(len(mess)): 
#         smess.append(mess.pop())
#     for m in smess: print(m)

# message = ['Hello, Dusty!', 'I hope you fed our cat.', "I'll be late today", 'Good night!']
# sentMessages = []
# sendMessages(message, sentMessages)
# print(f'{message}\n{sentMessages}')

# 8.11 (Данную задачу надо было выполнить, использовав передачу в качестве параметра среза списка, но у меня почему-то не работает)
# def sendMessages(mess, smess):
#     for m in mess:
#         print(m)
#         smess.append(m)

# message = ['Hello, Dusty!', 'I hope you fed our cat.', "I'll be late today", 'Good night!']
# sentMessages = []
# sendMessages(message, sentMessages)
# print(f'{message}\n{sentMessages}')

# 8.12
# def sandwich(*comp):
#     print(f"In this sandwich we have:")
#     for c in comp: print(f"- {c}")

# sandwich('cheese', 'meat', 'pickles', 'sauce')

# 8.13 (Если в **параметр такого типа передавать без ключа (например: не sex='male', а просто 'male'), то создастся кортеж, иначе создастся словарь)
# def buildProfile(firstName, lastName, **info):
#     info['firstName'] = firstName
#     info['lastName'] = lastName
#     return info

# prof = buildProfile('Angel', 'Ramirez', sex='male', country='argentina')

# 8.14
# def car(brand, model, **info):
#     info['brand'] = brand
#     info['model'] = model
#     return info

# def showInfo(car):
#     for key, value in car.items():
#         if(key == 'brand'): print(f"This model of {value} named {car['model']}")
#         elif(key == 'model'): continue
#         else:
#             print(value)     

# honda = car('honda', 'accord', color='grey', transmission='manual transmission')
# showInfo(honda)
# print(honda)

# 8.15
# from modul import car
# from modul import showInfo as info

# toyota = car('toyota', 'supra', color='blue', wheel='right')
# info(toyota)

# 8.16
# import modul
# print(modul.car('toyota', 'supra', color='blue', wheel='right'))

# from modul import car
# print(car('toyota', 'supra', color='blue', wheel='right'))

# from modul import car as c
# print(c('toyota', 'supra', color='blue', wheel='right'))

# import modul as m
# print(m.car('toyota', 'supra', color='blue', wheel='right'))

from modul import *
print(car('toyota', 'supra', color='blue', wheel='right'))






