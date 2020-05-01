from tkinter import *
import math
import parser
import tkinter.messagebox


root = Tk()
root.title("Scientific Calculator ISMART")
root.resizable(width = False, height = False)

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ',':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "Add":
            self.total += self.current
        if self.op == "Sub":
            self.total -= self.current
        if self.op == "Mul":
            self.total *= self.current
        if self.op == "Div":
            self.total /= self.current
        if self.op == "Mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current =float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
    def PM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)
    def factorial(self):
        self.result = False
        self.current = math.factorial(float(txtDisplay.get()))
        self.display(self.current)
    def square(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()),2)
        self.display(self.current)
    def pow(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()), 3)
        self.display(self.current)
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), width=18, bd=30, insertwidth=5, bg="powder blue", justify='right')
txtDisplay.grid(row=0, column=0, columnspan=5)
txtDisplay.insert(0, "0")
#=======================================================Numbers Button=====================================
numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(1,4):
        btn.append(Button(calc, width=6, bd=8, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i] ["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
        i +=1
#=========================================================Buttons==========================================
btnRadian = Button(calc, text="Radians", width=6, bd=8, fg="black", command = added_value.radians).grid(row=1, column=0)
btnSquare = Button(calc, text="x^2", width=6, bd=8, fg="black", command = added_value.square).grid(row=1, column=1)
btnClear = Button(calc, text="C", width=6, bd=8, fg="black", command = added_value.Clear_Entry).grid(row=1, column=2)
btnAll_clear = Button(calc, text="AC", width=6, bd=8, fg="black", command = added_value.all_Clear_Entry).grid(row=1, column=3)
btnDiv = Button(calc, text="/", width=6, bd=8, fg="black", command = lambda : added_value.operation("Div")).grid(row=1, column=4)

btn2pi = Button(calc, text="2π", width=6, bd=8, fg="black", command = added_value.tau).grid(row=2, column=0)
btnMult = Button(calc, text="*", width=6, bd=8, fg="black", command = lambda : added_value.operation("Mul")).grid(row=2, column=4)

btnPi = Button(calc, text="π", width=6, bd=8, fg="black", command = added_value.Pi).grid(row=3, column=0)
btnSub = Button(calc, text="-", width=6, bd=8, fg="black", command = lambda : added_value.operation("Sub")).grid(row=3, column=4)

btnE = Button(calc, text="e", width=6, bd=8, fg="black", command = added_value.e).grid(row=4, column=0)
btnAdd = Button(calc, text="+", width=6, bd=8, fg="black", command = lambda : added_value.operation("Add")).grid(row=4, column=4)

btnSqrt = Button(calc, text="√", width=6, bd=8, fg="black", command = added_value.sqrt).grid(row=5, column=0)
btnZero = Button(calc, text="0", width=6, bd=8, fg="black", command = lambda : added_value.operation(0)).grid(row=5, column=1)
btnDot = Button(calc, text=".", width=6, bd=8, fg="black", command = lambda : added_value.operation(".")).grid(row=5, column=2)
btnPM = Button(calc, text=chr(177), width=6, bd=8, fg="black", command = added_value.PM).grid(row=5, column=3)
btnEquals = Button(calc, text="=", width=6, bd=8, fg="black", command = added_value.sum_of_total).grid(row=5, column=4)

btnSin = Button(calc, text="sin", width=6, bd=8, fg="black", command = added_value.sin).grid(row=6, column=0)
btnCos = Button(calc, text="cos", width=6, bd=8, fg="black", command = added_value.cos).grid(row=6, column=1)
btnTan = Button(calc, text="tan", width=6, bd=8, fg="black", command = added_value.tan).grid(row=6, column=2)
btnMod = Button(calc, text="Mod", width=6, bd=8, fg="black", command = lambda :added_value.operation("Mod")).grid(row=6, column=3)
btnDegrees = Button(calc, text="Degrees", width=6, bd=8, fg="black", command = added_value.degrees).grid(row=6, column=4)

btnSinh = Button(calc, text="sinh", width=6, bd=8, fg="black", command = added_value.sinh).grid(row=7, column=0)
btnCosh = Button(calc, text="cosh", width=6, bd=8, fg="black", command = added_value.cosh).grid(row=7, column=1)
btnTanh = Button(calc, text="tanh", width=6, bd=8, fg="black", command = added_value.tanh).grid(row=7, column=2)
btnLog10 = Button(calc, text="log10", width=6, bd=8, fg="black", command = added_value.log10).grid(row=7, column=3)
btnLog2 = Button(calc, text="log2", width=6, bd=8, fg="black", command = added_value.log2).grid(row=7, column=4)

btnFactorial = Button(calc, text="x!", width=6, bd=8, fg="black", command = added_value.factorial).grid(row=8, column=0)
btnQubic = Button(calc, text="x^3", width=6, bd=8, fg="black", command = added_value.pow).grid(row=8, column=1)
btnExp = Button(calc, text="Exp", width=6, bd=8, fg="black", command = added_value.exp).grid(row=8, column=2)
btnAns = Button(calc, text="Ans", width=6, bd=8, fg="black", command = added_value.sum_of_total).grid(row=8, column=3)
btnLog = Button(calc, text="log", width=6, bd=8, fg="black", command = added_value.log).grid(row=8, column=4)
#====================================================================================================


root.mainloop()