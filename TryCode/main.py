#UNA
#Proyecto Paradigmas de Programacion TryCode
#Sergio Villanueva Rios
#Esteban Altamirano
#Ronald Blanco Navarro

from mainFrame import MainFrame
from tkinter import *

def main():
    root = Tk()
    root.wm_title("Compilador TryCode")
    root.resizable(False, False)
    app = MainFrame(root)
    app.mainloop()

if __name__=="__main__":
    main()