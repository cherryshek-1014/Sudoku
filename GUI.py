import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text = 'Hello Tkinter',
                    fg = 'white',
                    bg = '#34A2FE',
                    )

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)


entry = tk.Entry(fg='yellow',
                 bg='blue',
                 width = 50)

for names,index in {'Clear':0,'Submit':1}:
    frame = tk.Frame(master=window,relief='raised', borderwidth=5)
    frame.grid(column = index,padx=5)
    label = tk.Label(master=frame, text=names,width=7)
    label.pack()   


window.mainloop()
