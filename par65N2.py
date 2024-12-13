import random

def average_binary_search_steps():
    arr = sorted(random.sample(range(101), 32))
    total_steps = 0
    for _ in range(1000):
        target = random.randint(0, 100)
        left, right = 0, len(arr) - 1
        steps = 0
        while left <= right:
            steps += 1
            mid = (left + right) // 2
            if arr[mid] == target:
                break
            elif arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
        total_steps += steps
    return total_steps / 1000

print(average_binary_search_steps())