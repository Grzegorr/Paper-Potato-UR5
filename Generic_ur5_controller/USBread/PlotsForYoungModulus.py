import numpy as np
import matplotlib.pyplot as plt

data = np.load("InitialStepStabbing/0/raw_potato.npy", allow_pickle=True)

plt.plot(data[0:2500, 2])
plt.ylabel("Fz")
plt.xlabel("data_point")
plt.show()



data = np.load("InitialStepStabbing/30/thity_min_potato.npy", allow_pickle=True)

plt.plot(data[2500:5000, 2])
plt.ylabel("Fz")
plt.xlabel("data_point")
plt.show()

data = np.load("InitialStepStabbing/20/twenty_min_potato.npy", allow_pickle=True)

plt.plot(data[2500:5000, 2])
plt.ylabel("Fz")
plt.xlabel("data_point")
plt.show()

data = np.load("InitialStepStabbing/10/ten_min_potato.npy", allow_pickle=True)

plt.plot(data[12000:13999, 2])
plt.ylabel("Fz")
plt.xlabel("data_point")
plt.show()

