# Function to minimize vehicles used
def assign_packages(packages, capacity):
    packages.sort(reverse=True)   # Larger packages first
    vehicles = []

    def backtrack(index):
        if index == len(packages):
            return len(vehicles)

        min_vehicles = float('inf')

        # Try placing package in existing vehicles
        for i in range(len(vehicles)):
            if vehicles[i] + packages[index] <= capacity:
                vehicles[i] += packages[index]

                min_vehicles = min(min_vehicles, backtrack(index+1))

                # Backtrack
                vehicles[i] -= packages[index]

        # Try new vehicle
        vehicles.append(packages[index])

        min_vehicles = min(min_vehicles, backtrack(index+1))

        vehicles.pop()  # Backtrack

        return min_vehicles

    return backtrack(0)


# Example
packages = [4, 8, 1, 4, 2, 1]
vehicle_capacity = 10

print("Minimum vehicles needed:",
      assign_packages(packages, vehicle_capacity))