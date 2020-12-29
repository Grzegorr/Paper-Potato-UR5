import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


times = ["0", "10", "20", "30", "40", "50", "60"]
test_numbers = ["1", "2", "3", "4", "5"]

for i in range(len(times)):
    for j in range(len(test_numbers)):
        data = np.load(str(times[i]) + "/Test" + str(test_numbers[j]) + "/FvsEnc.npy")
        A_count = data[0]
        F = data[1]
        deriv_arr = []

        ###compute derivative
        for l in range(len(F)-1):
            delta_A_count = A_count[l+1] - A_count[l]
            delta_F = F[l+1] - F[l]
            if delta_F == 0:
                deriv = 0
            elif delta_A_count == 0:
                deriv = -1
            else:
                deriv = delta_F/delta_A_count
            deriv_arr.append(deriv)

        plt.clf()
        plt.plot(deriv_arr)
        plt.ylim(-0.001, 1)
        plt.xlabel("Array Index")
        plt.ylabel("K")
        # plt.show()
        plt.savefig("dumpOfplots/" + str(times[i]) + str(test_numbers[j]))






