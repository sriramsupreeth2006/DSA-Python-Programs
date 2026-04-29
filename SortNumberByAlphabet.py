def number_to_words(n):
    """
    Converts non-negative integers into their English word representation.
    Supports numbers up to 999 for this specific task.
    """
    if n == 0: return "zero"
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    words = ""
    
    if n >= 100:
        words += units[n // 100] + " hundred "
        n %= 100
        if n > 0:
            words += "and "
            
    if 10 <= n < 20:
        words += teens[n - 10]
    else:
        if n >= 20:
            words += tens[n // 10]
            if n % 10 > 0:
                words += "-" + units[n % 10]
        elif n > 0:
            words += units[n]
            
    return words.strip().capitalize()

def sort_numbers_alphabetically(arr):
    # We use our helper function as the sorting key
    # This sorts the original numbers based on the alphabetical order of their words
    arr.sort(key=number_to_words)
    return arr

# Input from your image
input_arr = [12, 10, 102, 31, 15]
result = sort_numbers_alphabetically(input_arr)

# Printing the result to match your sample output
print("Output:", " ".join(map(str, result)))