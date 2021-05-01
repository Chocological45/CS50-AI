"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Check that the board is in its initial state and bypass the rest of the code
    if board == initial_state():
        return X

    count_x = 0
    count_o = 0

    # Count the number of Xs and Os in the board
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)

    # Compare symbol counts
    # If the number of X's is greater than number of O's, O is next player
    if count_x > count_o:
        return O

    # If number of X's equals number of O's, X is next player
    elif count_x == count_o:
        return X

    # If the board is terminal then return None. Game is over
    elif terminal(board):
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Use set as to prevent duplicate move set entries
    moves = set()

    # Go through the board and gather the empty spots into moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                # Add the tuple (i, j) to the moves list
                moves.add((i, j))

    # Return the possible move set
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If the board is terminal, raise exception
    if terminal(board):
        raise ValueError("Game Over")

    # If action is not a valid action, raise exception
    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")

    # Use copy() to make a new deep copy of the board
    board_state = copy.deepcopy(board)
    # Use player(board) to get the next player's action
    board_state[action[0]][action[1]] = player(board)

    # Return the board state
    return board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # For X and O
    for players in (X, O):
        # Check state of horizontals
        for row in range(3):
            if all(board[row][col] == players for col in range(3)):
                return players

        # Check state of verticals
        for col in range(3):
            if all(board[row][col] == players for row in range(3)):
                return players

        # Check state of diagonals
        if all(board[i][i] == players for i in range(len(board))):
            return players

        if all(board[i][len(board) - i - 1] == players for i in range(len(board))):
            return players

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check that there is a winner and terminate the game
    if winner(board) is not None:
        return True

    # Check that all cells in the board are filled or not
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check that the board is not terminal before looking for optimal action
    if terminal(board):
        return None

    #if board == initial_state():
    #    return random.randint(0, 2), random.randint(0, 2)

    if player(board) == X:
        # Return optimal solution for when player is X
        optimal = -math.inf
        for action in actions(board):
            max_v = min_m(result(board, action))
            if max_v > optimal:
                optimal = max_v
                optimal_action = action

    elif player(board) == O:
        # Return optimal solution for when player is Y
        optimal = math.inf
        for action in actions(board):
            min_v = max_m(result(board, action))
            if min_v < optimal:
                optimal = min_v
                optimal_action = action

    return optimal_action


def max_m(board):
    if terminal(board):
        return utility(board)

    val = -math.inf
    for action in actions(board):
        val = max(val, min_m(result(board, action)))

    return val


def min_m(board):
    if terminal(board):
        return utility(board)

    val = math.inf
    for action in actions(board):
        val = min(val, max_m(result(board, action)))

    return val
