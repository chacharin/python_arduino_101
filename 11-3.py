from pyfirmata import Arduino
import time
board = Arduino('COM6')
print("Communication Successfully")
Servo3 = board.get_pin('d:3:s')

from tkinter import*
window = Tk()
window.geometry("300x200")
window.title("Leanbotic")

def print_s1(val):
    
    scale_value1 = S1.get()
    print("Scale1: "+ str(scale_value1))
    Servo3.write(scale_value1)
    

S1 = Scale(window, from_=0, to=180,width=20, length=250, orient = HORIZONTAL, command=print_s1)
S1.place(x=10, y=0)
