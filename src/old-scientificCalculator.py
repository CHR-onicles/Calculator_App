from tkinter import *
from tkinter import messagebox
from math import * 


root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")

calc=Frame(root,bg="grey")
calc.grid()

equa = "" 
equation = StringVar()
calculation = Entry(calc, textvariable = equation,fg="black",font=('arial',15,'bold'),bg="powder blue",bd=30,width=50,justify=LEFT)
calculation.grid(row=0, columnspan=4,column=0,pady=1)


def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


def EqualPress():
    global equa
    x=calculation.get()  
    if(equa==""):
               equa=equa+x              
    try:
               total = str(eval(equa))
               equation.set(total)
               if(float(total)==0):
                              equa=""
               else:
                              equa=total
    except:
               equation.set("Syntax Error")
               equa=""
               pass                                     
def ClearPress():
    global equa
    equa = ""
    equation.set("")

Button0 = Button(calc, text="0", command = lambda:btnPress(0),bd=4,width=6,height=1,bg="white",relief=SOLID)
Button1 = Button(calc, text="1", command = lambda:btnPress(1), borderwidth=1,bd=4,width=6,height=1,bg="white",relief=SOLID)
Button14 = Button(calc, text="(", command = lambda:btnPress("("), borderwidth=1,bd=4,width=6,height=1,bg="white",relief=SOLID)
Button2 = Button(calc, text="2", command = lambda:btnPress(2), borderwidth=1,bd=4,width=6,height=1,bg="white",relief=SOLID)
Button3 = Button(calc, text="3", command = lambda:btnPress(3), borderwidth=1,bd=4,width=6,height=1,bg="white",relief=SOLID)
Button13 = Button(calc, text="sqrt", command = lambda:btnPress("sqrt("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button4 = Button(calc, text="4", command = lambda:btnPress(4), borderwidth=1,bd=4,width=6,height=1,bg="white",relief=SOLID)
Button15 = Button(calc, text=")", command = lambda:btnPress(")"), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Button5 = Button(calc, text="5", command = lambda:btnPress(5), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Button6 = Button(calc, text="6", command = lambda:btnPress(6), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Button7 = Button(calc, text="7", command = lambda:btnPress(7), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Button16 = Button(calc, text=".", command = lambda:btnPress("."), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Button8 = Button(calc, text="8", command = lambda:btnPress(8), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Button9 = Button(calc, text="9", command = lambda:btnPress(9), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID)
Plus = Button(calc, text="+", command = lambda:btnPress("+"), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Minus = Button(calc, text="-", command = lambda:btnPress("-"), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button18 = Button(calc, text="sin", command = lambda:btnPress("sin("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button22 = Button(calc, text="log", command = lambda:btnPress("log("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Multiply = Button(calc, text="*", command = lambda:btnPress("*"), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button19 = Button(calc, text="cos", command = lambda:btnPress("cos("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button23 = Button(calc, text="pi", command = lambda:btnPress("pi"), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Divide = Button(calc, text="/", command = lambda:btnPress("/"), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button20 = Button(calc, text="factorial", command = lambda:btnPress("factorial("), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Equal = Button(calc, text="=", command = EqualPress, borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Clear = Button(calc, text="MC", command = ClearPress, borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button17 = Button(calc, text="%", command = lambda:btnPress("%"), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button25 = Button(calc, text="degrees", command = lambda:btnPress("degrees("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button26 = Button(calc, text="log", command = lambda:btnPress("log10("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button27 = Button(calc, text="log1p", command = lambda:btnPress("log1p("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button28 = Button(calc, text="radians", command = lambda:btnPress("radians("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button29 = Button(calc, text="sinh", command = lambda:btnPress("sinh("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button30 = Button(calc, text="cosh", command = lambda:btnPress("cosh("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button31 = Button(calc, text="tan", command = lambda:btnPress("tan("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button32 = Button(calc, text="tanh", command = lambda:btnPress("tanh("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button33 = Button(calc, text="E", command = lambda:btnPress("e"), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button34 = Button(calc, text="atan", command = lambda:btnPress("atan("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button36 = Button(calc, text="exp", command = lambda:btnPress("exp("), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button38 = Button(calc, text="asin", command = lambda:btnPress("asin("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button39 = Button(calc, text="acos", command = lambda:btnPress("acos("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button46 = Button(calc, text="ceil", command = lambda:btnPress("ceil("), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button47 = Button(calc, text="floor", command = lambda:btnPress("floor("), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button49 = Button(calc, text="abs", command = lambda:btnPress("abs("), borderwidth=1,bd=4,width=6,height=1,bg="powder blue", relief=SOLID)
Button50 = Button(calc, text="int", command = lambda:btnPress("int("), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)
Button51 = Button(calc, text="float", command = lambda:btnPress("float("), borderwidth=1,bd=4,width=6,height=1,bg="pink", relief=SOLID)




Button13.grid(row = 2, column = 0, padx=10, pady=10)
Button28.grid(row = 2, column =1, padx=10, pady=10)
Button25.grid(row = 2, column = 2, padx=10, pady=10)
Button32.grid(row = 2, column = 3, padx=10, pady=10)




Button26.grid(row = 3, column = 0, padx=10, pady=10)
Button27.grid(row = 3, column = 1, padx=10, pady=10)
Button29.grid(row = 3, column = 2, padx=10, pady=10)
Button30.grid(row = 3, column = 3, padx=10, pady=10)


Button31.grid(row = 4, column = 0, padx=10, pady=10)
Button19.grid(row = 4, column = 1, padx=10, pady=10)
Button18.grid(row = 4, column = 2, padx=10, pady=10)
Button22.grid(row = 4, column = 3, padx=10, pady=10)



Button1.grid(row = 5, column = 0, padx=10, pady=10)
Button2.grid(row = 5, column = 1, padx=10, pady=10)
Button3.grid(row = 5, column = 2, padx=10, pady=10)
Plus.grid(row = 5, column = 3, padx=10, pady=10)



Button4.grid(row = 6, column = 0, padx=10, pady=10)
Button5.grid(row = 6, column = 1, padx=10, pady=10)
Button6.grid(row = 6, column = 2, padx=10, pady=10)
Minus.grid(row = 6, column = 3, padx=10, pady=10)


Button7.grid(row = 7, column = 0, padx=10, pady=10)
Button8.grid(row = 7, column = 1, padx=10, pady=10)
Button9.grid(row = 7, column = 2, padx=10, pady=10)
Multiply.grid(row = 7, column = 3, padx=10, pady=10)



Button14.grid(row = 8, column = 0, padx=10, pady=10)
Button15.grid(row = 8, column = 1, padx=10, pady=10)
Button0.grid(row = 8, column = 2, padx=10, pady=10)
Button17.grid(row = 8, column = 3, padx=10, pady=10)


Clear.grid(row = 9, column = 0, padx=10, pady=10)
Equal.grid(row=9, column=1, padx=10, pady=10)
Button16.grid(row = 9, column = 2, padx=10, pady=10)
Divide.grid(row = 9, column = 3, padx=10, pady=10)


Button23.grid(row = 10, column = 0, padx=10, pady=10)
Button50.grid(row = 10, column = 1, padx=10, pady=10)
Button51.grid(row = 10, column = 2, padx=10, pady=10)
Button20.grid(row = 10, column = 3, padx=10, pady=10)

#Button44.grid(row = 10, column = 3, padx=10, pady=10)
#Button38.grid(row = 10, column = 4, padx=10, pady=10)
#Button39.grid(row = 10, column = 5, padx=10, pady=10)


Button33.grid(row = 11, column = 0, padx=10, pady=10)
Button46.grid(row = 11, column = 1, padx=10, pady=10)
Button47.grid(row = 11, column = 2, padx=10, pady=10)
Button36.grid(row = 11, column = 3, padx=10, pady=10)

#Button42.grid(row = 11, column = 4, padx=10, pady=10)
#Button43.grid(row = 11, column = 3, padx=10, pady=10)


#Button48.grid(row = 10, column = 6, padx=10, pady=10)
#Button49.grid(row = 10, column = 7, padx=10, pady=10)







def exit():
 	root.quit()

def scientific():
  root.resizable(width=False,height=False)
  root.geometry("940x568+0+0")
def standard():
  root.resizable(width=False,height=False)
  root.geometry("466x568+0+0")  


menubar=Menu(calc)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Manu",menu=filemenu)
filemenu.add_command(label="standard",command=standard)
filemenu.add_command(label="scientific",command=scientific)
filemenu.add_separator()
filemenu.add_command(label="exit",command=exit)




Author=Label(root,text="Created by : Patrick Attankurugu",fg="black",font=('arial',10,'bold'),borderwidth=1,bd=4,width=30,height=2,bg="white",relief=SOLID)
Author.grid(row=11,columnspan=8)


root.config(menu=menubar)
root.mainloop()