import serial
import numpy as np
import matplotlib.pyplot as plt
arduino = serial.Serial('COM3', 115200)

A_count = []
Sensor_value = []
i = 0

while True:
    data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
    data = data.decode('UTF-8')
    if (data[0:9] == "A_count: ") and abs(int(float(data[9:]))) < 300:
        print("Break")
        break


while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        data = data.decode('UTF-8')
        #print(data)

        if (data[0:14] == "Sensor Value: "):
            # print(data[3:])
            data_int = float(data[14:])
            #print(data_int)
            Sensor_value.append(data_int)
            i = i + 1
            #print(i)

        if (data[0:9] == "A_count: "):
            print(data[9:])
            data_int = int(float(data[9:]))
            A_count.append(abs(data_int))
            i = i + 1

    if i == 200:
        plt.plot(A_count, Sensor_value)
        plt.xlabel("Encoder Value")
        plt.ylabel("Sensor Reading")
        plt.savefig("FvsEnc.png")
        plt.show()
        dataToSave = [A_count, Sensor_value]
        np.save("FvsEnc.npy", dataToSave, allow_pickle = True)
        exit()