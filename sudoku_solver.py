class SudokuSolver:
    def __init__(self, board=None):
        self.board = board if board else [[0]*9 for _ in range(9)]

    def print_board(self):
        """Print the Sudoku board in a formatted way."""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def find_empty(self):
        """Find an empty cell in the board."""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, num, pos):
        """Check if the number is valid in the given position."""
        # Check row
        for j in range(9):
            if self.board[pos[0]][j] == num and pos[1] != j:
                return False

        # Check column
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve(self):
        """Solve the Sudoku puzzle using backtracking."""
        empty = self.find_empty()
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def validate_board(self):
        """Validate if the input board is valid."""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    num = self.board[i][j]
                    self.board[i][j] = 0
                    if not self.is_valid(num, (i, j)):
                        self.board[i][j] = num
                        return False
                    self.board[i][j] = num
        return True