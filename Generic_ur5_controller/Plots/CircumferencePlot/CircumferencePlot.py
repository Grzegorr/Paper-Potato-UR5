import matplotlib.pyplot as plt



GT = [206.612, 207.24, 208.496, 158.884, 135.02, 109.9, 99.224]
actual = [209.3, 208.8, 205.6, 173.4, 159.65, 143.5, 139.5]
error = [2.688, 1.56, -2.896, 14.516, 24.63, 33.6, 40.276]

plt.scatter(GT, actual)
plt.xlabel("Ground truth circumference.")
plt.ylabel("Measured circumference.")
plt.savefig("Circumference.png")
plt.show()

plt.scatter(GT, error)
plt.xlabel("Ground truth circumference.")
plt.ylabel("Measured error.")
plt.savefig("CircumferenceError.png")
plt.show()
