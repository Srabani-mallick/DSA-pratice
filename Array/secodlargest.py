def getSecondLargest(arr):
        first = second = -1
        for x in arr:
            if x > first:
                second = first
                first = x
            elif x != first and x > second:
                second = x
        return second
ar=[1,5,9,8,7]
print(getSecondLargest(ar))