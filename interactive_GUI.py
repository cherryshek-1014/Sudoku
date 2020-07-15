import tkinter as tk
import random

window = tk.Tk()

def rand_num():
    value = random.randrange(1,6)
    lbl_value['text'] = f"{value}"

window.rowconfigure([0,1], minsize=50)
window.columnconfigure(0, minsize=150)

btn_roll = tk.Button(master=window, text='Roll',command=rand_num)
btn_roll.grid(row=0,column=0,sticky='nsew')

lbl_value = tk.Label(master=window,text='')
lbl_value.grid(row=1,column=0)

window.mainloop()
