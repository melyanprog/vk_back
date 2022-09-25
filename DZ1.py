class TicTac:
    def __init__(self):
        self.board = list(range(1, 10))
        self.win_cor = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def dr_board(self):
        print("\033[1m{}\033[0m".format('-------------'))
        for i in range(0, 3):
            print('|', self.board[0+i*3], '|',
                  self.board[1+i*3], '|', self.board[2+i*3], '|')
            print("\033[1m{}\033[0m".format('-------------'))

    def valid_input(self, player):
        valid = False
        while not valid:
            print('Ходит: ' + player)
            player_ans = input('Выберете поле: ')
            try:
                player_ans = int(player_ans)
            except:
                print('Введите число')
                continue
            if player_ans >= 1 and player_ans <= 9:
                if self.board[player_ans-1] != 'X' and self.board[player_ans-1] != 'O':
                    self.board[player_ans-1] = player
                    valid = True
                else:
                    print('Клетка уже занята')
            else:
                print('Введите число от 1 до 9')

    def check_win(self):
        for each in self.win_cor:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def game(self):
        count = 0
        win = False
        while not win:
            self.dr_board()
            if count % 2 == 0:
                self.valid_input("\033[34m{}\033[0m".format("X"))
            else:
                self.valid_input("\033[31m{}\033[0m".format("O"))
            count += 1
            if count > 4:
                winner = self.check_win()
                if winner:
                    print('Победил :' + winner)
                    win = True
                    break
            if count == 9:
                print('Ничья')
                break
        self.dr_board()


g = TicTac()
g.game()
