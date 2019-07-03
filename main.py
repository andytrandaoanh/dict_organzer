import tkinter as tk
import lexicon_gui



win = tk.Tk()

win.title("Dictionary Organizer")
win.geometry("760x540") 
win.resizable(0, 0) 


myGUI = lexicon_gui.LexGUI(win)

myGUI.createGUI()


win.mainloop()