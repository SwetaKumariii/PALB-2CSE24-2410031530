def min_time_diff(arr):
    times = []

    for t in arr:
        h, m, s = map(int, t.split(':'))
        total = h * 3600 + m * 60 + s
        times.append(total)

    times.sort()

    ans = float('inf')

    for i in range(1, len(times)):
        ans = min(ans, times[i] - times[i-1])

    ans = min(ans, 24*3600 - times[-1] + times[0])

    return ans


print(min_time_diff(["12:30:15", "12:30:45"]))
print(min_time_diff(["00:00:01", "23:59:59", "00:00:05"]))
