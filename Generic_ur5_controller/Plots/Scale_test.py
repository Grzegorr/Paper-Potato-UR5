import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FixedLocator

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0.001) & (y < 0.999)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
fig, axs = plt.subplots()



# Function x**(1/2)
def forward(x):
    return np.log(3.14*x/np.sin(3.14*x))

def inverse(x):
    return x


ax = axs
ax.plot(x, y)
ax.set_yscale('function', functions=(forward, inverse))
ax.set_title('function: $x^{1/2}$')
ax.grid(True)
ax.yaxis.set_major_locator(FixedLocator(np.arange(0, 1, 0.2)**2))
ax.yaxis.set_major_locator(FixedLocator(np.arange(0, 1, 0.2)))


plt.show()