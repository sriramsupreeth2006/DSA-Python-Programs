def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def sort_and_display_counts(arr):
    # Sort the array based on the vowel count helper function
    arr.sort(key=count_vowels)
    
    # Print the specific counts for clarity, matching your task requirements
    for word in arr:
        v_count = count_vowels(word)
        print(f'"{word}" has {v_count} vowel(s)')
    
    return arr

# Input from your task
input_arr = ["pointer", "array", "code", "for"]
sorted_result = sort_and_display_counts(input_arr)