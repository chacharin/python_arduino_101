from tkinter import*
window = Tk()
window.geometry("300x200")
window.title("Robotics")

def print_s1(val):
    scale_value1 = S1.get()
    print("Scale1: "+ str(scale_value1))
    
def print_s2(val):
    scale_value2 = S2.get()
    print("Scale2: "+ str(scale_value2))

S1 = Scale(window, from_=0, to=100,width=20, length=180, orient = VERTICAL, command=print_s1)
S1.place(x=10, y=0)

S2 = Scale(window, from_=0, to=50,width=10, length=100,orient = HORIZONTAL, command=print_s2)
S2.place(x=80, y=80)
