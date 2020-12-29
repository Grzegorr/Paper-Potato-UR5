import numpy as np
import matplotlib.pyplot as plt

times = ["0", "10", "20", "30", "40", "50", "60"]
test_numbers = ["1", "2", "3", "4", "5"]
start_index = [
    [11, 8, 4, 8, 6],
    [18, 10, 8, 13, 13],
    [13, 11, 10, 15, 11],
    [10, 15, 14, 10, 10],
    [15, 0, 10, 13, 5],
    [10, 25, 20, 10, 10],
    [17, 16, 11, 6, 13]
]
end_index = [
    [40, 20, 60, 12, 20],
    [30,16,30,25,25],
    [30,33,25,28,33],
    [30,45,33,25,33],
    [80,7,20,25,20],
    [33,50,33,33,33],
    [80, 50, 30, 40, 30],
]

k = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


for i in range(len(times)):
    for j in range(len(test_numbers)):
#for i in [5]:
#    for j in [2]:
        data = np.load(str(times[i]) + "/Test" + str(test_numbers[j]) + "/FvsEnc.npy")
        A_count = data[0]
        F = data[1]
        plt.plot(A_count, F, color='green', linestyle='dashed')
        plt.plot(A_count[start_index[i][j]:end_index[i][j]], F[start_index[i][j]:end_index[i][j]], color='red')
        plt.xlabel("Encoder Value")
        plt.ylabel("Sensor Reading")
        #plt.show()
        plt.savefig("dumpOfplots/K/" + str(i) + str(j))

        this_k = (F[end_index[i][j]]-F[start_index[i][j]])/(A_count[end_index[i][j]]-A_count[start_index[i][j]])
        k[i][j] = this_k

print(k)