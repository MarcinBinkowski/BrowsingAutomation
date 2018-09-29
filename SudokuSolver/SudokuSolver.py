

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

    def check_if_possible(self, y, x, number):

        for i in range(9):
            if self.board[y][i] == number:
                if i != x:
                    return False

        for i in range(9):
            if self.board[i][x] == number:
                if i != y:
                    return False

        if y < 3:
            temp = (0,3)
        elif y < 6:
            temp = (3,6)
        else:
            temp = (6,9)

        x = x - (x % 3)

        for i in range(3):
            if number in self.board[x][temp[0]:temp[1]]:
                return False

        return True

    def find_next_not_aasigned(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == "-":
                    return (i, j)
        return False


    def solve(self):
        if self.find_next_not_aasigned() == False:
            return True

        x_y_pair = self.find_next_not_aasigned()

        for number in range(1,10):
            if self.check_if_possible(x_y_pair[0], x_y_pair[1], number) is True:
                self.board[x_y_pair[0]][x_y_pair[1]] = number
                if self.solve() is True:
                    return True
                self.board[x_y_pair[0]][x_y_pair[1]] = "-"
        self.print_board()
        return False



if __name__ == "__main__":
    solver = SudokuSolver()
    solver.add_to_board(0,0,6)
    solver.add_to_board(0,1,5)
    solver.add_to_board(0,2,9)
    solver.add_to_board(0,4,1)
    solver.add_to_board(0,6,2)
    solver.add_to_board(0,7,8)
    solver.add_to_board(1,0,1)
    solver.add_to_board(1,4,5)
    solver.add_to_board(1,7,3)
    solver.add_to_board(2,0,2)
    solver.add_to_board(2,3,8)
    solver.add_to_board(2,7,1)
    solver.add_to_board(3,3,1)
    solver.add_to_board(3,4,3)
    solver.add_to_board(3,5,5)
    solver.add_to_board(3,7,7)
    solver.add_to_board(4,0,8)
    solver.add_to_board(4,3,9)
    solver.add_to_board(4,8,2)
    solver.add_to_board(5,2,3)
    solver.add_to_board(5,4,7)
    solver.add_to_board(5,5,8)
    solver.add_to_board(5,6,6)
    solver.add_to_board(5,7,4)
    solver.add_to_board(6,0,3)
    solver.add_to_board(6,2,2)
    solver.add_to_board(6,5,9)
    solver.add_to_board(6,8,4)
    solver.add_to_board(7,5,1)
    solver.add_to_board(7,6,8)
    solver.add_to_board(8,2,8)
    solver.add_to_board(8,3,7)
    solver.add_to_board(8,4,6)
    # solver.add_to_board(0,0,1)
    # solver.add_to_board(0, 1, 2)
    # solver.add_to_board(0, 2, 3)
    # solver.add_to_board(0, 3, 4)
    # solver.add_to_board(0, 4, 5)
    # solver.add_to_board(0, 5, 6)
    # solver.add_to_board(0, 6, 7)
    # solver.add_to_board(0, 7, 8)
    # solver.add_to_board(0, 8, 9)


    solver.print_board()
    print(solver.solve())
    print('solved')
    solver.print_board()
