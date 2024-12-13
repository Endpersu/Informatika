def sort_half(arr):
    mid = len(arr) // 2
    first_half = sorted(arr[:mid])
    second_half = sorted(arr[mid:], reverse=True)
    return first_half + second_half

arr = [34, 23, 12, 45, 56, 78]
print(sort_half(arr))