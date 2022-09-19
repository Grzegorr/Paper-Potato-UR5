import numpy as np
import matplotlib.pyplot as plt

Size_ratio = [0.484482837, 0.562182915, 0.571324101, 0.78157137, 0.86384204, 0.89583619, 0.959824489, 0.626171214, 0.754147813, 0.831847891]
toughness_diff = [118.0851064, 38.29787234, 54.25531915, -2.127659574, 24.46808511, -14.89361702, -26.59574468, 4.255319149, 5.319148936, -8.510638298]
std = [61.11236858, 27.46796699, 20.37078953, 28.43962788, 43.58673919, 15.53822858, 12.70671835, 22.11128691, 16.06347752, 20.40779372]


plt.errorbar(Size_ratio, toughness_diff, std, fmt='.k')#, ecolor = "red" , mfc = "red", mec = "red")

plt.xlabel("Size ratio to potatoes used to make the model")
plt.ylabel("Deviation from optimal hardness [%]")
plt.savefig("GTvsRobot.png")
plt.show()