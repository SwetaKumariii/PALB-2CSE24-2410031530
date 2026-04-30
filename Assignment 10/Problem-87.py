def count_pairs(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            diff = 0
            for k in range(len(arr[i])):
                if arr[i][k] != arr[j][k]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                count += 1

    return count


print(count_pairs(["abc", "abd", "bbd"]))
print(count_pairs(["def", "deg", "dmf", "xef", "dxg"]))
print(count_pairs(["bcde", "bced", "bdce"]))
