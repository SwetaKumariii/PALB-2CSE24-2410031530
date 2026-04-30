def combination_sum(n, k):
    result = []

    def backtrack(start, path, total):
        if len(path) == k:
            if total == n:
                result.append(path[:])
            return

        for i in range(start, 10):
            if total + i > n:
                break
            path.append(i)
            backtrack(i + 1, path, total + i)
            path.pop()

    backtrack(1, [], 0)
    return result


print(combination_sum(9, 3))
print(combination_sum(3, 3))
