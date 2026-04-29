def solve():
    try:
        # Read number of test cases
        t_str = input().split()
        if not t_str:
            return
        t = int(t_str[0])
        
        for _ in range(t):
            # Read array size
            n = int(input())
            # Read array elements and sort them
            arr = list(map(int, input().split()))
            arr.sort()
            
            # current_even represents the next even number we want to 'fill'
            current_even = 2
            
            for num in arr:
                # If the current number can be decremented to reach 
                # or exceed our target even number
                if num >= current_even:
                    # We 'use' this slot and move to the next even number
                    current_even += 2
            
            # The smallest positive multiple of 2 not in our 
            # optimized array is the result
            print(current_even)
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()