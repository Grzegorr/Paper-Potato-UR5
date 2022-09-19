import numpy as np
import matplotlib.pyplot as plt


times = ["0", "10", "20", "30", "40", "50", "60"]
test_numbers = ["1", "2", "3", "4", "5"]
start_entries = [7, 9, 4, 5, 0, 5, 12]

for i in range(len(times)):
    data = np.load(str(times[i]) + "/Test1/FvsEnc.npy")
    A_count = data[0]
    F = data[1]
    A_count_plot = A_count.copy()
    F_bias = F[start_entries[i]].copy()
    ###Get the encoder value subtracted\
    for j in range(len(A_count)):
        bias = A_count[start_entries[i]]
        #print(bias)
        F[j] = F[j] - F_bias
        A_count_plot[j] = A_count[j] - bias
    plt.plot(A_count_plot[start_entries[i]:], F[start_entries[i]:], label = "T = " + str(times[i]))
    #plt.show()

plt.xlabel("Encoder Value")
plt.ylabel("Sensor Reading")
plt.legend()
plt.show()

