def find_pivot(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return low


def count_leq(arr, x, low, high):
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans + 1


def count_elements(arr, x):
    n = len(arr)
    pivot = find_pivot(arr)

    count = 0
    count += count_leq(arr, x, 0, pivot - 1)
    count += count_leq(arr, x, pivot, n - 1)

    return count


print(count_elements([4, 5, 8, 1, 3], 6))
print(count_elements([6, 10, 12, 15, 2, 4, 5], 14))
