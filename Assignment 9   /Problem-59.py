def max_visible(arr):
    n = len(arr)

    left = [0] * n
    right = [0] * n

    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if not stack:
            left[i] = i
        else:
            left[i] = i - stack[-1] - 1
        stack.append(i)

    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if not stack:
            right[i] = n - i - 1
        else:
            right[i] = stack[-1] - i - 1
        stack.append(i)

    ans = 0

    for i in range(n):
        ans = max(ans, left[i] + right[i] + 1)

    return ans


print(max_visible([6, 2, 5, 4, 5, 1, 6]))
print(max_visible([1, 3, 6, 4]))
