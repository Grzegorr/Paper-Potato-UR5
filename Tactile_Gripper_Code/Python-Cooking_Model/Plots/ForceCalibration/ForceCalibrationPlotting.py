import matplotlib.pyplot as plt

F = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25]
meanSensor = [0, 9, 15, 24, 30, 39, 45, 57, 66, 81, 93, 126, 171, 273]
stdSensor = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6]


plt.errorbar(F, meanSensor, stdSensor, fmt='.k')
plt.xlabel("Applied Force [N]")
plt.ylabel("Sensor Voltage Change [mV]")
plt.savefig("Fcalibaration.png")
plt.show()









