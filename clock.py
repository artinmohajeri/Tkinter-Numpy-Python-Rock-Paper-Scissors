import tkinter as tk
from time import strftime

def time():
    string = strftime('%H : %M : %S %p')
    label.config(text=string)
    label.after(1000, time)

WIN = tk.Tk()
WIN.minsize(340,100)
WIN.resizable(0,0)
WIN.title("Digital Clock")

label = tk.Label(WIN, font=('None', 40, 'bold'), height=2, background='black', foreground='cyan')
label.pack(anchor='center')

time()

WIN.mainloop()