def find_password_easy(n, passwords):
    for i in range(n):
        current = passwords[i]
        reversed_p = current[::-1]
        
        for j in range(n):
            if passwords[j] == reversed_p:
                length = len(current)
                middle_char = current[length // 2]
                print(f"{length} {middle_char}")
                return

# To run it, just call it with the sample data:
find_password_easy(4, ["abc", "dfa", "feg", "cba"])
