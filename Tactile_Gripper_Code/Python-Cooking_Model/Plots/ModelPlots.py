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


#use raw potato data only for this
def findConstant(k, Rt):
    print(k * Rt / 22)
    return k * Rt / 22

def matchLine(constant, Rt, k1, k2, t1, t2):
    Rr1 = (Rt-(constant/k1))/(21./22.)
    Rr2 = (Rt - (constant / k2)) / (21./22.)

    ratio1 = Rr1/Rt
    ratio2 = Rr2/Rt
    #print(ratio1)
    #print(ratio2)

    #print((3.14*ratio1)/np.sin(3.14*ratio1))
    #print((3.14 * ratio2) / np.sin(3.14 * ratio2))
    LHS1 = np.log((3.14*ratio1)/np.sin(3.14*ratio1))
    LHS2 = np.log((3.14 * ratio2) / np.sin(3.14 * ratio2))

    ##point of the curve are (t1, LHS1)(t2, LHS2)
    deltaY = LHS2-LHS1
    deltaX = t2-t1

    A = deltaY/deltaX
    B = LHS1 - A * t1

    return A, B

def matchModel(kraw, Rt, k1, k2, t1, t2):
    const = findConstant(kraw, Rt)
    A, B = matchLine(const, Rt, k1, k2, t1, t2)
    print("A: " + str(A))
    print("B: " + str(B))
    return A,B


#To draw lines which symbolize cookedness ratio
x_lines = [0, 35]
y_lines = [[0 ,0],[0.28, 0.28], [0.68, 0.68], [1, 1], [1.45, 1.45], [2.21, 2.21], [2.94, 2.94], [7.5866,7.5866]]
for i in range(len(y_lines)):
    if i == 0:
        plt.plot(x_lines, y_lines[i], color='black', linestyle="dashed", label = "$\mathregular{R_{raw}:R_t}$ ratio, right side scale")
    else:
        plt.plot(x_lines,y_lines[i],color='black', linestyle = "dashed")

#Ideal potato plot
x_potato = [0,10,20,30,35]
y_potato = [10, 2, -6, -6, -6]
plt.plot(x_potato,y_potato,color='black', marker = 's', label = "Ideal world example")

#Twice as big potato
x_potato = [0,10,20,30,35]
y_potato = [10, 8, 6, 4, 3]
plt.plot(x_potato,y_potato,color='brown', marker = 's', label = "Ideal world example - double radius")

A,B = matchModel(2.66, 30, 0.25, 0.95, 20., 10.)
#Matching to Slow stabbing data
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='green', marker = 's', label = "potato model - initial data")

A,B = matchModel(2.66, 30, 0.9*0.25, 1.1*0.95, 20., 10.)
#Matching to Slow stabbing data + error
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='yellow', marker = 's', label = "10% error, opposite directions")

A,B = matchModel(2.66, 30, 1.1*0.25, 0.9*0.95, 20., 10.)
#Matching to Slow stabbing data + error
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='yellow', marker = 's')

A,B = matchModel(2.66, 30, 0.9*0.25, 0.9*0.95, 20., 10.)
#Matching to Slow stabbing data + error
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='orange', marker = 's', label = "10% error, same direction")

A,B = matchModel(2.66, 30, 1.1*0.25, 1.1*0.95, 20., 10.)
#Matching to Slow stabbing data + error
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='orange', marker = 's')

A,B = matchModel(2.66, 30, 1.2*0.25, 0.8*0.95, 20., 10.)
#Matching to Slow stabbing data + error
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='red', marker = 's', label = "20% error, opposite directions")

A,B = matchModel(2.66, 30, 0.8*0.25, 1.2*0.95, 20., 10.)
#Matching to Slow stabbing data + error
x_potato = [0,10,20,30,40]
y_potato = [B, B+10*A, B+20*A, B+30*A, B+40*A]
plt.plot(x_potato,y_potato,color='red', marker = 's')



#plt.title("Dependance of required stabbing force on cooking time")
plt.ylabel("LHS of the thermal model equation")
plt.xlabel("Cooking time [minutes]")

plt.legend(loc='upper right')

#plt.show()
plt.savefig("CookingTime.png")
plt.clf()