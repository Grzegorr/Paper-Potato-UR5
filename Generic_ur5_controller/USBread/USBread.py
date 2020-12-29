import os, sys
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

#test_name = "raw_potato"
#test_name = "ten_min_potato"
#test_name = "fifteen_min_potato"
#test_name = "twenty_min_potato"
#test_name = "twentyfive_min_potato"
#test_name = "30_min_potato"
#test_name = "35_min_potato"
test_name = "45_min_potato"

#test_name = "test"


data_len = 4000

def bitsToUnsigned(no1, no2):
   str1 = bin(int(line[no1]))[2:].zfill(8)
   str2 = bin(int(line[no2]))[2:].zfill(8)
   print("Line[no1]: " + str(line[no1]))
   print("int(Line[no1]): " + str(int(line[no1])))
   print("bin(int(line[no2])): " + str(bin(int(line[no2]))))
   print("String1: " + str1)
   output_number = 0
   for i in range(8):
      if str1[i] == '1':
         output_number = output_number + 2 ** i
   for i in range(7):
      if str2[i] == '1':
         output_number = output_number + 2 ** (i + 8)
   if str2[7] == '1':
      output_number = - output_number
   return output_number

def bitsToUnsigned2(no1, no2):
   str1 = bin(int(line[no1]))[2:].zfill(8)
   str2 = bin(int(line[no2]))[2:].zfill(8)

   #print("Line[no1]: " + str(line[no1]))
   #print("int(Line[no1]): " + str(int(line[no1])))
   #print("bin(int(line[no1])): " + str(bin(int(line[no1]))))
   #print("String1: " + str1)

   output_number = 0
   for i in range(8):
      if str1[i] == '1':
         output_number = output_number + 2 ** (7-i)
   for i in range(1,8):
      if str2[i] == '1':
         output_number = output_number + 2 ** (7-i + 8)
   if str2[0] == '1':
      output_number = - output_number
   return output_number


def bitsToUnsigned3(no1, no2):
   str1 = bin(int(line[no1]))[2:].zfill(8)
   str2 = bin(int(line[no2]))[2:].zfill(8)

   #print("Line[no1]: " + str(line[no1]))
   #print("int(Line[no1]): " + str(int(line[no1])))
   #print("bin(int(line[no1])): " + str(bin(int(line[no1]))))
   #print("String1: " + str1)

   output_number = 0
   for i in range(8):
      if str1[i] == '1':
         output_number = output_number + 2 ** (7-i)
   for i in range(1,8):
      if str2[i] == '1':
         output_number = output_number + 2 ** (7-i + 8)
   if str2[0] == '1':
      output_number = output_number - 2**15
   return output_number


print("Hello frm USB read!")
###Setup for data storage###
data = np.zeros((data_len,6))
iter_data = 0


ser = serial.Serial(port='COM4', baudrate=19200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=10)
print("I am connected.")

# listen for the input, exit if nothing received in timeout period
while True:
   syncBit = ser.read(1)
   if syncBit == b'\x20':
      print("Got 1st sync bit.")
      syncBit = ser.read(1)
      if syncBit == b'\x4e':
         print("Got 2nd sync bit.")
         break


while True:
   line = ser.read(16)
   if len(line) == 0:
      print("Time out! Exit.\n")
      sys.exit()
   #print(line.hex())
   #Combining the bits from the data
   #print(bin(int(line[0]))[2:].zfill(8))
   Fx = bitsToUnsigned3(0, 1)
   #print("Sign: " + str(bin(int(line[1]))[2:].zfill(8)[0])) #that is correct with index 0
   Fy = bitsToUnsigned3(2, 3)
   Fz = bitsToUnsigned3(4, 5)
   Mx = bitsToUnsigned3(6, 7)
   My = bitsToUnsigned3(8, 9)
   Mz = bitsToUnsigned3(10, 11)


   #Now taking care for convention multipliers
   Fx = float(Fx) / 100
   Fy = float(Fy) / 100
   Fz = float(Fz) / 100
   Mx = float(Mx) / 1000
   My = float(My) / 1000
   Mz = float(Mz) / 1000

   current_data = [Fx,Fy,Fz,Mx,My,Mz]
   data[iter_data,:] = current_data[:]
   print(iter_data)
   #print(data[iter_data])
   iter_data = iter_data + 1

   if iter_data == data_len:
      np.save(str(test_name) + ".npy",data, allow_pickle=True)
      #data = np.load("raw_potato.npy", allow_pickle=True)
      plt.plot(data[:,0])
      plt.title(str(test_name))
      plt.ylabel("Fx")
      plt.xlabel("data_point")
      #plt.show()
      plt.savefig(str(test_name) + "Fx.png")
      plt.clf()

      plt.plot(data[:, 1])
      plt.title(str(test_name))
      plt.ylabel("Fy")
      plt.xlabel("data_point")
      #plt.show()
      plt.savefig(str(test_name) + "Fy.png")
      plt.clf()

      plt.plot(data[:, 2])
      plt.title(str(test_name))
      plt.ylabel("Fz")
      plt.xlabel("data_point")
      #plt.show()
      plt.savefig(str(test_name) + "Fz.png")
      plt.clf()

      plt.plot(data[:, 3])
      plt.title(str(test_name))
      plt.ylabel("Mx")
      plt.xlabel("data_point")
      #plt.show()
      plt.savefig(str(test_name) + "Mx.png")
      plt.clf()

      plt.plot(data[:, 4])
      plt.title(str(test_name))
      plt.ylabel("My")
      plt.xlabel("data_point")
      #plt.show()
      plt.savefig(str(test_name) + "My.png")
      plt.clf()

      plt.plot(data[:, 5])
      plt.title(str(test_name))
      plt.ylabel("Mz")
      plt.xlabel("data_point")
      #plt.show()
      plt.savefig(str(test_name) + "Mz.png")
      plt.clf()

   print("Fx: " + str(Fx) + " Fy: " + str(Fy) + " Fz: " + str(Fz) + " .")
   #print()
   #print(str(2**3))













