# 3. Списки

# 3.1
# names = ['Artur', 'Daniel', 'Darina', 'Artem']
# print(f'{names[0]}\t{names[1]}\t{names[-2]}\t{names[-1]}')

# 3.2
# names = ['Artur', 'Daniel', 'Darina', 'Artem']
# print(f"Hi, {names[0]}. How it is going?")
# print(f"Hi, {names[1]}. How it is going?")
# print(f"Hi, {names[2]}. How it is going?")
# print(f"Hi, {names[3]}. How it is going?")

# 3.3
# cars = ['Honda', 'Dodge', 'Toyota', 'Porsche', 'Mercedes-Benz']
# print(f"I'd like to buy a car {cars[-2]}")

# 3.4, 3.5, 3.6, 3.7
# icons = ['Martin Eden', 'Maxim Mikhailov', 'Eminem', 'Robert Downey Jr.']
# print(f"Hey, {icons[0]}, I'll glad to see you on my birthday!")
# print(f"Hey, {icons[1]}, I'll glad to see you on my birthday!")
# print(f"Hey, {icons[2]}, I'll glad to see you on my birthday!")
# print(f"Hey, {icons[3]}, I'll glad to see you on my birthday!")
# print(f"Hello, I'm {icons[0]}, I can't visit your birthday because I'm not a real person.")
# icons[0] = 'Charlz Darwin'
# print(icons)
# print('I found a table that is bigger than previous')
# icons.insert(0, "Walter O'Brien")
# icons.insert(2, 'John Tolkien')
# icons.append('Kyle Dickson')
# print(icons)
# print("Sorry, but there is no opportunity to deliver the new table to my birthday, so I can invite only 2 guests.")
# print(f"I'm sorry about this, {icons.pop(0)}")
# print(f"I'm sorry about this, {icons.pop(2)}")
# print(f"I'm sorry about this, {icons.pop(2)}")
# print(f"I'm sorry about this, {icons.pop(2)}")
# print(f"I'm sorry about this, {icons.pop(2)}")
# print(icons)
# print(f"I'm still waiting you, {icons[0]}")
# print(f"I'm still waiting you, {icons[1]}")
# del icons[0]
# del icons[0]
# print(icons)

# 3.8
# countries = ['Sweden', 'England', 'USA', 'Japan', 'France']
# print(countries, sorted(countries), countries, sorted(countries, reverse=True), countries)
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# 3.9
# icons = ['Martin Eden', 'Maxim Mikhailov', 'Eminem', 'Robert Downey Jr.']
# print(f"{len(icons)} guests are invited")

# 3.10 
theFellowshipOfTheRing = ['Frodo', 'Sam', 'Pipin', 'Merry', 'Legolas', 'Gimli', 'Aragorn', 'Boromoir', 'Gandalf']
print(theFellowshipOfTheRing)
print(len(theFellowshipOfTheRing))
print(sorted(theFellowshipOfTheRing))
print(sorted(theFellowshipOfTheRing, reverse=True))
theFellowshipOfTheRing.sort()
theFellowshipOfTheRing.reverse()
print(theFellowshipOfTheRing)
theFellowshipOfTheRing.sort(reverse=True)
print(theFellowshipOfTheRing)

