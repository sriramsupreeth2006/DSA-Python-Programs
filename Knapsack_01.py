def knapsack_01():
    n = int(input("Enter number of items: "))
    values, weights = [], []
    print("Enter value and weight of items:")
    for _ in range(n):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)
    W = int(input("Enter size of knapsack: "))

    # DP Table initialization
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    print(f"Maximum Value: {dp[n][W]}")

# knapsack_01()