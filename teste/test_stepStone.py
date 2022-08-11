from Algo.stepStone import parcours
from Algo.balasHammer import fonctMain
import numpy as np


def test_parcours():
    cout = np.array(([24, 22, 61, 49, 83, 35],
                     [23, 39, 78, 28, 65, 42],
                     [67, 56, 92, 24, 53, 54],
                     [71, 43, 91, 67, 40, 49]), int)
    sb = fonctMain(cout)
    print(parcours(sb, 1, 5, [2, 5], 1))
