import serial
import numpy as np
arduino = serial.Serial('COM3', 115200)

no_squeezes = 4

force_presqueeze_raw = np.zeros(no_squeezes * 100)
force_presqueeze = np.zeros(no_squeezes)
encoder_position_presqueeze = np.zeros(no_squeezes)
force_squeezed_raw = np.zeros(no_squeezes*100)
force_squeezed = np.zeros(no_squeezes)
encoder_position_squeezed = np.zeros(no_squeezes)
Potato_Encoder = 0;
k_arr = np.zeros(no_squeezes)
i = 0
j = 0
k = 0
l = 0

#Total gear ratio
Enc_gear_ratio = 3 #coz encoder is 12 counts per rotation
Motor_gear_ratio = 298 # datasehet
Radius_cylinder = 8.4
Distance_per_encoder_mm = 2*3.14*Radius_cylinder/Enc_gear_ratio/Motor_gear_ratio



while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        data = data.decode('UTF-8')
        #print(data)
#        if ("END_OF_INITIAL_SQUEZE_POSITION" in data):
#            data_split = data.split()
#            Potato_Encoder = data_split[1]
#            encoder = float(data_split[1])
#            distance_mm = encoder * Distance_per_encoder_mm
#            np.save("distance.npy", distance_mm, allow_pickle=True)
#            print("Distance: " + str(distance_mm))

        if(data[0:3] == "AAA"):
            #print(data[3:])
            data_int = int(data[3:])
            #print(data)
            force_presqueeze_raw[i] = data_int
            i = i + 1

        if (data[0:3] == "BBB"):
            # print(data[3:])
            data_int = int(data[3:])
            #print(data_int)
            encoder_position_presqueeze[j] = data_int
            j = j + 1

        if (data[0:3] == "CCC"):
            # print(data[3:])
            data_int = int(data[3:])
            # print(data)
            force_squeezed_raw[k] = data_int
            k = k + 1

        if (data[0:3] == "DDD"):
            # print(data[3:])
            data_int = int(data[3:])
            #print(data_int)
            encoder_position_squeezed[l] = data_int
            l = l + 1


        if(l == no_squeezes):
            for i in range(no_squeezes):
                force_presqueeze[i] = force_presqueeze_raw[100*i:100*(i+1)].mean()
            print("force_presqueeze: ")
            print(force_presqueeze)
            np.save("force_pre.npy", force_presqueeze, allow_pickle=True)

            for i in range(no_squeezes):
                force_squeezed[i] = force_squeezed_raw[100*i:100*(i+1)].mean()
            print("force_squeezed: ")
            print(force_squeezed)
            np.save("force_after.npy", force_squeezed, allow_pickle=True)

            print("encoder_position_presqueeze: ")
            print(encoder_position_presqueeze)
            np.save("pos_pre.npy", encoder_position_presqueeze, allow_pickle=True)

            print("encoder_position_squeezed: ")
            print(encoder_position_squeezed)
            np.save("pos_after.npy", encoder_position_squeezed, allow_pickle=True)

            #calculating k
            for t in range(no_squeezes):
                delta_F = force_squeezed[t] - force_presqueeze[t]
                delta_D = encoder_position_squeezed[t] - encoder_position_presqueeze[t]

                k = delta_F / delta_D
                k_arr[t] = k
            print(k_arr)
            exit()