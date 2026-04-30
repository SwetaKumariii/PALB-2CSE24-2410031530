from collections import Counter

def count_even_letters(s):
    freq = Counter(s)
    count = 0

    for ch in freq:
        if freq[ch] % 2 == 0:
            count += 1

    return count


print(count_even_letters("abacaba"))
print(count_even_letters("zzacccz"))
