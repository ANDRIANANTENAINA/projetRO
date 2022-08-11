import numpy as np
from Algo import balasHammer as bh
from Algo import minLi as ml
from Algo import stepStone as ss

if __name__ == '__main__':
    cout = np.array(([24, 22, 61, 49, 83, 35],
                     [23, 39, 78, 28, 65, 42],
                     [67, 56, 92, 24, 53, 54],
                     [71, 43, 91, 67, 40, 49]), int)
    print("Balas Hammer :")
    s1 = bh.fonctMain(cout)

    print("\nStepping Stone :")
    vx, vy, cxy = ss.VxCxyVy(s1, cout)
    print("Vx: ", vx)
    print("Vy: ", vy)
    print("Cxy: ", cxy)
    ss.steppingStone(s1, ss.gainsObtenue(s1, cout))
    ss.steppingMarquage(s1, ss.gainsObtenue(s1, cout))

