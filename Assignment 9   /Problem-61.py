def partition_array(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2

    if n % 2 == 0:
        size = n // 2
    else:
        size = n // 2

    result = []

    def backtrack(start, path, curr_sum):
        if len(path) == size and curr_sum == target:
            result.extend(path)
            return True

        if len(path) > size or curr_sum > target:
            return False

        for i in range(start, n):
            if backtrack(i + 1, path + [arr[i]], curr_sum + arr[i]):
                return True

        return False

    backtrack(0, [], 0)

    subset1 = result
    subset2 = arr[:]

    for x in subset1:
        subset2.remove(x)

    return [subset1, subset2]


print(partition_array([1, 2, 3, 4]))
print(partition_array([5, 10, 15]))
