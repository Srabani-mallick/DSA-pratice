class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
arr = [1, 2, 3, 4]
x = 3
obj = Solution()
print(obj.search(arr, x))
