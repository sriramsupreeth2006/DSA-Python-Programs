def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def calculate_total_cost(arr):
    total = 0
    for price in arr:
        total += price
    return total

# --- Execution Logic ---
try:
    # Taking input based on Sample-Input
    num_items = int(input("Enter number of items: "))
    # Reading the list of costs
    costs_input = input("Enter costs separated by space: ")
    costs = []
    for x in costs_input.split():
        costs.append(int(x))

    # Sort the elements based on price O(n^2)
    sorted_costs = selection_sort(costs)
    
    # Calculate total sum
    total_sum = calculate_total_cost(sorted_costs)

    # Format the output to match Sample-Output
    sorted_list_str = " ".join(map(str, sorted_costs))
    print(f"sorted list is : {sorted_list_str} , sum is: {total_sum}")

except ValueError:
    print("Please enter valid integers for the costs.")