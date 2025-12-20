# 4 Работа со списками

# 4.1
# pizzas = ['pepperoni', 'hawaii', 'spicy']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza")

# print("\nI love pizza very much!")

# 4.2
# animals = ['elephant', 'hippo', 'buffalo']

# for animal in animals:
#     print(f"{animal} is a big aninal")

# print("\nAny of this animals are big")

# 4.3
# for i in range(1, 21): print(i)

# 4.4
# arr = list(range(1, 1000001))
# for a in arr: print(a)

# 4.5
# arr = list(range(1, 1000001))
# print(min(arr))
# print(max(arr))
# print(sum(arr))

# 4.6
# arr = list(range(1, 20, 2))
# for a in arr: print(a)

# 4.7
# arr = list(range(3, 31, 3))
# for a in arr: print(a)

# 4.8, 4.9
# cubes = [value**3 for value in range(1, 11)]
# for cube in cubes:
#     print(cube)

# 4.10
# dishes = ['burger', 'pizza', 'sushi', 'chocolate', 'marsmallow']
# print(f"First 3 dishes:\n{dishes[:3]}")
# print(f"\nMiddle 3 dishes:\n{dishes[1:4]}")
# print(f"\nLast 3 dishes:\n{dishes[2:]}")

# 4.11, 4.12
# pizzas = ['pepperoni', 'hawaii', 'spicy']
# friendPizzas = pizzas[:]
# pizzas.append('ham')
# friendPizzas.append('cheese')
# print('My favorite pizzas:')
# for pizza in pizzas: print(pizza)
# print("\nMy friend's favorite pizzas:")
# for pizza in friendPizzas: print(pizza)

#4.13
dish = ('soup', 'porridge', 'rice', 'beef', 'salad')
for d in dish: print(d)
dish = ('soup', 'fish', 'rice', 'beef', 'cheese')  
for d in dish: print(d)