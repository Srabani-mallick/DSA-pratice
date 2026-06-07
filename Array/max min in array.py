def getMinMax(arr):
        min=arr[0]
        max=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min:
                min=arr[i]
            if arr[i]>max:
                max=arr[i]
        return min ,max

ar=[1, 4, 3, 5, 8, 6]
print(getMinMax(ar))