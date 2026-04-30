def min_people(arr):
    n = len(arr)
    intervals = []

    for i in range(n):
        if arr[i] != -1:
            left = max(0, i - arr[i])
            right = min(n - 1, i + arr[i])
            intervals.append((left, right))

    intervals.sort()

    count = 0
    i = 0
    current_end = 0
    farthest = 0

    while current_end < n:
        while i < len(intervals) and intervals[i][0] <= current_end:
            farthest = max(farthest, intervals[i][1])
            i += 1

        if farthest == current_end:
            return -1

        count += 1
        current_end = farthest + 1

    return count


print(min_people([1, 2, 1, 0]))
print(min_people([2, 3, 4, -1, 2, 0, 0, -1, 0]))
print(min_people([0, 1, 0, -1]))
