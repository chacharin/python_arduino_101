from pyfirmata import Arduino
import time
board = Arduino('COM6')
print("Communication Successfully")

Servo3 = board.get_pin('d:3:s')
Servo3.write(0)
time.sleep(1)

position=0
while(position<=180):
    Servo3.write(position)
    position = position+1
    time.sleep(0.0008)

position=180
while(position>=0):
    Servo3.write(position)
    position = position-1
    time.sleep(0.0008)
