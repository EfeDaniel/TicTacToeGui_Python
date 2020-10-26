class Tic_Tac_Toe:
    def __init__(self):
        #defining the board  3 x 3 matrix
        self.B = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.player = 1

    def get_open_spots(self):
        return [[row, column] for row in range(3) for column in range(3)
                if self.B[row][column] == 0]

    def is_valid_move(self, r, c):
        if 0 <= r <= 2 and 0 <= c <= 2 and self.B[r][c] == 0:

            return True

        return False

    def make_move(self, r, c):
        if self.is_valid_move(r, c):
            self.B[r][c] = self.player
            self.player = (self.player + 2) % 2 + 1

    def check_for_winner(self):

        for c in range(3):
            #checking the row for a valid move
            if self.B[0][c] == self.B[1][c] == self.B[2][c] != 0:
                return self.B[0][c]
        for r in range(3):
            if self.B[r][0] == self.B[r][1] == self.B[r][2] != 0:
                return self.B[r][0]
            if self.B[0][0] == self.B[0][1] == self.B[0][2] != 0:
                return self.B[0][0]
            if self.B[2][0] == self.B[1][1] == self.B[0][2] != 0:
                return self.B[2][0]
            if self.get_open_spots() == []:
                return 0
            return -1

    def print_board(self):
        chars = ['-', 'X', 'O']

        for r in range(3):
            for c in range(3):
                print(chars[game.B[r][c]], end=' ')
            print()

game =  Tic_Tac_Toe()
while game.check_for_winner()==-1:
    game.print_board()
    r,c = eval(input('Enter spot, player ' + str(game.player) + ': '))
    game.make_move(r,c)




x = game.check_for_winner()
if x==0:
    print("It's a draw.")
else:
    print('Player', x, 'wins!')
