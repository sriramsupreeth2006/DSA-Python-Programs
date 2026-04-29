def solve():
    # Read input
    try:
        m = int(input())
        car_costs = list(map(int, input().split()))
        bus_costs = list(map(int, input().split()))
    except EOFError:
        return
    car_costs.sort()
    bus_costs.sort()
    cost_start_car = 0
    cost_start_bus = 0

    for i in range(m):
        # i is 0-indexed, so even days (0, 2, 4) are Day 1, 3, 5...
        if i % 2 == 0:
            # Day 1, 3, 5...
            cost_start_car += car_costs[i]
            cost_start_bus += bus_costs[i]
        else:
            # Day 2, 4, 6...
            cost_start_car += bus_costs[i]
            cost_start_bus += car_costs[i]
    print(min(cost_start_car, cost_start_bus))

if __name__ == "__main__":
    solve()