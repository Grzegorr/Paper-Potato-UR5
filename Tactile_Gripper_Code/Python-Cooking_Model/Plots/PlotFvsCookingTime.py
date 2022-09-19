import numpy as np
import matplotlib.pyplot as plt

data_force = [[60, 60 , 70, 60,70,60,60], [5, 5, 7, 8, 10, 45, 45], [3, 3, 2, 2, 1.5, 1, 27],[2, 2, 2, 1.9, 1.8, 1.8, 1.7], [2, 2.1, 2, 2, 1.8, 2, 2]]
data_time = [0, 10, 20, 30, 35]
#data_time = [0, 1, 2,4]
#data_force = [[1,1,1,1],[1,2,3,4],[1,10,10,20],[0,0,0,-50,50]]


x = data_time
y = np.mean(np.array(data_force), axis = 1)
error = np.std(np.array(data_force), axis = 1)

plt.errorbar(x, y, error, marker = 's')
#plt.title("Dependance of required stabbing force on cooking time")
plt.ylabel("$\mathregular{F_z}$ [N]")
plt.xlabel("Cooking time [minutes]")
#plt.show()
plt.savefig("FzCookingTime.png")
plt.clf()