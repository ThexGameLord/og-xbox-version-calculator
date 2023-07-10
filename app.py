from tkinter import *
from tkinter import ttk
from tkinter import messagebox

v1_0 = [3944, 4034, 4036, 4627]
v1_1 = [4817, 4972]
v1_2_1_5 = [5101, 5713]
v1_6 = [5838]

def calculate_ver():
    userXB = entry.get()

    if userXB == "":
        XBresult = "No Kernel Inputted"
    elif len(userXB) < 4 and userXB.isdigit():
        XBresult = "Invalid Kernel Inputted (Not long enough)"
    elif len(userXB) > 4 and userXB.isdigit():
        XBresult = "Invalid Kernel Inputted (Too long)"
    elif not userXB.isdigit():
        XBresult = "Invalid Kernel Inputted (Numbers Only)"
    elif int(userXB) in v1_0:
        XBresult = "1.0"
    elif int(userXB) in v1_1:
        XBresult = "1.1"
    elif int(userXB) in v1_2_1_5:
        XBresult = "1.2 - 1.5"
    elif int(userXB) in v1_6:
        XBresult = "1.6"
    else:
        XBresult = "Unknown"

    ver_label['text'] = f"Xbox Version: {XBresult}"

root = Tk()
root.geometry("308x70")
root.minsize(400, 75)
root.maxsize(400, 75)
root.title("og xbox version calculator")

ver_label = ttk.Label(root, text="Xbox Version:")
calculate_button = ttk.Button(root, text="Calculate Version", command=calculate_ver)
ver_label.pack()

entry = ttk.Entry(root)
entry.pack()

calculate_button.place(x=150, y=45, width=100)
root.mainloop()
