def optimalArray(arr):
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
        ans = []
        for i in range(n):
            m = i // 2
            median = arr[m]
            left = median * (m + 1) - pref[m + 1]
            right = (pref[i + 1] - pref[m + 1]) - median * (i - m)
            ans.append(left + right)
        return ans
arr = [1, 6, 9, 12]
print(optimalArray(arr))