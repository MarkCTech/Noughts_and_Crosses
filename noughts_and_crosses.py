import random


def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    choice = 'WRONG'
    while choice not in ['X', 'x', 'O', 'o']:
        choice = input('Choose marker X or O: ')

        if choice not in ['X', 'x', 'O', 'o']:
            print(100 * '\n')
            print('Enter X or O')
    return choice.upper()


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    win = [mark, mark, mark]

    c1 = [board[1], board[2], board[3]]
    c2 = [board[4], board[5], board[6]]
    c3 = [board[7], board[8], board[9]]
    c4 = [board[1], board[4], board[7]]
    c5 = [board[2], board[5], board[8]]
    c6 = [board[3], board[6], board[9]]
    c7 = [board[1], board[5], board[9]]
    c8 = [board[3], board[5], board[7]]

    conditions = [c1, c2, c3, c4, c5, c6, c7, c8]

    def win_condition(n):
        return n == win

    result = any(map(win_condition, conditions))
    return result


def choose_first():
    chooser = random.randint(1, 2)

    if chooser == 1:
        return 'X'
    else:
        return 'O'


def space_check(board, position):
    return board[position] == 'X' or board[position] == 'O'


def full_board_check(board):
    index = 1
    checklist = []

    while index in range(1, 10):
        checklist.append(space_check(board, index))
        index += 1

    res = all(i for i in checklist)

    return res


def player_choice(board):
    choice = 'WRONG'
    acceptable_range = range(1, 10)
    within_range = False

    while not choice.isdigit() or not within_range:
        choice = input('Choose position 1-9: ')

        if not choice.isdigit():
            print('That is not a digit!')

        if choice.isdigit():
            if int(choice) not in acceptable_range:
                print('Must be in range 1-9: ')
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
    result = int(choice)

    if not space_check(board, result):
        print(100 * '\n')
        return result


def replay():
    choice = 'WRONG'

    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input('Would you like to play again? Y/N: ')
        if choice not in ['Y', 'y', 'N', 'n']:
            print('Enter Y or N ')

    if choice.upper() == 'Y':
        return True
    else:
        return False


def main():

    blank_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    num_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = blank_board
    position = 0
    player_2 = ''

    print('Welcome to Tic Tac Toe!')

    player_1 = player_input()
    if player_1 == 'X':
        player_2 = 'O'
    elif player_1 == 'O':
        player_2 = 'X'
    print(100 * '\n')
    print(f'Player 1 is {player_1}\nPlayer 2 is {player_2}\n')
    mark = choose_first()

    display_board(num_board)

    while not win_check(board, mark) or not full_board_check(board):

        print('\n')
        display_board(board)

        while position == 0 or position is None:
            print(f"Player {mark}'s turn")
            position = player_choice(board)
            if position is not None:
                place_marker(board, mark, position)
                display_board(board)

        if win_check(board, mark):
            print(f'Player {mark} wins!')
            if replay():
                blank_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                board = blank_board
            else:
                print('Goodbye!')
                break

        elif full_board_check(board):
            print(f'Board is full!')
            if replay():
                print(100 * '\n')
                blank_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                board = blank_board
            else:
                print('Goodbye!')
                break

        if mark == 'X':
            mark = 'O'
        elif mark == 'O':
            mark = 'X'
        position = 0
        print(100 * '\n')


if __name__ == '__main__':
    main()
