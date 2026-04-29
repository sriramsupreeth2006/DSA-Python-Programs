def sum_of_subsets(nums, target):
    result = []

    def backtrack(index, current_subset, current_sum):
        # If target sum is found, store the subset
        if current_sum == target:
            result.append(current_subset[:])
            return
        
        # If sum exceeds target or no more elements left, stop
        if current_sum > target or index >= len(nums):
            return

        # Include current element
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset, current_sum + nums[index])

        # Exclude current element (Backtrack)
        current_subset.pop()
        backtrack(index + 1, current_subset, current_sum)

    backtrack(0, [], 0)
    return result


# Driver code
numbers = [10, 7, 5, 18, 12, 20, 15]
target_sum = 35

subsets = sum_of_subsets(numbers, target_sum)

print("Subsets with sum", target_sum, "are:")
for subset in subsets:
    print(subset)