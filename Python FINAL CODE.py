import serial
import time
data=serial.Serial('com3',9600) #setting the serial communication bw python and arduino
time.sleep(2) #time delay for let the communication establish
print('initializing...')
M=1
A=2
ON=3
#status=float(string)
time.sleep(0.1)
while(1==1):
    k=input('enter {A} for auto nd {M}  for manual\n''OR\n''enter {sON} for turning on sprinkler &  {sOFF} for turning it off\n'':>')
    #user have to give the command according to his desired work
    if(k=='A'):#user selected automatic mode
        data.write(b'2')#giving command to arduino in bytes
        b = data.readline()#getting output from the command
        time.sleep(2)
        string_n = b.decode()
        string = string_n.rstrip()
        print('Automatic setting applied!')
        print ('motor WORKING..')
        data.write(b'ON')
        print ('status of water level:',string)
    elif(k=='M'):#user selected the manual mode
        data.write(b'1')
        b = data.readline() # read the arduino output
        time.sleep(2)
        string_n = b.decode() #decoding the input value from arduino
        string = string_n.rstrip()
        print('Manual setting applied!')
        print('status of water level:',string)
        u=input('enter {ON}m to turn on motor & {OFF} to turn off motor')#command for motor working
        if(u=='ON'):#motor on
         print('motor on')
         data.write(b'3')
        if(u=='OFF'):#motor off
         print('motor off')
         data.write(b'4')
    if(k=='sON'):#sprinkler on command
        data.write(b'5')
        print('sprinkler ON')

    if(k=='sOFF'):#sprinkler off command
        data.write(b'6')
        print('sprinkler OFF')
        
