import pygame
import params


def getGridCoords(mx, my):

    if mx < params.Xmin:
        return 0, 0
    if mx > params.Xmax:
        return 0, 0
    if my < params.Ymin:
        return 0, 0
    if my > params.Ymax:
        return 0, 0
    # mouse x: 250 - 950 (0 - 700)
    tempX = params.Xmin
    X = 0
    while tempX < mx:
        tempX = tempX + params.fieldX
        X = X + 1

    # mouse y:  70 - 550 (0 - 480)
    tempY = params.Ymin
    Y = 0
    while tempY < my:
        tempY = tempY + params.fieldY
        Y = Y + 1

    return X, Y
