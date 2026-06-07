def valEqualToPos(arr):
        res=[]
        for i in range(len(arr)):
            if arr[i]==i+1:
                res.append(arr[i])
        return res
arr= [15, 2, 45, 4, 7]
print(valEqualToPos(arr))
        