from pyfirmata import*
import time
board = Arduino('COM6')

it = util.Iterator(board)  
it.start()

print("Communication Successfully")

Sensor_x = board.get_pin('a:0:i')
Sensor_y = board.get_pin('a:1:i')
Sensor_sw = board.get_pin('d:7:i')


while(True):
    x=Sensor_x.read()
    y=Sensor_y.read()
    sw=Sensor_sw.read()
    print("x= ",end=" ");print(x,end=" ")
    print("y= ",end=" ");print(y,end=" ")
    print("sw= ",end=" ");print(sw)
    time.sleep(0.1)    
