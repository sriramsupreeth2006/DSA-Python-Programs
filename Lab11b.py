def subset_sum(arr, target):
    # Start with empty subset
    subsets = [[]]

    # Generate power set
    for num in arr:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])
        subsets.extend(new_subsets)

    # Check each subset sum
    for subset in subsets:
        if sum(subset) == target:
            print("Subset found:", subset)
            return True

    print("No subset found")
    return False


# Example
arr = [1, 2, 3]
target = 5

subset_sum(arr, target)