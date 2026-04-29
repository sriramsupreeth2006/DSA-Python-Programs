import time

# Naïve String Matching Algorithm
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            # Pattern found at index i
            pass

# KMP Algorithm: Preprocessing (LPS Array)
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

# KMP Algorithm: Searching
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            # Pattern found at index i - j
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Main Driver to Compare Execution Time
if __name__ == "__main__":
    # Larger input to make the time difference noticeable
    text = "ABABDABACDABABCABAB" * 5000 
    pattern = "ABABCABAB"

    # Measure Naïve Execution Time
    start_time = time.time()
    naive_search(text, pattern)
    end_time = time.time()
    print(f"Naïve method took {end_time - start_time:.6f} seconds")

    # Measure KMP Execution Time
    start_time = time.time()
    kmp_search(text, pattern)
    end_time = time.time()
    print(f"KMP method took {end_time - start_time:.6f} seconds")