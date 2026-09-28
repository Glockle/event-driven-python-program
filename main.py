import tkinter as tk

def sayHi():
    label.config(text="Hi!")

def sayBye():
    label.config(text="Bye!")

window = tk.Tk()

label = tk.Label(window, text="Click a button")
label.pack()

tk.Button(window, text="Hi", command=sayHi).pack()
tk.Button(window, text="Bye", command=sayBye).pack()

window.mainloop()
