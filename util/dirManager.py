from tkinter import Tk, filedialog

def chooseLocation():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory()