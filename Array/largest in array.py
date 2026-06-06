def largest(arr):
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum

ar = [1, 2, 90, 3, 7, 100]

print(largest(ar))