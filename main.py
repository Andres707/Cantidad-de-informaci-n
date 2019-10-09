import math
import easygui as eg
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt


def graficar(carater, i, h):
    x = []
    y = []
    xi = []
    yi = []
    for j in range(len(carater)):
        x.append(j + 1)
        y.append(h[j])
        xi.append(j + 1)
        yi.append(i[j])
    plt.grid()
    plt.plot(x, y, '-', linewidth=2, color='r')
    plt.plot(x, y, 'o', linewidth=3, color=(0.2, 0.1, 0.4))
    plt.plot(xi, yi, '-', linewidth=2, color='r')
    plt.plot(xi, yi, 'o', linewidth=3, color=(0.2, 0.1, 0.4))
    plt.xlabel('x')
    plt.ylabel('H')
    plt.title('Cantidad de informacion')
    plt.show()


class APP:

    def __init__(self):
        # Creat Window
        self.r = Tk()
        self.r.geometry('400x500')
        self.r.configure(bg='beige')
        self.r.title('Cantidad de Informacaion')
        # Creat Pestañas
        tab_control = ttk.Notebook(self.r)
        txt = ttk.Frame(tab_control)
        arch = ttk.Frame(tab_control)
        tab_control.add(txt, text='Texto')
        tab_control.add(arch, text='Archivo')
        tab_control.pack(expand=1, fill='both')
        # ARchivo
        # text box
        self.cajC = ScrolledText(arch, width=7, height=15)
        self.cajC.place(x=10, y=130)
        self.cajPD = ScrolledText(arch, width=8, height=15)
        self.cajPD.place(x=95, y=130)
        self.cajI = ScrolledText(arch, width=8, height=15)
        self.cajI.place(x=200, y=130)
        self.cajH = ScrolledText(arch, width=8, height=15)
        self.cajH.place(x=300, y=130)
        self.cajLectura = ScrolledText(arch, width=35, height=4)
        self.cajLectura.place(x=10, y=29)
        self.cajaruta = ttk.Entry(arch, justify=tk.LEFT)
        self.cajaruta.place(x=10, y=5, width=298, height=20)
        self.cajaruta.insert(0, 'c:/usuario/ejemplo')
        # self.cajLectura.config(state=tk.DISABLED)

        # Labels
        laC = Label(arch, text="Caracter", fg="black")
        laC.place(x=10, y=105)
        laPD = Label(arch, text="Pro. Decimal", fg="black")
        laPD.place(x=95, y=105)
        laI = Label(arch, text="I", fg="black")
        laI.place(x=200, y=105)
        laH = Label(arch, text="H", fg="black")
        laH.place(x=300, y=105)

        # button inicio arch
        self.botnini = ttk.Button(arch, text='Archivo', command=self.direccion)
        self.botnini.place(x=315, y=4)
        self.btninicio = ttk.Button(arch, text='Iniciar', command=self.cantidad)
        self.btninicio.place(x=315, y=35)
        self.btninicio.config(state=tk.DISABLED)
        # TExto
        # text box
        self.cajatexto = ScrolledText(txt, width=35, height=5)
        self.cajatexto.place(x=10, y=15)
        self.cajaC = ScrolledText(txt, width=7, height=15)
        self.cajaC.place(x=10, y=130)
        self.cajaPD = ScrolledText(txt, width=8, height=15)
        self.cajaPD.place(x=95, y=130)
        self.cajaI = ScrolledText(txt, width=8, height=15)
        self.cajaI.place(x=200, y=130)
        self.cajaH = ScrolledText(txt, width=8, height=15)
        self.cajaH.place(x=300, y=130)
        laC = Label(txt, text="Caracter", fg="black")
        laC.place(x=10, y=105)
        laPD = Label(txt, text="Pro. Decimal", fg="black")
        laPD.place(x=95, y=105)
        laI = Label(txt, text="I", fg="black")
        laI.place(x=200, y=105)
        laH = Label(txt, text="H", fg="black")
        laH.place(x=300, y=105)
        # button inicio txt
        self.botonini = ttk.Button(txt, text='Iniciar', command=self.cantidad)
        self.botonini.place(x=315, y=15)
        self.r.mainloop()

    def cantidad(self):
        self.limpiesa(1)
        ruta = self.cajaruta.get()
        if ruta == "c:/usuario/ejemplo":
            texto = self.cajatexto.get('0.1', END)
            T = 1
        else:
            texto = []
            ruta = self.cajaruta.get()
            print(ruta)
            archivo = open(ruta, encoding="utf8")
            txt = archivo.readlines()
            self.cajLectura.insert('0.1', txt)
            for i in range(len(txt)):
                for j in range(len(txt[i])):
                    texto.append(txt[i][j])
            texto = str(texto)
            T = 0
            archivo.close()
        longitud = (len(texto)) - 1
        # print(longitud)
        # print(ascii(texto))
        cadena = []
        for i in range(longitud):
            cadena.append(texto[i])
        # print(texto)
        # print(cadena)
        caracter = []
        for i in range(longitud):
            zero = caracter.count(texto[i])
            if zero == 0:
                caracter.append(texto[i])
        # print(caracter)
        prob = []
        for i in range(len(caracter)):
            p = cadena.count(caracter[i])
            pro = round((p / longitud), 5)
            prob.append([pro, caracter[i]])
        # print(prob)
        I = []
        H = []
        for j in range(len(caracter)):
            ii = round(math.log2(1 / prob[j][0]), 3)
            I.append(ii)
            hh = round(prob[j][0] * (math.log2(1 / prob[j][0])), 3)
            H.append(hh)
        # print(I)
        # print(H)
        self.imprimitxt(caracter, prob, I, H, T)
        graficar(caracter, I, H)
        self.limpiesa(0)

    def imprimitxt(self, caracter, prob, I, H, t):
        if t == 1:
            for i in range(len(caracter)):
                self.cajaC.insert(0.1, caracter[i] + '\n')
                self.cajaPD.insert(0.1, prob[i][0])
                self.cajaI.insert(0.1, I[i])
                self.cajaH.insert(0.1, H[i])
                if i < len(caracter) - 1:
                    self.cajaPD.insert(0.1, '\n')
                    self.cajaI.insert(0.1, '\n')
                    self.cajaH.insert(0.1, '\n')
        else:
            for j in range(len(caracter)):
                self.cajC.insert(0.1, caracter[j] + '\n')
                self.cajPD.insert(0.1, prob[j][0])
                self.cajI.insert(0.1, I[j])
                self.cajH.insert(0.1, H[j])
                if j < len(caracter) - 1:
                    self.cajPD.insert(0.1, '\n')
                    self.cajI.insert(0.1, '\n')
                    self.cajH.insert(0.1, '\n')

    def direccion(self):
        # self.cajaruta.config(state=tk.NORMAL)
        self.cajaruta.delete(0, END)
        extension = ["*.txt"]
        archivo = eg.fileopenbox(msg="Abrir archivo",
                                 title="Control: fileopenbox",
                                 default='',
                                 filetypes=extension)
        self.cajaruta.insert(0, archivo)
        self.cajaruta.config(state=tk.DISABLED)
        self.btninicio.config(state=tk.NORMAL)

    def limpiesa(self, tipo):
        if tipo == 1:
            self.cajaC.delete(0.1, END)
            self.cajaH.delete(0.1, END)
            self.cajaPD.delete(0.1, END)
            self.cajaI.delete(0.1, END)
            self.cajC.delete(0.1, END)
            self.cajH.delete(0.1, END)
            self.cajPD.delete(0.1, END)
            self.cajI.delete(0.1, END)
        elif tipo == 0:
            self.cajaruta.config(state=tk.NORMAL)
            self.cajaruta.delete(0, END)
            self.cajaruta.insert(0, 'c:/usuario/ejemplo')


def main():
    mi_app = APP()
    return 0


if __name__ == '__main__':
    main()
