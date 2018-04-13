# Just your average Connect Four game
# CC, 2017

from random import random

"""Coin toss for first move"""
player_symbol = 'O'
computer_symbol = 'X'

if random() > .5:
    # Player goes first
    print 'Player moves first.'
    turn_index = 0
else:
    # Computer goes first
    print 'Computer moves first.'
    turn_index = 1

def display(grid):
    """ Prints the grid"""
    print ''
    print '   0   1   2   3   4   5   6'
    for i in range(6):
        print i, '',
        for j in range(7):
            if grid[str(i) + str(j)] is None:
                print '.  ',
            else:
                print grid[str(i) + str(j)], ' ',
        print ''
    print ''

def wins(grid, player):
    """Return True if the player has four pieces in a row"""
    # Row win
    for i in range(6):
        for j in range(4):
            if (grid[str(i)+str(j)] == player and grid[str(i)+str(j+1)] == player and
                grid[str(i)+str(j+2)] == player and grid[str(i)+str(j+3)] == player):
                    return True

     # Column win
    for j in range(7):
        for i in range(3):
            if (grid[str(i)+str(j)] == player and
                grid[str(i+1) + str(j)] == player and
                grid[str(i+2) + str(j)] == player and
                grid[str(i+3) + str(j)] == player):
                    return True

    # Diagonal (/) win
    for i in range(5, 2, -1):
        for j in range(4):
            if (grid[str(i)+str(j)] == player and
            grid[str(i-1) + str(j+1)] == player and
            grid[str(i-2) + str(j+2)] == player and
            grid[str(i-3) + str(j+3)] == player):
                return True

    # Diagonal (\) win
    for i in range(3):
        for j in range(4):
            if (grid[str(i)+str(j)] == player and
            grid[str(i+1) + str(j+1)] == player and
            grid[str(i+2) + str(j+2)] == player and
            grid[str(i+3) + str(j+3)] == player):
                return True

    return False


def score(grid):
    """Score the board based on computer's perspective"""
    if wins(grid, computer_symbol):
        return 1
    elif wins(grid, player_symbol):
        return -1
    else:
        return 0


def minimax(grid, depth, alpha, beta, is_max_player):
    current_score = score(grid)
    if current_score != 0 or depth == 0:
        return current_score, None

    if is_max_player:
        best_value = -42 ** 10
        best_move = None

        for col in range(7):
            if grid['0'+str(col)] != None:
                continue

            for i in range(5, -1, -1):
                if grid[str(i)+str(col)] == None:
                    grid[str(i)+str(col)] = computer_symbol
                    break

            value, response = minimax(grid, depth-1, alpha, beta, False)
            grid[str(i)+str(col)] = None
            alpha = max(alpha, value)

            if value > best_value:
                best_value = value
                best_move = str(col)

            if beta <= alpha:
                break

    if not is_max_player:
        best_value = 42 ** 10
        best_move = None

        for col in range(7):
            if grid['0'+str(col)] != None:
                continue

            for i in range(5, -1, -1):
                if grid[str(i)+str(col)] == None:
                    grid[str(i)+str(col)] = player_symbol
                    break

            value, response = minimax(grid, depth-1, alpha, beta, True)
            grid[str(i)+str(col)] = None
            beta = min(beta, value)

            if value < best_value:
                best_value = value
                best_move = str(col)

            if beta <= alpha:
                break

    return best_value, best_move


def get_move(grid):
    flag = True

    while flag:
        flag = False

        print 'Which column (0-6) would you like to drop your piece?'
        move = int(raw_input())

        if move < 0 or move > 6:
            print 'Please stay within the grid.\n'
            flag = True
            continue

        if (grid['0'+str(move)] != None):
            print 'Column filled. Please choose another column.\n'
            flag = True

    return str(move)


def play():
    grid = {}
    for i in range(6):
        for j in range(7):
            grid[str(i) + str(j)] = None

    display(grid)
    turn = 0

    while turn < 42:
        if turn % 2 == turn_index:
            move = get_move(grid)
            for i in range(5, -1, -1):
                if grid[str(i)+move] == None:
                    grid[str(i)+move] = player_symbol
                    break
        else:
            value, move = minimax(grid, 9, -42 ** 10, 42 ** 10, True)
            print 'I will drop my chip down column %s.' % move
            print move
            for i in range(5, -1, -1):
                if grid[str(i)+move] == None:
                    grid[str(i)+move] = computer_symbol
                    break

        display(grid)
        if wins(grid, player_symbol):
            print '\nA haiku for you:'
            print '    Human v. Machine:'
            print '    You won against an A.I.'
            print '    Good for you, I guess.'
            print ''
            turn = 42
        elif wins(grid, computer_symbol):
            print '\nA haiku for you:'
            print '    In case you can\'t hear'
            print '    The computer is calling'
            print '    you -- inadequate.'
            print ''
            turn = 42
        turn += 1

    if turn == 42:
        print '\nA haiku for you:'
        print '    Mediocrity\n    When you neither win nor lose'
        print '    You should not have played'
        print ''

if __name__ == '__main__':
    play()
