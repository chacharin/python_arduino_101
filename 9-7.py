from tkinter import*
window = Tk()
window.geometry("300x200")
window.title("Leanbotic")

def print_s1(val):
    global scale_value1
    scale_value1 = S1.get()
    
def print_s2(val):
    global scale_value2
    scale_value2 = S2.get()

def change_label():
    global scale_value1
    global scale_value2
    L1.configure(text=scale_value1 + scale_value2)
    L1.update()

L1 = Label(window, text=0, bg="yellow")
L1.pack()

B1 = Button(window,text="Show Result",command=change_label)
B1.pack()

S1 = Scale(window, from_=0, to=100,width=20, length=180, orient = VERTICAL, command=print_s1)
S1.place(x=10, y=0)

S2 = Scale(window, from_=0, to=50,width=10, length=100,orient = HORIZONTAL, command=print_s2)
S2.place(x=80, y=80)
