from pyfirmata import*
import time
board = Arduino('COM6')

it = util.Iterator(board)  
it.start()

print("Communication Successfully")

Sensor_x = board.get_pin('a:0:i')
Servo3 = board.get_pin('d:3:s')

while(True):
    x=Sensor_x.read()
    if (x == None):
       pass
    else:
       print("x= ",end=" ");print(x)
       Servo3.write(x*180)
       time.sleep(0.001)  
