import serial
import time
import winsound

portnumber='COM9'
treshold = 3

def sound_alarm():
    for i in range(0, 10):
        winsound.Beep(1000, 440)
        time.sleep(0.5)

ser = serial.Serial(port=portnumber, baudrate=115200, timeout=1)

amt_rain = 0
while True:
    my_str = ser.readline()
    try:
        if(my_str[:16] == b'payload (string)'):
            if(my_str[18:25] == b"raining"):
                print("It is raining outside!!!")
                amt_rain = amt_rain+1
                if(amt_rain>treshold):
                    print("Its raining heavily")
                    sound_alarm()
                    
    
    except:
        pass