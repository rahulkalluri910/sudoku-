from sudoku_solver import SudokuSolver

def get_puzzle_input():
    """Get Sudoku puzzle input from user."""
    print("Enter Sudoku puzzle row by row (use 0 for empty cells)")
    print("Example: 530070000 for first row")
    board = []
    
    for i in range(9):
        while True:
            row = input(f"Enter row {i + 1}: ")
            if len(row) == 9 and row.isdigit() and all(0 <= int(x) <= 9 for x in row):
                board.append([int(x) for x in row])
                break
            else:
                print("Invalid input! Please enter 9 digits (0-9)")
    
    return board

def main():
    print("Welcome to Sudoku Solver!")
    print("\nChoose input method:")
    print("1. Enter your own puzzle")
    print("2. Use example puzzle")
    
    choice = input("\nEnter choice (1/2): ")
    
    if choice == '1':
        board = get_puzzle_input()
    else:
        # Example puzzle (0 represents empty cells)
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    
    solver = SudokuSolver(board)
    
    print("\nInput puzzle:")
    solver.print_board()
    
    if not solver.validate_board():
        print("\nInvalid puzzle! The input contains conflicts.")
        return
    
    print("\nSolving...")
    if solver.solve():
        print("\nSolution found:")
        solver.print_board()
    else:
        print("\nNo solution exists for this puzzle!")

if __name__ == "__main__":
    main()