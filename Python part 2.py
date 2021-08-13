import serial
import time
data=serial.Serial('com3',9600)
time.sleep(2)
print('initializing...')

#status=float(string)
time.sleep(0.1)
while(1==1):
    k=input('enter A for auto nd M  for manual')
    if(k=='2'):
        data.write(b'2')
        b = data.readline()
        time.sleep(2)
        string_n = b.decode()
        string = string_n.rstrip()
        print('Automatic setting applied!')
        print ('motor on')
        data.write(b'ON')
        print ('status of water level:)',string)
        break
    elif(k=='1'):
        data.write(b'2')
        b = data.readline()
        time.sleep(2)
        string_n = b.decode()
        string = string_n.rstrip()
        print('Manual setting applied!')
        print('status of water level:',string)
        u=input('enter command')
        if(u=='ON'):
         print('motor on')
        data.write(b'ON')
        u = input('enter command')
        if(u=='OFF'):
         print('motor off')
        data.write(b'OFF')
        break
