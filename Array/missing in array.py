def missingNum(arr):
          n = len(arr) + 1
          return n * (n + 1) // 2 - sum(arr)
arr= [1, 2, 3, 5]
print(missingNum(arr))
        