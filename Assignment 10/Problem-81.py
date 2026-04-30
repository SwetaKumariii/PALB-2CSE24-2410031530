def min_swaps(s1, s2):
    total_ones = s1.count('1') + s2.count('1')

    if total_ones % 2 != 0:
        return -1

    target = total_ones // 2
    ones_s1 = s1.count('1')

    return abs(ones_s1 - target)


print(min_swaps("1100", "1111"))
print(min_swaps("00011", "11001"))
