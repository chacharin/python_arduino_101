from pyfirmata import Arduino
import time
board = Arduino('COM6')
print("Communication Successfully")

Servo3 = board.get_pin('d:3:s')

while(True):
    Servo3.write(0)
    time.sleep(1)
    Servo3.write(180)
    time.sleep(1)
