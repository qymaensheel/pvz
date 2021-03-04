import pygame
import board_data


generationTime = 10000


def getGridCoords(mx, my):

    if mx < board_data.Xmin:
        return 0, 0
    if mx > board_data.Xmax:
        return 0, 0
    if my < board_data.Ymin:
        return 0, 0
    if my > board_data.Ymax:
        return 0, 0
    # mouse x: 250 - 950 (0 - 700)
    tempX = board_data.Xmin
    X = 0
    while tempX < mx:
        tempX = tempX + board_data.fieldX
        X = X + 1

    # mouse y:  70 - 550 (0 - 480)
    tempY = board_data.Ymin
    Y = 0
    while tempY < my:
        tempY = tempY + board_data.fieldY
        Y = Y + 1

    return X, Y
