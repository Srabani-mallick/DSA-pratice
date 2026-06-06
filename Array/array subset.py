from collections import Counter
def isSubset(a, b):
        count_a = Counter(a)

        for num in b:
            if count_a[num] == 0:
                return False
            count_a[num] -= 1

        return True
ar = [1, 2, 3, 4, 5]
ar1 = [3, 4, 5]

print(isSubset(ar,ar1))