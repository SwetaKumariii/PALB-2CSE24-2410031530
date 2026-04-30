def min_in_submatrix(a, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2:
        return 0
    mn = float('inf')
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if a[i][j] < mn:
                mn = a[i][j]
    return mn

def solve(a, queries):
    n = len(a)
    m = len(a[0])

    for R, C in queries:
        R -= 1
        C -= 1

        cost = 0

        cost += min_in_submatrix(a, 0, 0, R - 1, C - 1)
        cost += min_in_submatrix(a, 0, C + 1, R - 1, m - 1)
        cost += min_in_submatrix(a, R + 1, 0, n - 1, C - 1)
        cost += min_in_submatrix(a, R + 1, C + 1, n - 1, m - 1)

        print(cost)

a1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

queries1 = [(2, 2)]
solve(a1, queries1)

a2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4]
]

queries2 = [(3, 4)]
solve(a2, queries2)
