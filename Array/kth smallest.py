def kthSmallest(arr, k):
        def partition(l, r):
            pivot = arr[r]
            i = l
            for j in range(l, r):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[r] = arr[r], arr[i]
            return i
        l, r = 0, len(arr) - 1
        while l <= r:
            p = partition(l, r)
            if p == k - 1:
                return arr[p]
            elif p > k - 1:
                r = p - 1
            else:
                l = p + 1
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest(arr, k))