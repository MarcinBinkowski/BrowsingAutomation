

class SudokuSolver:

    def __init__(self):
        self.board = [["-" for x in range(9)] for y in range(9)]
        self.current_coords = (0, 0)

    def add_to_board(self, column, row, number):
        self.board[column][row] = number

    def print_board(self):
        print("\n")
        print("               BOARD             ")
        print("   ", end="")
        for i in range(9):
            print(" " + str(i) + " ", end="")
            if i % 3 == 2:
                print(" ", end="")
        print("\n  -------------------------------")
        for i in range(9):
            print(str(i) + " ", end="")
            print("|", end="")
            for j in range(9):
                print(" " + str(self.board[i][j])+" ", end="")
                if j % 3 == 2:
                    print("|", end="")
            if i % 3 == 2:
                print("\n  -------------------------------", end="")
            print()

    def print_without_effects(self):
        for i in self.board:
            print(i)

    def used_in_row(self, row, number):
        for col in range(9):
            if str(self.board[row][col]) == str(number):
                return True
        return False

    def used_in_col(self, col, number):
        for row in range(9):
            if str(self.board[row][col]) == str(number):
                return True
        return False

    def used_in_box(self, box_start_row, box_start_col, number):
        for row in range(3):
            for col in range(3):
                if str(self.board[row + box_start_row][col + box_start_col]) == str(number):
                    return True
        return False

    def is_safe(self, row, col, number):
        return not self.used_in_row(row, number)\
                                    and not self.used_in_col(col, number) \
                                    and not self.used_in_box(row - row % 3, col - col % 3, number)

    def find_next_not_aasigned(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == "-":
                    return i, j
        return False

    def solve(self):
        if self.find_next_not_aasigned() is False:
            return True

        x_y_pair = self.find_next_not_aasigned()

        for number in range(1, 10):
            if self.is_safe(x_y_pair[0], x_y_pair[1], number) is True:
                self.board[x_y_pair[0]][x_y_pair[1]] = number
                if self.solve() is True:
                    return True
                self.board[x_y_pair[0]][x_y_pair[1]] = "-"
        return False


if __name__ == "__main__":
    solver = SudokuSolver()

    solver.add_to_board(0, 0, '-')
    solver.add_to_board(1, 0, '-')
    solver.add_to_board(2, 0, '-')
    solver.add_to_board(3, 0, '5')
    solver.add_to_board(4, 0, '7')
    solver.add_to_board(5, 0, '-')
    solver.add_to_board(6, 0, '-')
    solver.add_to_board(7, 0, '2')
    solver.add_to_board(8, 0, '-')
    solver.add_to_board(0, 1, '9')
    solver.add_to_board(1, 1, '-')
    solver.add_to_board(2, 1, '3')
    solver.add_to_board(3, 1, '2')
    solver.add_to_board(4, 1, '-')
    solver.add_to_board(5, 1, '-')
    solver.add_to_board(6, 1, '-')
    solver.add_to_board(7, 1, '-')
    solver.add_to_board(8, 1, '-')
    solver.add_to_board(0, 2, '-')
    solver.add_to_board(1, 2, '-')
    solver.add_to_board(2, 2, '7')
    solver.add_to_board(3, 2, '-')
    solver.add_to_board(4, 2, '-')
    solver.add_to_board(5, 2, '-')
    solver.add_to_board(6, 2, '-')
    solver.add_to_board(7, 2, '8')
    solver.add_to_board(8, 2, '3')
    solver.add_to_board(0, 3, '7')
    solver.add_to_board(1, 3, '4')
    solver.add_to_board(2, 3, '-')
    solver.add_to_board(3, 3, '-')
    solver.add_to_board(4, 3, '3')
    solver.add_to_board(5, 3, '6')
    solver.add_to_board(6, 3, '2')
    solver.add_to_board(7, 3, '-')
    solver.add_to_board(8, 3, '-')
    solver.add_to_board(0, 4, '2')
    solver.add_to_board(1, 4, '9')
    solver.add_to_board(2, 4, '-')
    solver.add_to_board(3, 4, '-')
    solver.add_to_board(4, 4, '-')
    solver.add_to_board(5, 4, '7')
    solver.add_to_board(6, 4, '-')
    solver.add_to_board(7, 4, '-')
    solver.add_to_board(8, 4, '-')
    solver.add_to_board(0, 5, '-')
    solver.add_to_board(1, 5, '-')
    solver.add_to_board(2, 5, '-')
    solver.add_to_board(3, 5, '-')
    solver.add_to_board(4, 5, '-')
    solver.add_to_board(5, 5, '2')
    solver.add_to_board(6, 5, '6')
    solver.add_to_board(7, 5, '7')
    solver.add_to_board(8, 5, '1')
    solver.add_to_board(0, 6, '-')
    solver.add_to_board(1, 6, '1')
    solver.add_to_board(2, 6, '9')
    solver.add_to_board(3, 6, '7')
    solver.add_to_board(4, 6, '-')
    solver.add_to_board(5, 6, '-')
    solver.add_to_board(6, 6, '-')
    solver.add_to_board(7, 6, '-')
    solver.add_to_board(8, 6, '-')
    solver.add_to_board(0, 7, '-')
    solver.add_to_board(1, 7, '-')
    solver.add_to_board(2, 7, '2')
    solver.add_to_board(3, 7, '3')
    solver.add_to_board(4, 7, '4')
    solver.add_to_board(5, 7, '-')
    solver.add_to_board(6, 7, '-')
    solver.add_to_board(7, 7, '-')
    solver.add_to_board(8, 7, '5')
    solver.add_to_board(0, 8, '-')
    solver.add_to_board(1, 8, '-')
    solver.add_to_board(2, 8, '-')
    solver.add_to_board(3, 8, '-')
    solver.add_to_board(4, 8, '8')
    solver.add_to_board(5, 8, '-')
    solver.add_to_board(6, 8, '4')
    solver.add_to_board(7, 8, '9')
    solver.add_to_board(8, 8, '2')

    solver.print_board()
    solver.solve()
    solver.print_board()
