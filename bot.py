import pyautogui as ag
import copy
import math
import sys
import time
import random

ag.FAILSAFE = True

# pyautogui
RESET_DURATION = 0.40  # in seconds
BUFFER_DURATION = 0.20  # in seconds
GRID_POS = [0.15, 0.5, 0.85]  # gird scaling
OFFSET_DEF_ZOOM = 0.35  # find pixel
RETINA_FACTOR = 2.0  # for MacBook
CROSS_COLOUR = (84, 84, 84, 255)  # 545454
CIRCLE_COLOR = (241, 235, 213, 255)  # F1EBD5
BG_COLOUR = (87, 186, 172, 255)  # 57BAAC

# minimax
POSSIBLE_MOVES = range(0, 9, 1)
PLAYER_CHAR = 'x'
OPP_CHAR = 'o'
EMPTY_CHAR = '_'
WIN_CONDITIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]
SCORE_WIN = 10
SCORE_LOSE = -10
SCORE_DRAW = 0


def evalBoard(board: list[int]) -> int:
    """This function assumes player is always using PLAYER_CHAR

    evalulate board state and return scores
    """
    for condition in WIN_CONDITIONS:
        c1, c2, c3 = condition
        if board[c1] == board[c2] == board[c3] and board[c1] != '_':
            if board[c1] == PLAYER_CHAR:
                if __debug__:
                    print("Player win")
                return SCORE_WIN
            elif board[c1] == OPP_CHAR:
                if __debug__:
                    print("Opponent win")
                return SCORE_LOSE

    if '_' not in board:
        if __debug__:
            print("Game draw")
        return SCORE_DRAW

    if __debug__:
        print("Game ongoing")
    return None


def minimax(board: list[int], maximiser_turn: bool, max_depth=10) -> int:
    """Returns best possible score for player

    Args:
        maximiser_turn
        true -> best score for x
        false -> best score of o
    """
    if __debug__:
        print("----------------")

    score = evalBoard(board)

    if __debug__:
        if maximiser_turn:
            print("Player:\t", PLAYER_CHAR)
        else:
            print("Player:\t", OPP_CHAR)
        print("Depth:\t", max_depth)
        print("Score:\t", score)
        printBoard(board)
        print("----------------")

    if max_depth == 0 or score is not None:
        return score

    if maximiser_turn:
        best_score = -math.inf
        for move in POSSIBLE_MOVES:
            if board[move] is EMPTY_CHAR:
                copy_board = copy.deepcopy(board)
                copy_board[move] = PLAYER_CHAR
                score = minimax(copy_board, False, max_depth-1)
                best_score = max(score, best_score)
        return best_score

    elif not maximiser_turn:
        best_score = +math.inf
        for move in POSSIBLE_MOVES:
            if board[move] is EMPTY_CHAR:
                copy_board = copy.deepcopy(board)
                copy_board[move] = OPP_CHAR
                score = minimax(copy_board, True, max_depth-1)
                best_score = min(score, best_score)
        return best_score


def matchPix(pixel_1: tuple[int, ...],
             pixel_2: tuple[int, ...],
             tolerance=0) -> bool:
    r, g, b = pixel_1[:3]
    exR, exG, exB = pixel_2[:3]
    return (
        (abs(r - exR) <= tolerance)
        and (abs(g - exG) <= tolerance)
        and (abs(b - exB) <= tolerance)
    )


def getBoard(board: list[float]) -> list[str]:
    # pixel match test
    im = ag.screenshot()
    board_array = []
    # update function to not take a million screenshot every loop
    for coord in board:
        pix = im.getpixel((coord[0], coord[1]))
        if (matchPix(pix, CIRCLE_COLOR, 10)):
            board_array.append('o')
            continue
        if (matchPix(pix, CROSS_COLOUR, 10)):
            board_array.append('x')
            continue
        if (matchPix(pix, BG_COLOUR, 10)):
            board_array.append('_')
            continue
        print("error reading board")
        return []

    if (len(board_array) == 9):
        return board_array
    else:
        print("error reading board")
        return []


def printBoard(board: list[float]):
    if len(board) != 9:
        print("corrupted board")
        return
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def main():
    try:
        restartButt = ag.locateCenterOnScreen('imgs/restart.png')
    except ag.ImageNotFoundException:
        print("restart button not found on screen.")
        sys.exit(0)

    # adjust scaling and reset board
    restartCoord = [coord / RETINA_FACTOR for coord in restartButt]
    ag.doubleClick(restartCoord[0], restartCoord[1])
    time.sleep(RESET_DURATION)

    baord_images = ['imgs/board.png', 'imgs/board_small.png']
    for img in baord_images:
        try:
            board = ag.locateOnScreen(img, confidence=0.9)
            if board:
                break
        except ag.ImageNotFoundException:
            print(img, "is not found on screen")

    try:
        board
    except NameError:
        print("Cannot locate board, try default browser zoom")
        sys.exit(0)

    # row major
    boardCoord = [
        [board.left + board.width * GRID_POS[0],
            board.top + board.height * GRID_POS[0]],
        [board.left + board.width * GRID_POS[1],
            board.top + board.height * GRID_POS[0]],
        [board.left + board.width * GRID_POS[2],
            board.top + board.height * GRID_POS[0]],
        [board.left + board.width * GRID_POS[0],
            board.top + board.height * GRID_POS[1]],
        [board.left + board.width * GRID_POS[1],
            board.top + board.height * GRID_POS[1]],
        [board.left + board.width * GRID_POS[2],
            board.top + board.height * GRID_POS[1]],
        [board.left + board.width * GRID_POS[0],
            board.top + board.height * GRID_POS[2]],
        [board.left + board.width * GRID_POS[1],
            board.top + board.height * GRID_POS[2]],
        [board.left + board.width * GRID_POS[2],
            board.top + board.height * GRID_POS[2]]
    ]

    # offset is for pixel matching, factor for retina screens
    offset = (board.width / RETINA_FACTOR) / 3 * OFFSET_DEF_ZOOM
    boardWithFactor = [[(coord - offset) for coord in sublist]
                       for sublist in boardCoord]
    boardCoord = [[(coord / RETINA_FACTOR) for coord in sublist]
                  for sublist in boardCoord]

    # test (cross win board)
    ag.click(boardCoord[0][0], boardCoord[0][1])
    time.sleep(BUFFER_DURATION)
    ag.click(boardCoord[1][0], boardCoord[1][1])
    time.sleep(BUFFER_DURATION)
    ag.click(boardCoord[4][0], boardCoord[4][1])
    time.sleep(BUFFER_DURATION)
    ag.click(boardCoord[6][0], boardCoord[6][1])
    time.sleep(BUFFER_DURATION)
    ag.click(boardCoord[7][0], boardCoord[7][1])
    time.sleep(BUFFER_DURATION)
    ag.click(boardCoord[5][0], boardCoord[5][1])
    time.sleep(BUFFER_DURATION)
    # end test

    print(minimax(getBoard(boardWithFactor), True))
    sys.exit(0)

    while 1:
        rand = random.randint(0, len(boardCoord) - 1)
        ag.click(boardCoord[rand][0], boardCoord[rand][1])


if __name__ == "__main__":
    main()
