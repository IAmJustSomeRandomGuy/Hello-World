import random

rows = ' [0, 1, 2] \n [3, 4, 5] \n [6, 7, 8] '
p1 = '1'
p2 = '2'
winner = None
num_range = list(range(9))
moves = random.randint(0, 1)

if moves % 2 == 0:
    print('player 1 starts (○)')
elif moves % 2 == 1:
    print('player 2 starts (x)')


def user_input(player):
    global user
    print(rows)

    while user not in num_range:
        try:
            user = int(input('Pick a on the board: '))
        except ValueError:
            print('Wrong input')

    num_range.remove(user)

    replace_board(player)


def replace_board(who):
    global replace_with, rows

    replace_with = who
    if who == p1:
        replace_with = '○'
    elif who == p2:
        replace_with = 'x'

    rows = rows.replace(str(user), replace_with)


def check_winner():
    global winner
    if rows[2] == rows[14] == rows[26] or rows[5] == rows[17] == rows[29] or rows[8] == rows[20] == rows[32]:
        winner = replace_with
    elif rows[2] == rows[5] == rows[8] or rows[14] == rows[17] == rows[20] or rows[26] == rows[29] == rows[32]:
        winner = replace_with
    elif rows[2] == rows[17] == rows[32] or rows[8] == rows[17] == rows[26]:
        winner = replace_with

    if winner == '○':
        print(rows)
        print('Player 1 won')
    elif winner == 'x':
        print(rows)
        print('Player 2 won')
    elif len(num_range) == 0:
        winner = 'both'
        print(rows)
        print("It's a tie")


while winner is None:
    user = ''
    if moves % 2 == 0:
        user_input(p1)
    elif moves % 2 == 1:
        user_input(p2)
    moves += 1

    check_winner()
