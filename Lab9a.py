N = 8
solutions = []
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve(row, board):
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(row + 1, board)
def print_solution(board, num):
    print(f"Solution {num}:")
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
board = [-1] * N
solve(0, board)
for i, sol in enumerate(solutions, start=1):
    print_solution(sol, i)
print("Total Solutions:", len(solutions))