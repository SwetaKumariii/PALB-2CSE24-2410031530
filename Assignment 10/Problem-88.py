from collections import Counter

def election_winner(arr):
    freq = Counter(arr)

    max_votes = max(freq.values())
    candidates = []

    for name in freq:
        if freq[name] == max_votes:
            candidates.append(name)

    winner = min(candidates)

    return [winner, str(max_votes)]


print(election_winner(["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie",
                       "john", "johnny", "jamie", "johnny", "john"]))

print(election_winner(["andy", "blake", "clark"]))
