board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

x_win = ['X', 'X', 'X']
o_win = ['O', 'O', 'O']

board_t = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
cor1 = [board[0][0], board[1][1], board[2][2]]
cor2 = [board[2][0], board[1][1], board[0][2]]
count_x = 0
count_o = 0
count = 0


def update_board():
    global board_t, cor1, cor2, count
    count += 1
    board_t = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    cor1 = [board[0][0], board[1][1], board[2][2]]
    cor2 = [board[2][0], board[1][1], board[0][2]]


def print_board():
    print("---------")
    for i in board:
        print("| {} {} {} |".format(i[0], i[1], i[2]))
    print("---------")


def o_wins():
    for i in range(0, 3):
        if board[i] == o_win or board_t[i] == o_win:
            return True
        if cor1 == o_win or cor2 == o_win:
            return True


def x_wins():
    for i in range(0, 3):
        if board[i] == x_win or board_t[i] == x_win:
            return True
        if cor1 == x_win or cor2 == x_win:
            return True


def impossible():
    if x_wins() and o_wins():
        return True
    elif abs(count_x - count_o) > 1:
        return True


def draw():
    var = True
    if x_wins() and o_wins():
        return True

    for i in board:
        if "_" in i:
            var = False

    if var:
        return True


def current_situation():
    if impossible():
        print("Impossible!")
    elif x_wins():
        print("X wins!")
    elif o_wins():
        print("O wins!")
    elif draw():
        print("Draw!")
    else:
        return True


def next_move():
    global count, count_x, count_o

    while True:
        raw_input = input()
        next_move_cord1, next_move_cord2 = raw_input.split(' ')
        if next_move_cord1.isdigit() and next_move_cord2.isdigit():
            next_move_cord1 = int(next_move_cord1)
            next_move_cord2 = int(next_move_cord2)
        else:
            print("You should enter numbers!")
            continue

        if next_move_cord1 > 3 or next_move_cord2 > 3 or \
                next_move_cord1 < 1 or next_move_cord2 < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        if next_move_cord2 == 3 and board[0][next_move_cord1 - 1] is not '_' or \
                next_move_cord2 == 2 and board[1][next_move_cord1 - 1] is not '_' or \
                next_move_cord2 == 1 and board[2][next_move_cord1 - 1] is not '_':
            print("This cell is occupied! Choose another one!")
            continue

        if count % 2 is 0:
            count_x += 1
            if next_move_cord2 == 3:
                board[0][next_move_cord1 - 1] = 'X'
            elif next_move_cord2 == 2:
                board[1][next_move_cord1 - 1] = 'X'
            else:
                board[2][next_move_cord1 - 1] = 'X'
        else:
            count_o += 1
            if next_move_cord2 == 3:
                board[0][next_move_cord1 - 1] = 'O'
            elif next_move_cord2 == 2:
                board[1][next_move_cord1 - 1] = 'O'
            else:
                board[2][next_move_cord1 - 1] = 'O'

        update_board()
        break


print_board()

while current_situation():
    next_move()
    print_board()
