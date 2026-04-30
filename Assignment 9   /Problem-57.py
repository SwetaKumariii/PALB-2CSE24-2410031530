def count_subarrays(arr):
    n = len(arr)
    stack = []
    next_smaller = [n] * n

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            next_smaller[idx] = i
        stack.append(i)

    result = 0

    for i in range(n):
        result += next_smaller[i] - i

    return result


print(count_subarrays([1, 2, 1]))
print(count_subarrays([1, 3, 5, 2]))
