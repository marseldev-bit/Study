print("Hello world")
word = input("Введите слово: ")
wordLower = word.lower() 
firstIndex = 0
lastIndex = len(word) - 1
tf = False
for c in wordLower:
    if(wordLower[firstIndex] == wordLower[lastIndex]):
        tf = True
    else:
        tf = False
        break
    firstIndex += 1
    lastIndex -= 1

if(tf): print(f"Word {word} is palindrome")
else: print(f"Word {word} is not palindrome")