def buddy_strings(A, B):
    # Lengths must be equal
    if len(A) != len(B):
        return False
    
    # If strings are identical, we need at least one duplicate char to swap
    if A == B:
        return len(set(A)) < len(A)
    
    # Find indices where characters differ
    diff = []
    for i in range(len(A)):
        if A[i] != B[i]:
            diff.append(i)
            
    # Must have exactly 2 differences and swapping them must match B
    return len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]

# Testing Examples
print(buddy_strings("ab", "ba"))       # True
print(buddy_strings("ab", "ab"))       # False
print(buddy_strings("aa", "aa"))       # True
print(buddy_strings("aaaaaaabc", "aaaaaaacb")) # True