def largest_string(s, k):
    stack = []

    for ch in s:
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)

    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)


print(largest_string("ritz", 2))
print(largest_string("zebra", 3))
