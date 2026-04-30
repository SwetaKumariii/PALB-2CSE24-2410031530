def previous_greater(arr):
    stack = []
    result = []

    for x in arr:
        while stack and stack[-1] <= x:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(x)

    return result


print(previous_greater([10, 4, 2, 20, 40, 12, 30]))
print(previous_greater([10, 20, 30, 40]))
