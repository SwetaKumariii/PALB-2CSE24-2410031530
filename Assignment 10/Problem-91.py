from collections import Counter
import math

def count_vowel_strings(s):
    vowels = set('aeiou')
    freq = Counter(s)

    selected = []
    for ch in vowels:
        if ch in freq:
            selected.append(freq[ch])

    if not selected:
        return 0

    total = 1
    for x in selected:
        total *= x

    total *= math.factorial(len(selected))

    return total


print(count_vowel_strings("aeiou"))
print(count_vowel_strings("ae"))
print(count_vowel_strings("aacidf"))
