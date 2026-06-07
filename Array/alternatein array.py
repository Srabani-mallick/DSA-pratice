def getAlternates(arr):
    res=[]
    for i in range(0,len(arr),2):
        res.append(arr[i])
    return res

arr= [1, 2, 3, 4]
print(getAlternates(arr))