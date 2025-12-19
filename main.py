print("Hello world")
arr = [2, 15, 4, 90, 7, 10, 1, 0]

for i in arr:
    temp = 0
    index = 0
    for j in range(len(arr)-1):
        if(arr[index] > arr[index+1]):
            temp = arr[index]
            arr[index] = arr[index+1]
            arr[index+1] = temp
        index+=1
print(arr)
