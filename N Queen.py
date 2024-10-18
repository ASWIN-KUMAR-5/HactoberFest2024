def solveNQueens(N):
    def isSafe(row, col):
        # Check the column and diagonals for threats from other queens
        return col not in cols and (row - col) not in diagonals1 and (row + col) not in diagonals2

    def placeQueen(row):
        # If all queens are placed, add the solution
        if row == N:
            board = []
            for r in range(N):
                row_str = '.' * N
                row_str = row_str[:queens[r]] + 'Q' + row_str[queens[r] + 1:]
                board.append(row_str)
            solutions.append(board)
            return
        
        for col in range(N):
            if isSafe(row, col):
                # Place the queen and mark the column and diagonals
                queens[row] = col
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                
                # Recursively place queens in the next row
                placeQueen(row + 1)

                # Backtrack
                queens[row] = -1
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

    solutions = []
    queens = [-1] * N  # queens[i] = column of the queen in the i-th row
    cols = set()       # columns where queens are placed
    diagonals1 = set() # row - col
    diagonals2 = set() # row + col
    placeQueen(0)
    return solutions

# Test Cases
print(solveNQueens(4))  # Example 1
print(solveNQueens(1))  # Example 2
print(solveNQueens(3))  # Example 3
