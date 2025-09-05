import pyautogui as ag
import time
import sys
import random


RESET_DURATION = 0.3  # in seconds
GRID_POS = [0.15, 0.5, 0.85]  # gird scaling
OFFSET_DEF_ZOOM = 0.16  # find pixel
RETINA_FACTOR = 2  # for MacBook
CROSS_COLOUR = (84, 84, 84)  # 545454
CIRCLE_COLOR = (241, 235, 213)  # F1EBD5
BG_COLOUR = (87, 186, 172)  # 57BAAC


def main():
    try:
        restartButt = ag.locateCenterOnScreen('imgs/restart.png')
    except ag.ImageNotFoundException:
        print("restart button not found on screen.")
        sys.exit(0)
    restartCoord = [coord / 2 for coord in restartButt]

    # focus and reset board
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

    # adjust for retina / add offset
    offset = (board.width / RETINA_FACTOR) / 3 * OFFSET_DEF_ZOOM
    boardCoord = [[(coord / RETINA_FACTOR - offset) for coord in sublist]
                  for sublist in boardCoord]

    ag.click(boardCoord[0][0], boardCoord[0][1])
    time.sleep(1)
    ag.click(boardCoord[1][0], boardCoord[1][1])

    # main loop
    region = [coord / RETINA_FACTOR for coord in board]
    pix_circle = ag.pixel(boardCoord[0][0], boardCoord[0][1])
    print(pix_circle)
    print(CIRCLE_COLOR)
    pix_cross = ag.pixel(boardCoord[1][0], boardCoord[1][1])
    print(pix_cross)
    print(CROSS_COLOUR)
    pix_empty = ag.pixel(boardCoord[2][0], boardCoord[2][1])
    print(pix_empty)
    print(BG_COLOUR)
    if pix_circle == CIRCLE_COLOR:
        print("found circle")
    if pix_cross == CROSS_COLOUR:
        print("found cross")
    if pix_empty == BG_COLOUR:
        print("found background")
    sys.exit(0)

    while 1:
        rand = random.randint(0, len(boardCoord) - 1)
        ag.click(boardCoord[rand][0], boardCoord[rand][1])


if __name__ == "__main__":
    main()
