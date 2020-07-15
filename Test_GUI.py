import tkinter as tk

window = tk.Tk()

List_of_names = ['First Name:','Last Name:']

for i in range(2):
    for j in range(2):
        if j == 0:
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
                
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=List_of_names[i])
            label.pack()
        if j ==1:
            frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
            
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, bg = 'white',width = 50)
            label.pack()

for names in ['Clear','Submit']:
    frame = tk.Frame(master=window, relief='raised', borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=names)
    label.pack()   

window.mainloop()
