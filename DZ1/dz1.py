"""TicTac game"""


class TicTac:
    '''TicTac class'''

    def __init__(self):
        self.board = list(range(1, 10))
        self.win_cor = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.x_sym = "\033[34mX\033[0m"
        self.o_sym = "\033[31mO\033[0m"

    def dr_board(self):
        '''draw board to console'''
        print("\033[1m-------------\033[0m")
        for i in range(0, 3):
            print('|', self.board[0+i*3], '|',
                  self.board[1+i*3], '|', self.board[2+i*3], '|')
            print("\033[1m-------------\033[0m")

    def valid_input(self, player):
        '''validating input'''
        print(f"Ходит:  {player}")
        player_ans = input('Выберете поле: ')
        player_ans = int(player_ans)
        if player_ans < 1 or player_ans > 9:
            raise ValueError('Введите число от 1 до 9')
        if self.board[player_ans-1] == self.x_sym or self.board[player_ans-1] == self.o_sym:
            raise ValueError('Клетка уже занята')
        return player_ans

    def check_win(self):
        '''check_win function'''
        for each in self.win_cor:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def game(self):
        '''game function'''
        count = 0
        win = False
        while not win:
            self.dr_board()
            player = ""
            if count % 2 == 0:
                player = self.x_sym
            else:
                player = self.o_sym
            while True:
                try:
                    player_ans = self.valid_input(player)
                    self.board[player_ans-1] = player
                    break
                except ValueError as error:
                    print(error)
            count += 1
            if count > 4:
                winner = self.check_win()
                if winner:
                    print(f"Победил : {winner}")
                    win = True
                    break
            if count == 9:
                print('Ничья')
                break
        self.dr_board()


if __name__ == '__main__':
    g = TicTac()
    g.game()
