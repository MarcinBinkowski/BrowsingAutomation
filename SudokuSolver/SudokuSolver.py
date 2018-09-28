

class SudokuSolver:

    def __init__(self):
        self.board = [[["" for x in range(3)] for y in range(3)] for i in range(9)]
        self.current_coords = (0,0)

    def add_to_board(self, column, row, number):
        self.board[row][column] = number

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[3*i+j])
            print()

    def check_if_possible(self, y, x, number):
        for i in range(9):
            if self.board[y][i] == number:
                if i != x:
                    return False
        for i in range(9):
            if self.board[i][x] == number:
                if i != y:
                    return False
        for i in range(3)
        return True



    def solve(self, y, x):
        if self.board[y][x] == "":
            self.board[y][x] = 1






if __name__ == "__main__":
    solver = SudokuSolver()
    solver.print_board()
    # solver.add_to_board(0,0,3)
    #
    # solver.print_board()
    # print(solver.check_if_possible(0,1,3))