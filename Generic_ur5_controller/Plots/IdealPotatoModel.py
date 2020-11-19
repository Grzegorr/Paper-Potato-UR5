import numpy as np
import matplotlib.pyplot as plt
from pynverse import inversefunc

plt.ylim(0, 10)
plt.xlim(0, 35)
plt.text(35.5, 7.55, "1")
plt.text(35.5, 2.96, "0.95")
plt.text(35.5, 2.25, "0.9")
plt.text(35.5, 1.5, "0.8")
plt.text(35.5, 1.15, "0.7")
plt.text(35.5, 0.7, "0.6")
plt.text(35.5, 0.3, "0.4")
plt.text(35.5, 0, "0")


#To draw lines which symbolize cookedness ratio
x_lines = [0, 35]
y_lines = [[0 ,0],[0.28, 0.28], [0.68, 0.68], [1, 1], [1.45, 1.45], [2.21, 2.21], [2.94, 2.94], [7.5866,7.5866]]
for i in range(len(y_lines)):
    plt.plot(x_lines,y_lines[i],color='black')

#Ideal potato plot
x_potato = [0,10,20,30,35]
y_potato = [10, 6, 2, -2, -4]
plt.plot(x_potato,y_potato,color='red', marker = 's')

#Twice as big potato
x_potato = [0,10,20,30,35]
y_potato = [10, 8, 6, 4, 3]
plt.plot(x_potato,y_potato,color='red', marker = 's')


#plt.title("Dependance of required stabbing force on cooking time")
plt.ylabel("LHS of the thermal model equation")
plt.xlabel("Cooking time [minutes]")


#plt.show()
plt.savefig("CookingTime.png")
plt.clf()