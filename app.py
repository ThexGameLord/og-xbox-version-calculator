from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calculate_ver():
    pcid_label['text'] = f"PCID: {pcid}"

  


root = Tk()
root.geometry("308x70")
root.minsize(600, 70)
root.maxsize(600, 70)
root.title("GFWL PCID Fix")

pcid_label = ttk.Label(root, text="Xbox Version")
calculate_button = ttk.Button(root, text="Calculate Version", command=calculate_ver)

pcid_label.pack()
generate_button.place(x=110, y=40, width=90)
root.mainloop()
 
