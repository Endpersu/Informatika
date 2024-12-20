def sort_and_find(arr, target):
    arr.sort(reverse=True)
    return [x for x in arr if x == target]

arr = [34, 23, 12, 45, 56, 78, 34, 23]
target = 34
print(sort_and_find(arr, target))