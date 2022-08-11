import numpy as np

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


# recherche une valeur minim dNS UN LISTE CONTENANT NBR ET None
def reachMin(liste):
    i = 0
    val = 0

    while i < len(liste):
        if liste[i] is not None:
            if val == 0:
                val = liste[i]
            elif val != 0 and val > liste[i]:
                val = liste[i]

        i = i + 1

    if np.isnan(val):
        try:
            val = np.nanmin(liste)
        except RuntimeWarning as a:
            print(a)

    return val


# recherche une valeur maxim dNS UN LISTE CONTENANT NBR ET None
def reachMax(liste):
    i = 0
    val = None
    while i < len(liste):
        if liste[i] is not None:
            if val is None:
                val = liste[i]
            elif val < liste[i]:
                val = liste[i]
        i = i + 1
    return val


# pour faire le difference minimale par line
def diffMinLine(cout):
    initx = 0
    nombreColonneCout = len(cout[0])
    nombreLineCout = len(cout)
    y = []
    # print(cout, 'cccc')
    while initx < nombreLineCout:
        cout2List = []
        i = 0
        while i < nombreColonneCout:
            cout2List.append(cout[initx][i])
            i = i + 1
        minL1 = reachMin(cout[initx])
        nbrMinL1 = cout2List.count(minL1)
        if nbrMinL1 == 1:
            cout2List.remove(minL1)
            minL2 = reachMin(cout2List)
            if np.isnan(minL2):
                diff = minL1
            else:
                diff = minL2 - minL1
            # print(minL1, 'minL1', minL2, 'minL2')
        else:
            diff = 0
        y.append(diff)
        initx = initx + 1
    # print(y, 'yyyy')
    return y


# minimum pour CHAQUE COLONNE
def diffMinColonne(cout):
    initx = 0
    nombreColonneCout = len(cout[0])
    nombreLineCout = len(cout)
    x = []
    while initx < nombreColonneCout:
        inity = 0
        z = []
        while inity < nombreLineCout:
            z.append(cout[inity][initx])
            inity = inity + 1

        min1 = reachMin(z)
        nombreMin1 = z.count(min1)
        if nombreMin1 == 1:
            z.remove(min1)
            min2 = reachMin(z)
            if np.isnan(min2):
                diff = min1
            else:
                diff = min2 - min1
        else:
            diff = 0
        x.append(diff)
        initx = initx + 1
    return x


def index(tab):
    qteDemande = diffMinColonne(tab)
    qteDisponible = diffMinLine(tab)
    maxY = reachMax(qteDisponible)
    maxX = reachMax(qteDemande)
    if maxX > maxY:
        indexX = qteDemande.index(maxX)
        tmpY = []
        i = 0
        m = len(tab)
        while i < m:
            tmpY.append(tab[i][indexX])
            i = i + 1
        indexY = tmpY.index(reachMin(tmpY))
        val = tab[indexY][indexX]

    else:

        indexY = qteDisponible.index(maxY)
        linPrienCharge = tab[indexY]
        tmpX = []
        i = 0
        while i < len(tab[0]):
            tmpX.append(tab[indexY][i])
            i += 1
        # print(linPrienCharge, 'linPrienCharge')
        indexX = tmpX.index(reachMin(linPrienCharge))
        val = tab[indexY][indexX]

    return indexX, indexY


def funcBase(baseSolution, cout, Vx, Vy):
    k = 0
    while k < len(baseSolution):
        j = 0

        while j < len(baseSolution[0]):
            if baseSolution[k][j] == 0:
                indiceCol = index(cout)[0]
                indiceLine = index(cout)[1]
                # print(indiceCol, 'indicecol'.upper(), indiceLine, 'indiceLine'.upper())

                minVxVy = min(Vx.item(indiceLine), Vy.item(indiceCol))

                a = Vx[0][indiceLine] - minVxVy
                b = Vy[0][indiceCol] - minVxVy
                Vy = np.array(Vy, dtype=np.float64)
                Vx = np.array(Vx, dtype=np.float64)
                baseSolution = np.array(baseSolution, dtype=np.float64)
                cout = np.array(cout, dtype=np.float64)
                if a == 0:
                    Vx[0][indiceLine] = None
                    Vy[0][indiceCol] = b
                    i = 0
                    while i < len(cout[0]):
                        cout[indiceLine][i] = None
                        if baseSolution[indiceLine][i] == 0:
                            baseSolution[indiceLine][i] = None
                        i += 1

                if b == 0:
                    Vy[0][indiceCol] = None
                    Vx[0][indiceLine] = a
                    i = 0
                    while i < len(cout):
                        cout[i][indiceCol] = None
                        if baseSolution[i][indiceCol] == 0:
                            baseSolution[i][indiceCol] = None

                        i += 1
                baseSolution[indiceLine][indiceCol] = minVxVy
            j += 1

            # print(cout, 'cout')
            # print(baseSolution, 'baseSolution')
        k += 1
    return baseSolution, cout, Vx, Vy


def steppingStone(matriceInit, resBase, z):
    m = 0
    vectTmp = []
    indiceMax = 0
    line = 0
    # fill the V(x,y) with vx = None et vy = None par default
    while line < len(matriceInit):
        col = 0
        dictTmp = {str(line): None}
        while col < len(matriceInit[0]):
            if resBase[line][col] != 0:
                if matriceInit[line][col] > m:
                    indiceMax = line
                    m = matriceInit[line][col]
                dictTmp['0' + str(col)] = [matriceInit[line][col], None]
            col += 1
        vectTmp.append(dictTmp)
        line += 1
    # fill the first arc
    vectTmp[indiceMax][str(indiceMax)] = 0

    # vectTmp[indiceMax]['0' + str(indiceMax)][1] = vectTmp[indiceMax][str(indiceMax)] \
    #                                               + vectTmp[indiceMax]['0' + str(indiceMax)][0]

    print(vectTmp)


def fonctMain(cout):
    # tmpCout = copy de cout
    tmpCout = cout.copy()
    # Vx = quantite disponible dans le depot
    Vx = np.array([[18, 32, 14, 9]], int)
    #  Vy = quantite demande
    Vy = np.array([[9, 11, 28, 6, 14, 5]], int)
    # baseSolution = copy de cout mais le valeur sont zeros
    baseSolution = np.zeros(cout.shape)
    resBase = funcBase(baseSolution, cout, Vx, Vy)
    baseSolution = resBase[0]
    newCout = resBase[1]
    newVx = resBase[2]
    newVy = resBase[3]
    j = 0
    while j < len(baseSolution):
        i = 0
        while i < len(baseSolution[0]):
            if baseSolution[j][i] == 0:
                var = funcBase(baseSolution, newCout, newVx, newVy)
                baseSolution = funcBase(baseSolution, newCout, newVx, newVy)[0]
                newCout = var[1]
                newVx = var[2]
                newVy = var[3]
                pass
            else:
                i += 1
        j += 1

    j = 0
    while j < len(baseSolution):
        i = 0
        while i < len(baseSolution[0]):
            if np.isnan(baseSolution[j][i]):
                baseSolution[j][i] = 0
            i += 1
        j += 1
    # print(baseSolution, Vx, Vy)

    print("Solution de base:\n", baseSolution)
    z = int((tmpCout * baseSolution).sum())
    print("Cout de base:", z)

    return baseSolution
