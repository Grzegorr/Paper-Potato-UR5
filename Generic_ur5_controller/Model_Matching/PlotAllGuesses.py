import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x_regression_small = []
y_regression_small = []
x_regression_large = []
y_regression_large = []


Rt_small = 30
Rt_large = 50


#small potato measurements
measured_k_raw = [2.22, 2.866, 3.428]
measured_k_10 = [1.095238095, 1.19047619, 0.952380952]
measured_k_15 = [0.444444444, 0.833333333, 1]
measured_k_20 = [0.633333333, 0.6525641026, 0.552380952]
measured_k_25 = [0.154, 0.1666, 0.205]
measured_k_cooked = [0.15, 0.1333]

avg_K_raw = sum(measured_k_raw)/len(measured_k_raw)
avg_K_cooked = sum(measured_k_cooked)/len(measured_k_cooked)
max_K_raw = np.max(np.array(measured_k_raw))
min_K_cooked = np.min(np.array(measured_k_cooked))

measured_k_raw_large = [2.60, 2.22, 2.14]
measured_k_10_large = [1.481481481, 1.388888889, 0.909090909]
measured_k_15_large = [0.769230769, 0.833333333, 0.952380952, 0.740740741]
measured_k_20_large = [0.666666667, 0.909090909, 0.848484848, 0.769230769]
measured_k_25_large = [0.740740741, 0.666666667, 0.555555556, 0.4]
measured_k_30_large = [0.476190476, 0.523809524, 0.595238095, 0.380952381]
measured_k_35_large = [0.333333333, 0.296296296, 0.242424242, 0.222222222]
measured_k_cooked_large = [0.179487179, 0.153846154, 0.164102564, 0.121212121]

avg_K_raw_large = sum(measured_k_raw_large)/len(measured_k_raw_large)
avg_K_cooked_large = sum(measured_k_cooked_large)/len(measured_k_cooked_large)
max_K_raw_large = np.max(np.array(measured_k_raw_large))
min_K_cooked_large = np.min(np.array(measured_k_cooked_large))


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



plt.ylim(-0.3, 8)
plt.xlim(-2, 50)
plt.text(50.5, 7.55, "1")
plt.text(50.5, 2.96, "0.95")
plt.text(50.5, 2.25, "0.9")
plt.text(50.5, 1.5, "0.8")
plt.text(50.5, 1.15, "0.7")
plt.text(50.5, 0.7, "0.6")
plt.text(50.5, 0.3, "0.4")
plt.text(50.5, 0, "0")

#Small potato samples
for i in measured_k_raw:
    placeObservation(max_K_raw, min_K_cooked, Rt_small, i, 0, "ro", 0)

for i in measured_k_10:
    placeObservation(max_K_raw, min_K_cooked, Rt_small, i, 10, "ro", 0)

for i in measured_k_15:
    placeObservation(max_K_raw, min_K_cooked, Rt_small, i, 15, "ro", 0)

for i in measured_k_20:
    placeObservation(max_K_raw, min_K_cooked, Rt_small, i, 20, "ro", 0)

for i in measured_k_25:
    placeObservation(max_K_raw, min_K_cooked, Rt_small, i, 25, "ro", 0)

for i in measured_k_cooked:
    placeObservation(max_K_raw, min_K_cooked, Rt_small, i, 30, "ro", 0)

#Large potato samples
for i in measured_k_raw_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 0, "bo", 1)

for i in measured_k_10_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 10, "bo", 1)

for i in measured_k_15_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 15, "bo", 1)

for i in measured_k_20_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 20, "bo", 1)

for i in measured_k_25_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 25, "bo", 1)

for i in measured_k_30_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 30, "bo", 1)

for i in measured_k_35_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 35, "bo", 1)

for i in measured_k_cooked_large:
    placeObservation(max_K_raw_large, min_K_cooked_large, Rt_large, i, 45, "bo", 1)

##LABELS
plt.plot(-5, -5, "ro", label = "small potatoes")
plt.plot(-5, -5, "bo", label = "large potatoes")

#To draw lines which symbolize cookedness ratio
x_lines = [-5, 55]
y_lines = [[0 ,0],[0.28, 0.28], [0.68, 0.68], [1, 1], [1.45, 1.45], [2.21, 2.21], [2.94, 2.94], [7.5866,7.5866]]
for i in range(len(y_lines)):
    if i == 0:
        plt.plot(x_lines, y_lines[i], color='black', linestyle="dashed", label = "$\mathregular{R_{raw}:R_t}$ ratio, right side scale")
    else:
        plt.plot(x_lines,y_lines[i],color='black', linestyle = "dashed")

#plt.title("Dependance of required stabbing force on cooking time")
plt.ylabel("LHS of the thermal model equation")
plt.xlabel("Cooking time [minutes]")

plt.legend(loc='upper right')

plt.savefig("AllMeasurements.png")
plt.show()


####Regression part
print("")
print("")
print(x_regression_small)
print(y_regression_small)
print(x_regression_large)
print(y_regression_large)

x_regression_small = np.array(x_regression_small).reshape((-1, 1))
y_regression_small = np.array(y_regression_small)
x_regression_large = np.array(x_regression_large).reshape((-1, 1))
y_regression_large = np.array(y_regression_large)

print("")
print("")
print(x_regression_small)
print(y_regression_small)
print(x_regression_large)
print(y_regression_large)

model = LinearRegression()
try:
    model.fit(x_regression_small, y_regression_small)
except:
    model.fit(x_regression_small, y_regression_small)
model2 = LinearRegression()
try:
    model2.fit(x_regression_large, y_regression_large)
except:
    model2.fit(x_regression_large, y_regression_large)

print("Model 1, a, b: " + str(model.intercept_) + ", " + str(model.coef_[0]))
print("Model 2, a, b: " + str(model2.intercept_) + ", " + str(model2.coef_[0]))

a1 = model.coef_[0]
a2 = model2.coef_[0]
b1 = model.intercept_
b2 = model2.intercept_

####Numbers for plotting
x = [-10, 70]
y1 = [b1-10*a1,  b1+70*a1]
y2 = [b2-10*a2,  b2+70*a2]

plt.plot(x, y1, color='red', label = "Small potato model prediction")
plt.plot(x, y2, color='blue', label = "Large potato model prediction")

#Size dependent model
Size_ratio = 1.3
a3 = a1/(Size_ratio**2)
y3 = [b1-10*a3,  b1+70*a3]
plt.plot(x, y3, color='green', label = "1.3 the size of small potato")


plt.ylim(-0.3, 8)
plt.xlim(-2, 50)
plt.text(50.5, 7.55, "1")
plt.text(50.5, 2.96, "0.95")
plt.text(50.5, 2.25, "0.9")
plt.text(50.5, 1.5, "0.8")
plt.text(50.5, 1.15, "0.7")
plt.text(50.5, 0.7, "0.6")
plt.text(50.5, 0.3, "0.4")
plt.text(50.5, 0, "0")

#To draw lines which symbolize cookedness ratio
x_lines = [-5, 55]
y_lines = [[0 ,0],[0.28, 0.28], [0.68, 0.68], [1, 1], [1.45, 1.45], [2.21, 2.21], [2.94, 2.94], [7.5866,7.5866]]
for i in range(len(y_lines)):
    if i == 0:
        plt.plot(x_lines, y_lines[i], color='black', linestyle="dashed", label = "$\mathregular{R_{raw}:R_t}$ ratio, right side scale")
    else:
        plt.plot(x_lines,y_lines[i],color='black', linestyle = "dashed")

plt.ylabel("LHS of the thermal model equation")
plt.xlabel("Cooking time [minutes]")

plt.legend(loc='upper right')

plt.savefig("ModelsSizeDependance.png")
plt.show()