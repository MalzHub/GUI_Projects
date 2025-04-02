import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Arial", 50, "bold"), background="black", foreground="cyan")
clock_label.pack(anchor="center")

def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time) 

update_time()

root.mainloop()
