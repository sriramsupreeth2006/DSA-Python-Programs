# 0/1 Knapsack using Backtracking

p = [15,10,18]
w = [3,5,7]
n = 3
m = 20

maxProfit = 0

def knapsack(i, weight, profit):
    global maxProfit

    if weight <= m and profit > maxProfit:
        maxProfit = profit

    if i == n:
        return

    # Include item
    if weight + w[i] <= m:
        knapsack(i+1, weight+w[i], profit+p[i])

    # Exclude item
    knapsack(i+1, weight, profit)

knapsack(0,0,0)

print("Optimal Profit =", maxProfit)