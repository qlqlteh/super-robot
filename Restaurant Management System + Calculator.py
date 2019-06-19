from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input=StringVar()
operator = ""

Tops = Frame(root, width = 1600, height = 50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
#====================================Time============================
localtime=time.asctime(time.localtime(time.time()))
#====================================Info============================
lblInfo = Label(Tops, font=('arial', 40, 'bold'), text="Choindian Restaurant Management Systems", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)
#====================================Calculator======================
def btnClick(numbers):
    global operator
    operator = operator+ str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(129086, 508763)
    randomRef = str(x)
    rand.set(randomRef)

    CoM = float(Masala.get())
    CoK = float(Korma.get())
    CoP = float(Palak.get())
    CoT = float(Tandoori.get())
    CoN = float(Naan.get())
    CoL= float(Lassi.get())

    CostofMasala = CoM * 7.99
    CostofKorma = CoK * 6.99
    CostofPalak = CoP * 8.99
    CostofTandoori = CoT * 12.99
    CostofNaan = CoN * 2.99
    CostofLassi = CoL * 5.99

    CostofMeal = "£", str('%.2f'% (CostofMasala + CostofKorma + CostofPalak + CostofTandoori + CostofNaan + CostofLassi))
    PayTax = ((CostofMasala + CostofKorma + CostofPalak + CostofTandoori + CostofNaan + CostofLassi) * 0.2)
    TotalCost = (CostofMasala + CostofKorma + CostofPalak + CostofTandoori + CostofNaan + CostofLassi)
    Ser_Charge = ((CostofMasala + CostofKorma + CostofPalak + CostofTandoori + CostofNaan + CostofLassi)/99)
    Service = "£", str('%.2f' % Ser_Charge)
    OverAllCost = "£", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax= "£", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set("")
    rand.set("")
    Masala.set("")
    Korma.set("")
    Palak.set("")
    Tandoori.set("")
    Naan.set("")
    Lassi.set("")
    Service_Charge.set("")
    Cost.set("")
    Tax.set("")
    SubTotal.set("")
    Total.set("")

txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg='powder blue', justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7", bg="powder blue", command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8", bg="powder blue", command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9", bg="powder blue", command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+", bg="powder blue", command=lambda:btnClick("+")).grid(row=2,column=3)
#----------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4", bg="powder blue", command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5", bg="powder blue", command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6", bg="powder blue", command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-", bg="powder blue", command=lambda:btnClick("-")).grid(row=3,column=3)
#----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1", bg="powder blue", command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2", bg="powder blue", command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3", bg="powder blue", command=lambda:btnClick(3)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*", bg="powder blue", command=lambda:btnClick("*")).grid(row=4,column=3)
#----------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0", bg="powder blue", command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C", bg="powder blue", command=btnClearDisplay).grid(row=5,column=1)
btnEqual=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=", bg="powder blue", command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/", bg="powder blue", command=lambda:btnClick("/")).grid(row=5,column=3)
#--------------------------------------Restaurant Info 1--------------------------------------------------------
rand = StringVar()
Masala = StringVar()
Korma = StringVar()
Palak = StringVar()
Tandoori = StringVar()
Naan = StringVar()
Lassi = StringVar()
Service_Charge = StringVar()
Cost = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

lblReference = Label(f1,font=('arial',16,'bold'),text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtReference.grid(row=0,column=1)

lblMasala = Label(f1,font=('arial',16,'bold'),text="Tikka Masala", bd=16, anchor='w')
lblMasala.grid(row=1,column=0)
txtMasala=Entry(f1,font=('arial',16,'bold'),textvariable=Masala, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtMasala.grid(row=1,column=1)

lblKorma = Label(f1,font=('arial',16,'bold'),text="Korma", bd=16, anchor='w')
lblKorma.grid(row=2,column=0)
txtKorma=Entry(f1,font=('arial',16,'bold'),textvariable=Korma, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtKorma.grid(row=2,column=1)

lblPalak = Label(f1,font=('arial',16,'bold'),text="Palak Paneer", bd=16, anchor='w')
lblPalak.grid(row=3,column=0)
txtPalak=Entry(f1,font=('arial',16,'bold'),textvariable=Palak, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtPalak.grid(row=3,column=1)

lblTandoori = Label(f1,font=('arial',16,'bold'),text="Tandoori Chicken", bd=16, anchor='w')
lblTandoori.grid(row=4,column=0)
txtTandoori=Entry(f1,font=('arial',16,'bold'),textvariable=Tandoori, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtTandoori.grid(row=4,column=1)

lblNaan = Label(f1,font=('arial',16,'bold'),text="Naan", bd=16, anchor='w')
lblNaan.grid(row=5,column=0)
txtNaan=Entry(f1,font=('arial',16,'bold'),textvariable=Naan, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtNaan.grid(row=5,column=1)

#-------------------------------Restaurant Info 2---------------------------

lblLassi = Label(f1,font=('arial',16,'bold'),text="Lassi", bd=16, anchor='w')
lblLassi.grid(row=0,column=2)
txtLassi=Entry(f1,font=('arial',16,'bold'),textvariable=Lassi, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtLassi.grid(row=0,column=3)

lblCost = Label(f1,font=('arial',16,'bold'),text="Cost", bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('arial',16,'bold'),text="Service", bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtService.grid(row=2,column=3)

lblTax = Label(f1,font=('arial',16,'bold'),text="Tax", bd=16, anchor='w')
lblTax.grid(row=3,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtTax.grid(row=3,column=3)

lblSubTotal = Label(f1,font=('arial',16,'bold'),text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial',16,'bold'),text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=Total, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtTotalCost.grid(row=5,column=3)

#--------------------------------Buttons----------------------------------
btnTotal=Button(f1, padx=16, pady=8, bd=16, fg="black",font=('arial',16,'bold'), width=10, text="Total", bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset=Button(f1, padx=16, pady=8, bd=16, fg="black",font=('arial',16,'bold'), width=10, text="Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit=Button(f1, padx=16, pady=8, bd=16, fg="black",font=('arial',16,'bold'), width=10, text="Exit", bg="powder blue", command=qExit).grid(row=7, column=3)

root.mainloop()