from tkinter import*
window = Tk()
window.geometry("300x200")
window.title("Robotics")

def ok():
    print("OK")

B1 = Button(window, text= "OK", command=ok)
B1.place(x=135,y=80)
