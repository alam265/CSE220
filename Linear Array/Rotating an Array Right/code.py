def RoateRight(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

print(RoateRight([1,2,3,4,5]))