import random


def display_board(board):
    print('\n'*20)
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|'  + ' ' + board[9] + ' ')
    print('-----------')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|'  + ' ' + board[6] + ' ')
    print('-----------')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|'  + ' ' + board[3] + ' ')


def player_input():

    '''
    OUTPUT = (player 1 marker, player 2 marker)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, mark):

    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))


def choose_first():
    first_player_num = random.randint(1,2)

    if first_player_num == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False

    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: 1- 9: '))

    return position


def replay():

    answer = input('Do you want to play again? y for yes and n for no: ')

    return answer.lower() == 'y'

# WHILE LOOP TO KEEP RUNNING THE GAME

print('Welcome to Tick Tack Toe')


while True:

    the_board = [' ']*10
    display_board(the_board)
    player1,player2 = player_input()
    turn = choose_first()

    print(turn + ' Will go first!')

    play_game = input('Ready to play? y or n: ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Display the board

        if turn == 'Player 1':

            display_board(the_board)
            # define position to place
            position = player_choice(the_board)
            # set marker
            place_marker(the_board, player1, position)

            if win_check(the_board, player1):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Its a tie!')
                    game_on = False

                else:
                    turn = 'Player 2'


        else:

            display_board(the_board)
            # define position to place
            position = player_choice(the_board)
            # set marker
            place_marker(the_board, player2, position)

            if win_check(the_board, player2):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False

            else:
                if full_board_check(the_board):
                    print('Its a tie!')
                    game_on = False

                else:
                    turn = 'Player 1'


    if not replay():
        break
