def min_length_after_deletion():
    n = int(input().strip())
    s = input().strip()
    
    # Frequency array for 26 letters
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1
    
    # Find the character that appears most frequently
    max_freq = 0
    for f in freq:
        if f > max_freq:
            max_freq = f
            
    # Result is total length minus the occurrences of the most frequent char
    print(n - max_freq)