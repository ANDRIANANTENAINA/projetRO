import time
import numpy as np
import datetime


# min sans le min precedent
def minWithOut(m, indiceC):
    m[indiceC] = max(m) + 100
    return m


# pour isoler tous le valuer de cout deja prise
def maximisation(m, indiceC):
    lin = 0
    while lin < len(m):
        m[lin][indiceC] = max(m[lin]) + 100
        lin = lin + 1
    return m


def fonctMain(cout):
    timeInit = time.time()
    line = 0
    tmpCout = cout.copy()

    Vx = np.array([[18, 32, 14, 9]], int)
    Vy = np.array([[9, 11, 28, 6, 14, 5]], int)

    baseSolution = np.zeros(cout.shape)

    while line < len(cout):
        indiceCol = cout[line].argmin()
        minVxVy = min(Vx.item(line), Vy.item(indiceCol))
        nextL = Vx.item(line) - minVxVy
        Vx.itemset(line, Vx.item(line) - minVxVy)
        Vy.itemset(indiceCol, Vy.item(indiceCol) - minVxVy)
        baseSolution[line][indiceCol] = minVxVy

        if Vy.item(indiceCol) == 0:
            cout = maximisation(cout, indiceCol)

        while not (nextL == 0):
            mI = minWithOut(cout[line], indiceCol).argmin()
            minVxVy = min(Vx.item(line), Vy.item(mI))
            tmp = Vx.item(line) - minVxVy
            Vx.itemset(line, Vx.item(line) - minVxVy)
            Vy.itemset(mI, Vy.item(mI) - minVxVy)
            if Vy.item(mI) == 0:
                cout = maximisation(cout, mI)
            baseSolution[line][mI] = minVxVy

            nextL = tmp

        line += 1

    timeFinal = time.time()

    print("Solution de base:\n", baseSolution)
    z = int((tmpCout * baseSolution).sum())
    print("Cout de base:", z)
    print(float(timeFinal - timeInit), " ms")

    return baseSolution
