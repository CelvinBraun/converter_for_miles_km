from tkinter import *
from convert import Convert

# window settings
window = Tk()
window.minsize(height=80, width=200)
window.title("Converter for Km/Miles")

convert  = Convert()

window.mainloop()