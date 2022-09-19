def bitsToUnsigned2(no1, no2):
   str1 = bin(int(line[no1]))[2:].zfill(8)
   str2 = bin(int(line[no2]))[2:].zfill(8)
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


line = b'\xAA\x00'
line = b'\x00\x90'

number = bitsToUnsigned2(0,1)
print(number)
number = float(number) / 100
print(number)