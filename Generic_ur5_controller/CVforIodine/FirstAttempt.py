import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogramPlotting(VariableToPlot):
    n, bins, patches = plt.hist(x=VariableToPlot, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.show()

def imageAnalysys(file_name):
    print()
    print()

    print("File name: " + str(file_name))
    img = cv2.imread(file_name,1)
    cv2.imshow("The input",img)
    #print(img.shape)
    #cv2.waitKey(0)

    R = []
    G = []
    B = []
    sumR = 0
    sumG = 0
    sumB = 0

    for row in img:
        for pixel in row:
            sumR = sumR + pixel[2]
            sumG = sumG + pixel[1]
            sumB = sumB + pixel[0]
            R.append(pixel[2])
            G.append(pixel[1])
            B.append(pixel[0])

    avgR = sumR/img.shape[0]/img.shape[1]
    avgG = sumG/img.shape[0]/img.shape[1]
    avgB = sumB/img.shape[0]/img.shape[1]

    print("AvgR: " + str(avgR))
    print("AvgG: " + str(avgG))
    print("AvgB: " + str(avgB))
    print()


    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    H = []
    S = []
    V = []
    sumH = 0
    sumS = 0
    sumV = 0

    for row in img:
        for pixel in row:
            sumV = sumV + pixel[2]
            sumS = sumS + pixel[1]
            sumH = sumH + pixel[0]
            V.append(pixel[2])
            S.append(pixel[1])
            H.append(pixel[0])

    avgH = sumH/img.shape[0]/img.shape[1]
    avgS = sumS/img.shape[0]/img.shape[1]
    avgV = sumV/img.shape[0]/img.shape[1]

    print("AvgH: " + str(avgH))
    print("AvgS: " + str(avgS))
    print("AvgV: " + str(avgV))

    #histogramPlotting(R)




imageAnalysys("raw.png")
imageAnalysys("middle.png")
imageAnalysys("cooked.png")

imageAnalysys("raw2.png")
imageAnalysys("middle2.png")
imageAnalysys("cooked2.png")