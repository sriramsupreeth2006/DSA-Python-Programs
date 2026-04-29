n = 3
m = 20
profits = [15, 10, 18]
weights = [3, 5, 7]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(m + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(
                profits[i-1] + dp[i-1][w - weights[i-1]],
                dp[i-1][w]
            )
        else:
            dp[i][w] = dp[i-1][w]
print("Maximum Profit:", dp[n][m])
w = m
selected = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(i)
        w -= weights[i-1]
selected.reverse()
print("Selected Items:", selected)