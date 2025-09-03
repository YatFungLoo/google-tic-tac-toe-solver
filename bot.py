import pyautogui as ag
import time
import sys
import random


RESET_DURATION = 0.3  # in seconds
GRID_POS = [0.15, 0.5, 0.85]  # gird scaling
OFFSET_PIXEL = 0.33  # find pixel
CROSS_COLOUR = '545454'
CIRCLE_COLOR = 'F1EBD5'
GREEN_COLOR = '57BAAC'


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

    # offset
    offset = board.width * OFFSET_PIXEL

    boardCoord = [[coord / 2 for coord in sublist]
                  for sublist in boardCoord]

    # for c in boardCoord:
    #     ag.moveTo(c[0], c[1])
    # sys.exit(0)

    # TL 330 455, BL 330 518, TR 393 455
    # 375, 475
    # 93-74,

    # main loop
    while 1:
        rand = random.randint(0, len(boardCoord) - 1)
        ag.click(boardCoord[rand][0], boardCoord[rand][1])


if __name__ == "__main__":
    main()
