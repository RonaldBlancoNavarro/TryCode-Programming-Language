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

# .color1 {color: #5f98d6;}mas oscuro
# .color2 {color: #7fb3de;}
# .color3 {color: #acd0e6;}
# .color4 {color: #deebf1;}
# .color5 {color: #ffffff;} mas claro


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280 , height=700, bg="#acd0e6")
        self.var_op = IntVar()
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
         
         self.btnNuevo = Button(self, text="Nuevo", command=self.compilar)
         self.btnNuevo.place(x=10, y=10, width=100, height=20)
         self.lblOpciones = Label(self, text="Opciones")
         self.lblOpciones.place(x=100, y=10, width=100, height=20)
         self.btnSalir = Button(self, text="Salir", command=self.master.destroy)
         self.btnSalir.place(x=200, y=10, width=100, height=20)

         self.btnCalcular=Button(self,text="Compilar", command=self.compilar)
         self.btnCalcular.place(x=1100,y=650)
         self.btnCalcular.configure(background="#ffffff")         
         self.btnEjecutar=Button(self,text="Ejecutar")
         self.btnEjecutar.place(x=1195,y=650)
         self.btnEjecutar.configure(background="#ffffff")

         Label(self,text="Codigo Entrada:").place(x=10,y=50)
         p_aux =Frame(self)
         p_aux.place(x=10,y=80)
         scroll = Scrollbar(p_aux)
         scroll.pack(side='right', fill='y')
         self.txtInput=Text(p_aux,width=80, height=37, yscrollcommand=scroll.set)
         self.txtInput.pack(side='left')
         scroll.config(command = self.txtInput.yview)
         
         Label(self,text="Salida:").place(x=700,y=50)
         p_aux =Frame(self)
         p_aux.place(x=700,y=80)
         scroll = Scrollbar(p_aux)
         scroll.pack(side='right', fill='y')
         self.txtOutput=Text(p_aux,width=66, height=34, yscrollcommand=scroll.set)
         self.txtOutput.pack(side='left')
         scroll.config(command = self.txtOutput.yview)
         

    def compilar(self):
        messagebox.showinfo(title="PruebaCompilar", message = "compilacion exitosa")

    def ejecutar(self):
        messagebox.showinfo(title="PruebaEjecutar", message = "ejecucion exitosa")    



#  SECCION CODIGO  BASURA


        # fFrac1 = Frame(self, width=100, height=60)
        # fFrac1.place(x=30, y=30)
        # fx1 = Frame(fFrac1, width=42, height=27)
        # fx1.grid(row=0, column=0, rowspan=2)
        # Label(fx1,text="Ent").pack(side="left")
        # self.txt1E = Entry(fx1,width=4)
        # self.txt1E.pack(side="right")
        # Label(fFrac1,text="Num").grid(row=0,column=2)
        # Label(fFrac1,text="Den").grid(row=1,column=2)
        # self.txt1N=Entry(fFrac1,width=4)
        # self.txt1D=Entry(fFrac1,width=4)
        # self.txt1N.grid(row=0,column=1)
        # self.txt1D.grid(row=1,column=1)
        # fFrac2= Frame(self,width=100, height=60)
        # fFrac2.place(x=180,y=30)
        # fx2=Frame(fFrac2,width=42, height=27)
        # fx2.grid(row=0,column=0,rowspan=2)
        # Label(fx2,text="Ent").pack(side="left")
        # self.txt2E = Entry(fx2,width=4)
        # self.txt2E.pack(side="right")
        # Label(fFrac2,text="Num").grid(row=0,column=2)
        # Label(fFrac2,text="Den").grid(row=1,column=2)
        # self.txt2N=Entry(fFrac2,width=4)
        # self.txt2D=Entry(fFrac2,width=4)
        # self.txt2N.grid(row=0,column=1)
        # self.txt2D.grid(row=1,column=1)
        # Label(self,text="Fraccion 1:").place(x=48,y=8)
        # Label(self,text="Fraccion 2:").place(x=198,y=8)



        # Label(self,text="Operación:").place(x=30,y=150)
        # self.btnCalcular=Button(self,text="Calcular", command=self.compilar)
        # self.btnCalcular.place(x=210,y=150)

        # opciones={"Suma":0, "Resta":1, "Multiplicación":2,"División":3, "Son Iguales?":4}
        # posy=150
        # for (t,v) in opciones.items():
        #     Radiobutton(self, text=t, value=v, variable = self.var_op).place(x=100,y=posy)
        #     posy=posy+20

    #def fCalcular(self):
       # e1 = int(self.txt1E.get())
    #     n1 = int(self.txt1N.get())
    #     d1 = int(self.txt1D.get())
    #     #f1 = FracMix(e1,n1,d1)
    #     e2 = int(self.txt2E.get())
    #     n2 = int(self.txt2N.get())
    #     d2 = int(self.txt2D.get())
    #    # f2 = FracMix(e2,n2,d2)
    #     if self.var_op.get() == 4:
    #         if f1 == f2:
    #             messagebox.showinfo(title="Fracciones Mixtas", message = "Las fracciones son iguales")
    #         else:
    #             messagebox.showinfo(title="Fracciones Mixtas", message = "Las fracciones son diferentes")
    #     else:
    #         if self.var_op.get() == 0:
    #             f3 = f1+f2
    #         elif self.var_op.get() == 1:
    #             f3 = f1-f2
    #         elif self.var_op.get() == 2:
    #             f3 = f1*f2
    #         elif self.var_op.get() == 3:
    #             f3 = f1/f2
    #         self.txtRes.insert(1.0,f3)