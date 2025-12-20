# Пример 1:
s = "abcde"
words = ['a', 'bb', 'acd', 'ace']

# Пример 2:
# s = "dsahjpjauf"
# words = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax']

index = 0
count = 0

while(index < len(words)):
    sCopy = s
    temp = 0
    for r in words[index]:
        if r in sCopy:
            temp+=1
            f = sCopy.find(r)
            sCopy = sCopy[:f]+sCopy[f+1:]
        else:
            break
    if(len(words[index]) == temp): count+=1
    index+=1

print(count)