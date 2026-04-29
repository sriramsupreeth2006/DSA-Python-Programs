def sort_by_frequency_and_alpha(arr):
    # Manually count frequencies using a dictionary
    counts = {}
    for string in arr:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
            
    # Convert dictionary to a list of unique strings
    unique_strings = list(counts.keys())
    
    # Sort the unique strings:
    # 1. Primary key: frequency (counts[x])
    # 2. Secondary key: alphabetical order (x)
    unique_strings.sort(key=lambda x: (counts[x], x))
    
    return unique_strings