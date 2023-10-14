from pyfirmata import Arduino
import time
board = Arduino('COM6')
print("Communication Successfully")

led13 = board.get_pin('d:13:o')

while(True):
    led13.write(1)
    time.sleep(1)
    led13.write(0)
    time.sleep(1)
