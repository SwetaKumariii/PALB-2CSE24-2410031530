from collections import Counter

def sort_by_frequency(s):
    freq = Counter(s)
    chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
    
    result = []
    for ch, count in chars:
        result.append(ch * count)
    
    return ''.join(result)


print(sort_by_frequency("geeksforgeeks"))
print(sort_by_frequency("abc"))
