# 10. Файлы и исключения
from pathlib import Path
import json

# 10.1, 10.2, 10.3
# py = Path('files/piDigits.txt')
# cont = py.read_text()
# print(cont)

# message = ''
# for line in cont.splitlines():
#     line = line[1:]
#     line = line.replace('.', '')
#     line = line.replace('Python', 'Assembler')
#     line = line.strip()
#     message += f'{line}, '
# print(message)

# 10.4
# path = Path("files/piDigits.txt")

# guest = input("Hello! What is your name? ")
# path.write_text(guest)

# 10.5
# guests = Path('files/piDigits.txt')
# guestList = ''
# for i in range(1, 6):
#     name = input("Please, enter your name: ")
#     guestList += f"{i}. {name.title()}\n"
#     print(f"Nice to see you, {name.title()}")
# guests.write_text(guestList.rstrip())
# print(guests.read_text())

# 10.6, 10.7
# while True:
#     n1 = input("First number: ")
#     if n1 == 'q': break
#     n2 = input("Second number: ")
#     if n2 == 'q': break
#     try:
#         print(f"The sum is {int(n1)+int(n2)}")
#     except ValueError:
#         print('Please, enter the number.')

# 10.8
# cats = Path('files/cats.txt')
# dogs = Path('files/dogs.txt')

# try:
#     catContent = cats.read_text()
# except FileNotFoundError:
#     print(f"File {cats} doesn't exist!")
# else:
#     for line in catContent.splitlines():
#         print(f"Cat's name is {line}")

# try:
#     dogContent = dogs.read_text()
# except FileNotFoundError:
#     print(f"File {dogs} doesn't exist!")
# else:
#     for line in dogContent.splitlines():
#         print(f"Dog's name is {line}")

# 10.10
# def countWord(path, word):
#     try:
#         content = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         return f"File {path} doesn't exist"
#     else:
#         return content.lower().count(f'{word} ')
    
# def showWord(name, path, word):
#     if isinstance(countWord(path, word), int):
#         print(f"In book '{name}' the word '{word}' meets {countWord(path, word)} times")
#     else:
#         print(countWord(path, word))


# books = {'Martin Eden': Path('files/martinEden.txt'), 'Jane Eyre': Path('files/janeEyre.txt'), 'Dead Souls': Path('files/deadSouls.txt')}

# for key, value in books.items():
#     showWord(key, value, 'me')

# 10.11, 10.12
# path = Path('files/favNum.json')
# if path.exists():
#     content = json.loads(path.read_text())
#     print(f"I know your favorite number! It's {content}")
# else:
#     path.write_text(json.dumps(input("What's your favorite number? ")))

# 10.13
def addPerson(path):
    path = Path('files/personInfo.json')
    me = {}
    me['name'] = input("What's your name? ")
    try: 
        me['age'] = int(input("How old are you? "))
    except ValueError:
        print("Please, enter the number")
        me['age'] = int(input("How old are you? "))
    me['sex'] = input("Are you a male or female? ")
    path.write_text(json.dumps(me))

person = Path('files/personInfo.json')
if person.exists():
    print("Info about you:")
    print(json.loads(person.read_text()))
    correct = input("Is this information correct? y/n: ")
    if correct == 'y':
        print('Welcome!')
    elif correct == 'n':
        addPerson(person)
else:
    addPerson(person)
