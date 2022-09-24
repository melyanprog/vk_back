
board = list(range(1, 10))
win_cor = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
           (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def dr_board(board):
    print('-------------')
    for i in range(0, 3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')


def valid_input(player):
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
            if board[player_ans-1] != 'X' and board[player_ans-1] != 'O':
                board[player_ans-1] = player
                valid = True
            else:
                print('Клетка уже занята')
        else:
            print('Введите числj от 1 до 9')


def check_win(board):
    for each in win_cor:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    count = 0
    win = False
    while not win:
        dr_board(board)
        if count % 2 == 0:
            valid_input('X')
        else:
            valid_input('O')
        count += 1
        if count > 4:
            winner = check_win(board)
            if winner:
                print('Победил :' + winner)
                win = True
                break
        if count == 9:
            print('Ничья')
            break
    dr_board(board)


main(board)
