import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x_regression_large = []
y_regression_large = []
Rt = 50


K = [
    [0.09846808510638304, 0.13983122362869195, 0.06860869565217396, 0.09040201005025131, 0.12063063063063076],
    [0.08236453201970442, 0.09053435114503816, 0.10644736842105268, 0.0585781990521327, 0.059096385542168686],
    [0.044583333333333273, 0.04601941747572817, 0.047081081081081125, 0.04650717703349275, 0.05119658119658128],
    [0.01634868421052631, 0.018059701492537328, 0.024130434782608682, 0.015095057034220528, 0.016384976525821604],
    [0.015107913669064707, 0.027490774907749087, 0.04233766233766234, 0.03673151750972762, 0.038571428571428534],
    [0.015163727959697722, 0.02099999999999999, 0.024270833333333314, 0.016273291925465838, 0.011719745222929958],
    [0.008311036789297658, 0.011020881670533642, 0.014306358381502899, 0.00969365426695844, 0.010144092219020162]
]

maxKraw = np.max(np.array(K[0]))
minKcooked = np.mean(np.array(K[6]))




def findConstant(k_raw, k_cooked, Rt):
    YoungModuleRatio = k_raw/k_cooked
    constant = k_raw * Rt / YoungModuleRatio
    return constant

#regression 0 = add to small potato regression
#regression 1 = add to large potato data
def placeObservation(k_raw, k_cooked, Rt, k_to_place, time_to_place, arg, regression):
    constant = findConstant(k_raw, k_cooked, Rt)
    YoungModuleRatio = k_raw / k_cooked

    #Raw radius
#    print(k_raw)
#    print(k_cooked)
#    print(YoungModuleRatio)
#    print(((YoungModuleRatio - 1.)/YoungModuleRatio))
    Rr1 = (Rt-(constant/k_to_place))/((YoungModuleRatio - 1.)/YoungModuleRatio)

    #ration of raw to total radius
    ratio1 = Rr1/Rt
    #print(ratio1)
    if ratio1 >= 1:
        ratio1 = 0.99
    if ratio1 <=0:
        ratio1 = 0.0000001
    #print((3.14*ratio1)/np.sin(3.14*ratio1))
    LHS1 = np.log((3.14*ratio1)/np.sin(3.14*ratio1))
    plt.plot(time_to_place, LHS1, arg)

    if regression == 0:
        x_regression_small.append(float(time_to_place))
        y_regression_small.append(LHS1)
        #print(x_regression_small)

    if regression == 1:
        x_regression_large.append(float(time_to_place))
        y_regression_large.append(LHS1)




for i in range(7):
    for j in range(5):
        plt.plot(10*i, K[i][j], "bo")


plt.title("K (it is not afrwe modelling, not expected to be linear")
plt.xlabel("Cooking time[min]")
plt.ylabel("K[sensor_val/Enc_val]")
plt.savefig("ModelPlots/K")
plt.show()
plt.clf()



for i in range(7):
    for j in range(5):
        placeObservation(maxKraw, minKcooked, Rt, K[i][j], 10 * i, "bo", 1)

plt.ylim(-0.3, 8)
plt.xlim(-2, 65)
plt.text(65.5, 7.55, "1")
plt.text(65.5, 2.96, "0.95")
plt.text(65.5, 2.25, "0.9")
plt.text(65.5, 1.5, "0.8")
plt.text(65.5, 1.15, "0.7")
plt.text(65.5, 0.7, "0.6")
plt.text(65.5, 0.3, "0.4")
plt.text(65.5, 0, "0")

#To draw lines which symbolize cookedness ratio
x_lines = [-5, 70]
y_lines = [[0 ,0],[0.28, 0.28], [0.68, 0.68], [1, 1], [1.45, 1.45], [2.21, 2.21], [2.94, 2.94], [7.5866,7.5866]]
for i in range(len(y_lines)):
    if i == 0:
        plt.plot(x_lines, y_lines[i], color='black', linestyle="dashed", label = "$\mathregular{R_{raw}:R_t}$ ratio, right side scale")
    else:
        plt.plot(x_lines,y_lines[i],color='black', linestyle = "dashed")

plt.ylabel("LHS of the thermal model equation")
plt.xlabel("Cooking time [minutes]")

plt.legend(loc='upper right')

plt.savefig("ModelPlots/RcookedRatio")
plt.show()
plt.clf()





####Regression part
print("")
print("")
print(x_regression_large)
print(y_regression_large)

x_regression_large = np.array(x_regression_large).reshape((-1, 1))
y_regression_large = np.array(y_regression_large)

print("")
print("")
print(x_regression_large)
print(y_regression_large)

model2 = LinearRegression()
try:
    model2.fit(x_regression_large, y_regression_large)
except:
    model2.fit(x_regression_large, y_regression_large)

print("Model 2, a, b: " + str(model2.intercept_) + ", " + str(model2.coef_[0]))

a2 = model2.coef_[0]
b2 = model2.intercept_

print()
print()
print(a2)
print(b2)

####Numbers for plotting
x = [-10, 70]
y2 = [b2-10*a2,  b2+70*a2]

plt.plot(x, y2, color='blue', label = "Large potato model prediction")

####Numbers for plotting
a2_1 = a2/(0.9**2)
x = [-10, 70]
y2 = [b2-10*a2_1,  b2+70*a2_1]

plt.plot(x, y2, color='red', label = "0.9 of large potato's size")

####Numbers for plotting
a2_1 = a2/(0.8**2)
x = [-10, 70]
y2 = [b2-10*a2_1,  b2+70*a2_1]

plt.plot(x, y2, color='orange', label = "0.8 of large potato's size")

####Numbers for plotting
a2_1 = a2/(0.7**2)
x = [-10, 70]
y2 = [b2-10*a2_1,  b2+70*a2_1]

plt.plot(x, y2, color='yellow', label = "0.7 of large potato's size")

####Numbers for plotting
a2_1 = a2/(0.6**2)
x = [-10, 70]
y2 = [b2-10*a2_1,  b2+70*a2_1]

plt.plot(x, y2, color='green', label = "0.6 of large potato's size")

plt.ylim(-0.3, 8)
plt.xlim(-2, 65)
plt.text(65.5, 7.55, "1")
plt.text(65.5, 2.96, "0.95")
plt.text(65.5, 2.25, "0.9")
plt.text(65.5, 1.5, "0.8")
plt.text(65.5, 1.15, "0.7")
plt.text(65.5, 0.7, "0.6")
plt.text(65.5, 0.3, "0.4")
plt.text(65.5, 0, "0")

#To draw lines which symbolize cookedness ratio
x_lines = [-5, 65]
y_lines = [[0 ,0],[0.28, 0.28], [0.68, 0.68], [1, 1], [1.45, 1.45], [2.21, 2.21], [2.94, 2.94], [7.5866,7.5866]]
for i in range(len(y_lines)):
    if i == 0:
        plt.plot(x_lines, y_lines[i], color='black', linestyle="dashed", label = "$\mathregular{R_{raw}:R_t}$ ratio, right side scale")
    else:
        plt.plot(x_lines,y_lines[i],color='black', linestyle = "dashed")

plt.ylabel("LHS of the thermal model equation")
plt.xlabel("Cooking time [minutes]")

plt.legend(loc='upper right')

plt.savefig("ModelPlots/ModelMatch")
plt.show()


















































