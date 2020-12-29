import matplotlib.pyplot as plt

GT = [206.612, 207.24, 208.496, 158.884, 135.02, 109.9, 99.224]
measured_mean = [205.5426667, 203.8533333, 202.5, 153.647, 132.7963333, 108.3336667, 104.3833333]
standard_deviation = [2.07751069, 0.618899238, 2.552595855, 1.094572611, 1.891345941, 2.682034874, 3.212585667]
error_mean = [-1.069333333, -3.386666667, -5.996, -5.237, -2.223666667, -1.56633, 5.159333333]


plt.errorbar(GT, measured_mean, standard_deviation, fmt='.k')
plt.xlabel("Ground truth circumference [mm]")
plt.ylabel("Measured circumference [mm]")
plt.savefig("Circumference.png")
plt.show()

plt.errorbar(GT, error_mean, standard_deviation, fmt='.k')
plt.xlabel("Ground truth circumference [mm]")
plt.ylabel("Measured error [mm]")
plt.savefig("CircumferenceError.png")
plt.show()








