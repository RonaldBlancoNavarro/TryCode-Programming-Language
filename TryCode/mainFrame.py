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
from lexer import TryCodeLexer
from parser import TryCodeParser

# sys.path.insert(1, "\TryCode\TryCode")
# from TryCode import tryCode

def extraerExpresion(self):    #encontar ; mas cercano y retornar la cadena de texto desde el inicio hasta el ;
    expresion = ""
    if self.input == "":
        return ""
    try:
        if self.input.index(";") >= 0:
            expresion = self.input[0:self.input.index(";")] # extraer la expresion
            self.input = self.input[self.input.index(";")+1:] # eliminar todo lo que esta hasta el ;
            return expresion    
    except ValueError:
        return "-1"


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280, height=700, bg="#2c4b65")
        self.var_op = IntVar()
        self.master = master
        self.pack()
        self.lexer = TryCodeLexer()
        self.parser = TryCodeParser()
        self.env = {}
        self.create_widgets()
        self.input=""

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
        self.input = self.txtInput.get(1.0, "end-1c")
        while True:
            text = extraerExpresion(self)
            if text == "-1":
                self.txtOutput.insert(END, '\n')
                self.txtOutput.insert(END, "Error usencia decaracter ';' al final de expresion -  Compilacion finalizada")
                return                    
            if text:
                tree = self.parser.parse(self.lexer.tokenize(text))
                TryCodeExecute(tree, self.env, self.txtOutput)
                self.txtOutput.see(END)
            else:
                self.txtOutput.insert(END, '\n')
                self.txtOutput.insert(END, "Compilacion finalizada")
                return

    def ejecutar(self):
        messagebox.showinfo(title="PruebaEjecutar", message="ejecucion exitosa")




            # text = input

            # print(self.input)
            # print("----------------------")
            # print(text)


            # lexer1 = self.lexer.get_lexer()
            # print(lexer1)
            # print("hola mundo")

            # listaExpresion = []  # Tokens dentro de una expresion
            # listaExpresiones=[]  # Lista de expresiones
            # for tok in self.lexer.tokenize(text):
            #     print(tok)
            #     if tok.type != ';':
            #         listaExpresion.append(tok)
            #     else:
            #         listaExpresiones.append(listaExpresion)
            #         listaExpresion = []
            # tree = self.parser.parse(listaExpresiones)
            # TryCodeExecute(tree, self.env , self.txtOutput)
            # self.txtOutput.see(END)

            # print(self.parser.parse(self.lexer.tokenize(text)))