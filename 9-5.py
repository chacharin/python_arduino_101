from tkinter import*
window = Tk()
window.geometry("300x200")
window.title("Robotics")

def Print():
    text_value = E1.get()
    print(text_value)

E1 = Entry(window, width=10)
E1.place(x=100,y=50)

B1 = Button(window, text= "Print", command=Print)
B1.place(x=135,y=80)
