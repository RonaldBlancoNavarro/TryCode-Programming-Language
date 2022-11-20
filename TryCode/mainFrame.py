from tkinter import (
    Label,
    Button,
    Entry,
    Frame,
    Place,
    Tk,
    messagebox,
    Radiobutton,
    Text,
    Scrollbar,
    IntVar,
)
import sys
from interpreter import *
# sys.path.insert(1, "\TryCode\TryCode")
# from TryCode import tryCode

# .color1 {color: #5f98d6;}mas oscuro
# .color2 {color: #7fb3de;}
# .color3 {color: #acd0e6;}
# .color4 {color: #deebf1;}
# .color5 {color: #ffffff;} mas claro


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280, height=700, bg="#acd0e6")
        self.var_op = IntVar()
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.btnNuevo = Button(self, text="Nuevo", command=self.limpiar)
        self.btnNuevo.place(x=10, y=10, width=100, height=20)
        self.lblOpciones = Label(self, text="Opciones")
        self.lblOpciones.place(x=100, y=10, width=100, height=20)
        self.btnSalir = Button(self, text="Salir", command=self.master.destroy)
        self.btnSalir.place(x=200, y=10, width=100, height=20)

        self.btnCalcular = Button(self, text="Compilar", command=self.compilar)
        self.btnCalcular.place(x=1100, y=650)
        self.btnCalcular.configure(background="#ffffff")
        self.btnEjecutar = Button(self, text="Ejecutar")
        self.btnEjecutar.place(x=1195, y=650)
        self.btnEjecutar.configure(background="#ffffff")

        Label(self, text="Codigo Entrada:").place(x=10, y=50)
        p_aux = Frame(self)
        p_aux.place(x=10, y=80)
        scroll = Scrollbar(p_aux)
        scroll.pack(side="right", fill="y")
        self.txtInput = Text(p_aux, width=80, height=37, yscrollcommand=scroll.set)
        self.txtInput.pack(side="left")
        scroll.config(command=self.txtInput.yview)

        Label(self, text="Salida:").place(x=700, y=50)
        p_aux = Frame(self)
        p_aux.place(x=700, y=80)
        scroll = Scrollbar(p_aux)
        scroll.pack(side="right", fill="y")
        self.txtOutput = Text(p_aux, width=66, height=34, yscrollcommand=scroll.set)
        self.txtOutput.pack(side="left")
        scroll.config(command=self.txtOutput.yview)

    def limpiar(self):
        self.txtInput.delete(1.0, "end-1c")
        self.txtOutput.delete(1.0, "end-1c")

    def compilar(self):
        self.txtOutput.delete(1.0, "end-1c")
        text = self.txtInput.get(1.0, "end-1c")
        ejecutar(text , self.txtOutput)
        
    def ejecutar(self):
        messagebox.showinfo(title="PruebaEjecutar", message="ejecucion exitosa")
