def optimal_bst(keys, freq):
    n = len(keys)
    pairs = sorted(zip(keys, freq))
    keys = [x[0] for x in pairs]
    freq = [x[1] for x in pairs]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + freq[i]
    def range_sum(i, j):
        return prefix[j+1] - prefix[i]
    cost = [[0]*n for _ in range(n)]
    root = [[0]*n for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            cost[i][j] = float('inf')
            for r in range(i, j+1):
                left = cost[i][r-1] if r > i else 0
                right = cost[r+1][j] if r < j else 0
                total = left + right + range_sum(i, j)
                if total < cost[i][j]:
                    cost[i][j] = total
                    root[i][j] = r
    return cost, root, keys
n = int(input().strip())
keys = list(map(int, input().split()))
freq = list(map(int, input().split()))
cost, root, sorted_keys = optimal_bst(keys, freq)
print(cost[0][n-1])