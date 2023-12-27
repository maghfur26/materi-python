from tkinter import *
from tkinter import ttk

# init
window = Tk()
window.title("My project")
window.config(bg="white")
window.resizable(False,False)


# agar tinggi dan lebar sesuai ukuran laptop
win_width = window.winfo_screenwidth()
win_height = window.winfo_screenheight()

# geometery = untuk mengatur posisi awla muncul
# format = geometry(f"{lebar} * {tinggi} + {x} + {y}")
lebar = 500
tinggi = 400
x = int((win_width/2) - (lebar/2))
y = int((win_height/2) - (tinggi/2))
window.geometry(f"{lebar}x{tinggi}+{x}+{y}")



# main program

frm = ttk.Frame(window, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)


window.mainloop()