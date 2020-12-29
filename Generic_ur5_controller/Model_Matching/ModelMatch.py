import numpy as np
from sklearn.linear_model import LinearRegression


#use raw potato data only for this
def findConstant(k, Rt):
    print(k * Rt / 22)
    return k * Rt / 22

def matchLine(constant, Rt, k1, k2, t1, t2):
    Rr1 = (Rt-(constant/k1))/(21./22.)
    Rr2 = (Rt - (constant / k2)) / (21./22.)

    ratio1 = Rr1/Rt
    ratio2 = Rr2/Rt
    #print(ratio1)
    #print(ratio2)

    #print((3.14*ratio1)/np.sin(3.14*ratio1))
    #print((3.14 * ratio2) / np.sin(3.14 * ratio2))
    LHS1 = np.log((3.14*ratio1)/np.sin(3.14*ratio1))
    LHS2 = np.log((3.14 * ratio2) / np.sin(3.14 * ratio2))

    ##point of the curve are (t1, LHS1)(t2, LHS2)
    deltaY = LHS2-LHS1
    deltaX = t2-t1

    A = deltaY/deltaX
    B = LHS1 - A * t1

    return A, B


def matchModel(kraw, Rt, k1, k2, t1, t2):

    const = findConstant(kraw, Rt)
    A, B = matchLine(const, Rt, k1, k2, t1, t2)

    print("A: " + str(A))
    print("B: " + str(B))

matchModel(2.66, 30, 0.25, 0.95, 20., 10.)
matchModel(2.66, 30, 0.9*0.25, 1.1*0.95, 20., 10.)
matchModel(2.66, 30, 1.1*0.25, 0.9*0.95, 20., 10.)
matchModel(2.66, 30, 1.1*0.25, 1.1*0.95, 20., 10.)
matchModel(2.66, 30, 0.9*0.25, 0.9*0.95, 20., 10.)








