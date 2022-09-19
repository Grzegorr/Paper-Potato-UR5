import numpy as np
import matplotlib.pyplot as plt


times = ["0", "10", "20", "30", "40", "50", "60"]
test_numbers = ["1", "2", "3", "4", "5"]
start_entries = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(test_numbers)):
    data = np.load("60/Test" + str(test_numbers[i]) + "/FvsEnc.npy")
    A_count = data[0]
    F = data[1]
    A_count_plot = A_count.copy()
    ###Get the encoder value subtracted\
    for j in range(len(A_count)):
        bias = A_count[start_entries[i]]
        #print(bias)
        A_count_plot[j] = A_count[j] - bias
    plt.plot(A_count_plot[start_entries[i]:], F[start_entries[i]:], label = "Test = " + str(test_numbers[i]))
    #plt.show()

plt.xlabel("Encoder Value")
plt.ylabel("Sensor Reading")
plt.legend()
plt.show()