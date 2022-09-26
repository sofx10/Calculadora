#Importancion de tkinter
#Sofia Gissell Hernandez Ascnecio
#Gilmar Adriel Gonzalez Romero
from tkinter import E, W, Tk, Entry, Label, Radiobutton, IntVar, messagebox
from this import s
from tkinter import *
from tkinter import messagebox

def suma():
	sumar = input1.get() + input2.get()
	messagebox.showinfo("Resultado", sumar)
def resta():
	restar = input1.get() - input2.get()
	messagebox.showinfo("Resultado", restar)
def multi():
	multi = input1.get() * input2.get()
	messagebox.showinfo("Resultado", multi)
def divi():
	divi = input1.get() / input2.get()
	messagebox.showinfo("Resultado", divi)
def modu():
	modu = input1.get() % input2.get()
	messagebox.showinfo("Resultado", modu)
def expo():
	expo = input1.get() ** input2.get()
	messagebox.showinfo("Resultado", expo)

vent1= Tk()
vent1.geometry("400x300")
vent1.title("Calculadora")
vent1.config(bg= "light blue")

input1 = IntVar()
input2 = IntVar()
radio = IntVar()

labl1=Label(vent1, text="Ingrese un numero: ",  bg="black",fg="white")
input11=Entry(vent1,textvariable=input1, bg="light grey")
labl2=Label(vent1, text="Ingrese otro numero: ",  bg="black",fg="white")
input22=Entry(vent1,textvariable=input2, bg="light grey")
rdb1 = Radiobutton(vent1, text="Suma", value=1, variable=radio, bg="light grey", fg="black", command = suma) 
rdb2 = Radiobutton(vent1, text="Resta", value=2, variable=radio, bg="light grey",fg="black" , command= resta)
rdb3 = Radiobutton(vent1, text="Multiplicacion", value=3, variable=radio, bg="light grey",fg="black", command= multi)
rdb4 = Radiobutton(vent1, text="Division", value=4, variable=radio, bg="light grey",fg="black", command=divi)
rdb5 = Radiobutton(vent1, text="Modulo", value=5, variable=radio, bg="light grey",fg="black", command=modu)
rdb6 = Radiobutton(vent1, text="Exponente", value=6, variable=radio, bg="light grey",fg="black", command=expo)


labl1.place(x=30,y=25)
input11.place(x=30,y=60)
labl2.place(x=250,y=25)
input22.place(x=250,y=60)
rdb1.place(x=30,y=120)
rdb2.place(x=30,y=180)
rdb3.place(x=250,y=120)
rdb4.place(x=250,y=180)
rdb5.place(x=30,y=230)
rdb6.place(x=250,y=230)

vent1.mainloop()