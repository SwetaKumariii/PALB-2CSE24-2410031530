def count_balanced(arr):
    vowels = set('aeiou')
    vals = []

    for s in arr:
        v = 0
        c = 0
        for ch in s:
            if ch in vowels:
                v += 1
            else:
                c += 1
        vals.append(v - c)

    prefix = 0
    freq = {0: 1}
    count = 0

    for x in vals:
        prefix += x
        if prefix in freq:
            count += freq[prefix]
        freq[prefix] = freq.get(prefix, 0) + 1

    return count


print(count_balanced(["aeio", "aa", "bc", "ot", "cdbd"]))
print(count_balanced(["ab", "be"]))
print(count_balanced(["tz", "gfg", "ae"]))
