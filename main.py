print("Hello world")
arr = [10, 2, 10, 10, 10, 3, 4, 10, 4, 5, 19, 0]

index = 0

while(index < len(arr)):
    temp = 1
    while((index+temp) < len(arr)):
        if(arr[index] == arr[index+temp]):
            del arr[index]
            index-=1
            break
        temp+=1
    index+=1

print(arr)
