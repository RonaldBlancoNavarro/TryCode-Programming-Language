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
from tkinter import *
from tkinter import messagebox as MessageBox
from lexer import TryCodeLexer
from parser import TryCodeParser

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

class MainFrame(Frame):  # creacion de la vista
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
        

    def create_widgets(self):# creacion de elementos en pantalla

        #Creacion de menu de opciones
        menubar=Menu(self.master)

        self.master.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=self.limpiar)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.master.quit)

        Words = Menu(menubar, tearoff=0)
        Words.add_command(label="PRINT", command= self.PRINT)
        Words.add_command(label="IF", command= self.IF)
        Words.add_command(label="FOR", command= self.FOR)
        Words.add_command(label="WHILE", command= self.WHILE)

        Types = Menu(menubar, tearoff=0)
        Types.add_command(label="STRING", command= self.STRING)
        Types.add_command(label="NUMBER", command= self.NUMBER)
        Types.add_command(label="FLOAT", command= self.FLOAT)
        Types.add_command(label="TRUE", command= self.TRUE)
        Types.add_command(label="FALSE", command= self.FALSE)

        Examples = Menu(menubar, tearoff=0)
        Examples.add_command(label="Ejemplo#1", command= self.EJEMPLO1)
        Examples.add_command(label="Ejemplo#1", command= self.EJEMPLO2)
        

        Optionmenu = Menu(menubar, tearoff=0)
        Optionmenu.add_cascade(label="Palabras reservadas",menu=Words)
        Optionmenu.add_cascade(label="Tipos de datos", menu=Types)
        Optionmenu.add_cascade(label="Ejemplos",menu=Examples)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...", command=self.AcercaDe)

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Opciones", menu=Optionmenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        #Creacion de botones
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

    #ejemplos de codigo

    def PRINT(self):
        self.txtInput.insert(END,"PRINT("'"Hola Mundo"'");")
    def IF(self):
        self.txtInput.insert(END,"a=1;\nIF a==1 THEN\na\nELSE\na+2;")
    def FOR(self):
        self.txtInput.insert(END,"FOR a=0 TO 5 THEN a;")
    def WHILE(self):
        self.txtInput.insert(END,"a=1;\nWHILE a<3 THEN\na\na=a+1;")
    def FUN(self):
        self.txtInput.insert(END,"FUN hello() -> x=10;")
    def STRING(self):
        self.txtInput.insert(END,"var="'"hola"'";")
    def NUMBER(self):
        self.txtInput.insert(END,"x=5;")
    def FLOAT(self):
        self.txtInput.insert(END,"y=2.5;")
    def TRUE(self):
        self.txtInput.insert(END,"TRUE")
    def FALSE(self):
        self.txtInput.insert(END,"FALSE")
    def EJEMPLO1(self):
        self.txtInput.insert(END,"n1 = 9 - 6;\nn2 = 4 + 2;\nPRINT(n1);\nPRINT(n2);\nIF n1<n2 THEN\nPRINT(n1)\nELSE\nPRINT(n2);")
    def EJEMPLO2(self):
        self.txtInput.insert(END,"x = 0;\nPRINT(x);\nWHILE x<5 THEN\nx\nx=x+1;")

    def limpiar(self):#limpiar input y output
        self.txtInput.delete(1.0, "end-1c")
        self.txtOutput.delete(1.0, "end-1c")

    def compilar(self): #compilar codigo
        self.txtOutput.delete(1.0, "end-1c")
        self.input = self.txtInput.get(1.0, "end-1c")
        while True:
            text = extraerExpresion(self)
            if text == "-1":
                self.txtOutput.insert(END, '\n')
                self.txtOutput.insert(END, "Error: ausencia de caracter ';' al final de expresion -  Compilacion finalizada")
                return                    
            if text:
                tree = self.parser.parse(self.lexer.tokenize(text)) #analisis lexico y sintactico
                TryCodeExecute(tree, self.env, self.txtOutput)#ejecucion
                self.txtOutput.see(END)
            else:
                self.txtOutput.insert(END, '\n')
                self.txtOutput.insert(END, "Compilacion finalizada")
                return

    def AcercaDe(self):
        MessageBox.showinfo("Acerca de este proyecto", "Curso: Paradigmas de programación 2022\nElaborado por:\nSergio Villanueva Ríos\nRonald Blanco Navarro\nEsteban Altamirano Granados")
        
    def ejecutar(self):
        messagebox.showinfo(title="PruebaEjecutar", message="ejecucion exitosa")
