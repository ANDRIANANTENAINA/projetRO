import numpy as np


#
# cout = np.array(([24, 22, 61, 49, 83, 35],
#                  [23, 39, 78, 28, 65, 42],
#                  [67, 56, 92, 24, 53, 54],
#                  [71, 43, 91, 67, 40, 49]), dtype=np.float64)
#
# solutionBase = np.array(([0, 11, 2, 0, 0, 5],
#                          [9, 0, 23, 0, 0, 0],
#                          [0, 0, 3, 6, 5, 0],
#                          [0, 0, 0, 0, 9, 0]), dtype=np.float64)
# # print('cout=', cout)
# # print('**********x***********')
# # print('solutionBase=')
# # print(solutionBase)
# cxy = np.zeros(cout.shape)
# i = 0
# while i < len(cout):
#     j = 0
#     while j < len(cout[0]):
#         if solutionBase[i][j] != 0:
#             # print("(", i, ',', j, ')')
#             # print(solutionBase[i][j])
#             cxy[i][j] = cout[i][j]
#
#         j += 1
#     i += 1
#
#     # Vy?
#     # Vx?


# print(cxy)
def verifyNone(tab):
    i = 0
    for x in tab:
        for t in x:
            if t == None:
                i = None
    if i == None:
        return 0
    else:
        return 1


def step(cxy):
    tmp = []

    for x in cxy:
        a = list(x)
        a.insert(0, None)
        tmp.append(a)

    nbrcol = len(cxy[0])
    i = 0
    firstlin = []

    while i < nbrcol:
        firstlin.append(None)
        i += 1
    tmp.insert(0, firstlin)

    i = 0
    maxim = max(cxy[0])
    while i < len(cxy):
        j = 0
        while j < len(cxy[i]):
            if max(cxy[i]) > maxim:
                maxim = (max(cxy[i]))
                lin = i
                col = cxy[lin].tolist().index(max(cxy[lin]))
            j += 1
        i += 1
    lin += 1
    tmp[lin][0] = 0

    return lin, col, tmp


def VxCxyVy(solutionBase, cout):
    cxy = np.zeros(cout.shape)
    i = 0
    while i < len(cout):
        j = 0
        while j < len(cout[0]):
            if solutionBase[i][j] != 0:
                # print("(", i, ',', j, ')')
                # print(solutionBase[i][j])
                cxy[i][j] = cout[i][j]

            j += 1
        i += 1
    tmp = step(cxy)[2]
    nbrColon = len(tmp[1])
    nbrLine = len(tmp)
    i = 0
    while i < len(tmp[0]):
        if tmp[0][i] is None:
            a = 0
            while a < nbrLine:
                if tmp[a][0] is not None:
                    y = 1
                    while y < nbrColon:
                        if tmp[a][y] is not None and tmp[a][y] != 0 and tmp[0][y - 1] is None:
                            tmp[0][y - 1] = tmp[a][0] + tmp[a][y]
                        y += 1

                a += 1
            k = 0
            while k < len(tmp[0]):
                if tmp[0][k] is not None:
                    l = 1
                    while l < nbrLine:
                        if tmp[l][0] is None and tmp[l][k + 1] != 0:
                            tmp[l][0] = tmp[0][k] - tmp[l][k + 1]
                        l += 1
                k += 1
        point = verifyNone(tmp)
        if point == 1:
            break
    i += 1
    Vy = tmp[0]
    Vx = []
    for x in tmp:
        if x != tmp[0]:
            Vx.append(x[0])
    return Vx, Vy, cxy


def gainsObtenue(solutionBase, cout):
    Vx = VxCxyVy(solutionBase, cout)[0]
    Vy = VxCxyVy(solutionBase, cout)[1]
    coutMarginaux = list(np.zeros(cout.shape))
    i = 0
    while i < len(cout):
        coutMarginaux[i] = list(coutMarginaux[i])
        j = 0
        while j < len(cout[0]):
            if solutionBase[i][j] == 0:
                coutMarginaux[i][j] = cout[i][j]

            j += 1
        i += 1
    for x in coutMarginaux:
        line = coutMarginaux.index(x)
        for val in x:
            if val != 0:
                col = x.index(val)
                coutMarginaux[line][col] = Vx[line] + val - Vy[col]

    print('cout Marginaux = ')
    for x in coutMarginaux:
        print(x)

    i = 0
    for line in coutMarginaux:
        j = 0
        for coutMargin in line:
            if coutMargin < 0:
                print()
                # while..

            j += 1
        i += 1
    return coutMarginaux


def tCol(liste, ignorer, line, col):
    i = 0
    while i < len(liste):
        if i != line:
            for nbr in ignorer:
                if i != nbr:
                    if liste[i][col] != 0:
                        return i

        i += 1


def tLine(liste, ignorer, line, col):
    i = 0
    while i < len(liste[line]):
        for nbr in ignorer:
            if i != nbr:
                if liste[line][i] != 0:
                    return i
        i += 1


def steppingStone(solutionBase, coutMarginaux):
    # coordonnes an'ireo coutmarginaux negatif
    coordonnes = []
    coordonne = []

    # comptery = ijerena y cout marginaux negatif
    comptery = 0

    for i in coutMarginaux:
        # compterx = ijerena x cout marginaux negatif
        compterx = 0

        for z in i:
            if z < 0:
                coordonne = [comptery, compterx]
                coordonnes += [coordonne]
            compterx += 1
        comptery += 1

    y = 0
    for i in coordonnes:
        longeurSBase = len(solutionBase)
        x = i[1]
        y = i[0]
        coordonne_marquage = [i]
        compter = 0
        while compter < longeurSBase:
            val_index = solutionBase[compter][x]
            if val_index != 0:
                coordonne_marquage.append([compter, x])
            compter += 1
        print(coordonne_marquage)


def steppingMarquage(solutionBase, coutMarginaux):
    neg = []
    solutionBase = list(solutionBase)
    coutM = coutMarginaux

    for i in coutM:
        for j in i:
            if j < 0:
                neg.append([coutMarginaux.index(i), i.index(j)])
    print("+++++++", neg)

    # for i in neg:
    #     tmp = []
    #     solutionBase[i[0]][i[1]] = None
    #     while tmp != i:
    #
    #         for col in range(0, i[0]):
    #             if solutionBase[col][i[1]] > 0:
    #                 print(solutionBase[col][i[1]])
    #
    #         for col in range(i[0], len(solutionBase)):
    #             if solutionBase[col][i[1]] > 0:
    #                 print(solutionBase[col][i[1]])


# 1 ligne, 0 colonne
def parcours(solutionBase, line, col, arret, etat):
    if [line, col] == arret:
        return "vita"
    # -
    elif solutionBase[line][col] == 0 and etat == 1:
        print(line, col)
        if line - 1 >= 0:
            return parcours(solutionBase, line - 1, col, arret, 1)

    elif solutionBase[line][col] > 0 and etat == 1:
        print(line, col)
        if col - 1 >= 0:
            return parcours(solutionBase, line, col - 1, arret, 0)
    # +
    elif solutionBase[line][col] == 0 and etat == 1:
        print(line, col)
        if line + 1 < len(solutionBase):
            return parcours(solutionBase, line + 1, col, arret, 1)

    elif solutionBase[line][col] > 0 and etat == 1:
        print(line, col)
        if col + 1 < len(solutionBase[0]):
            return parcours(solutionBase, line, col + 1, arret, 0)

    # -------------------
    # -
    elif solutionBase[line][col] == 0 and etat == 0:
        print(line, col)
        if col - 1 >= 0:
            return parcours(solutionBase, line, col - 1, arret, 0)

    elif solutionBase[line][col] > 0 and etat == 0:
        print(line, col)
        if line - 1 >= 0:
            return parcours(solutionBase, line - 1, col, arret, 1)
        else:
            return parcours(solutionBase, line + 1, col, arret, 1)
    # +
    elif solutionBase[line][col] == 0 and etat == 0:
        print(line, col)
        if col + 1 < len(solutionBase[0]):
            return parcours(solutionBase, line, col + 1, arret, 0)

    elif solutionBase[line][col] > 0 and etat == 0:
        print(line, col)
        if line + 1 < len(solutionBase):
            return parcours(solutionBase, line + 1, col, arret, 1)

    return "tss"

# VxCxyVy(solutionBase)
# step(cxy)
# gainsObtenue()
# steppingStone(solutionBase, gainsObtenue())
# valCoordonne([0,1], solutionBase)
