from tkinter import*
window = Tk()
window.geometry("300x300")
window.title("Robot_arm")

from pyfirmata import Arduino
import time
board = Arduino('COM12')

Servo_A = board.get_pin('d:11:s') 
Servo_B = board.get_pin('d:10:s') 
Servo_C = board.get_pin('d:9:s') 
Servo_D = board.get_pin('d:8:s') 
Servo_A.write(80) #limit 70-180
Servo_B.write(90) #limit 50-120
Servo_C.write(120) #limit 90-150
Servo_D.write(90) #limit 5-175
time.sleep(0.5)
print("Communication Successfully")

def reset_position():
	Servo_A.write(80)
	Servo_B.write(90)
	Servo_C.write(120)
	Servo_D.write(90)
	time.sleep(0.5)






def arm_action():
	Servo_A.write(90)
	time.sleep(0.5)
	Servo_B.write(90)
	time.sleep(0.5)
	Servo_C.write(150)
	time.sleep(0.5)
	Servo_D.write(90)
	time.sleep(0.5)

	Servo_A.write(180)
	time.sleep(0.5)
	Servo_B.write(120)
	time.sleep(0.5)
	Servo_C.write(125)
	time.sleep(0.5)
	Servo_D.write(90)
	time.sleep(0.5)

	Servo_A.write(180)
	time.sleep(0.5)
	Servo_B.write(80)
	time.sleep(0.5)
	Servo_C.write(150)
	time.sleep(0.5)
	Servo_D.write(90)
	time.sleep(0.5)

	reset_position()

def run_onece():
	arm_action()

def run_repeat():
	while(1):
    		arm_action()


B0 = Button(window,text = "Reset all Position", command=reset_position)
B0.pack()
B1 = Button(window, text="Run one time",command = run_onece)
B1.pack()
B2 = Button(window,text="Run repeat", command = run_repeat)
B2.pack()
