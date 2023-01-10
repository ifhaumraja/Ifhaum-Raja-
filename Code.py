from tkinter import *
import random
import time;
import datetime
from tkinter import messagebox

root = Tk()
root.geometry("1350x700+0+0")
root.title("COFFEE")
root.configure(background='black')
root.state('zoomed')
Tops = Frame(root, width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=100, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)
ft2 = Frame(f2, width=440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=450, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)
f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

# Functions for Buttons

# Function to check if the user input is empty and give it value of zero
def chkForNull(food):
    if food == "":
        return "0"
    else:
        return food

# Function to calculate the cost of the food
def CostofItem():
    Item1 = float(chkForNull(E_Latte.get()))
    Item2 = float(chkForNull(E_Espresso.get()))
    Item3 = float(chkForNull(E_Iced_Latte.get()))
    Item4 = float(chkForNull(E_Vale_Coffee.get()))
    Item5 = float(chkForNull(E_Cappucino.get()))
    Item6 = float(chkForNull(E_African_Coffee.get()))
    Item7 = float(chkForNull(E_American_Coffee.get()))
    Item8 = float(chkForNull(E_Iced_Cappucino.get()))
    Item9 = float(chkForNull(E_Coffee_Cake.get()))
    Item10 = float(chkForNull(E_Red_Velvet_Cake.get()))
    Item11 = float(chkForNull(E_Black_Forest_Cake.get()))
    Item12 = float(chkForNull(E_Boston_Cream_Cake.get()))
    Item13 = float(chkForNull(E_Lagos_Chocolate_Cake.get()))
    Item14 = float(chkForNull(E_Kilburn_Chocolate_Cake.get()))
    Item15 = float(chkForNull(E_Carlton_Hill_Cake.get()))
    Item16 = float(chkForNull(E_Queen_Park_Chocolate_Cake.get()))
    
    # Equation for Cost
    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) \
    + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) \
    + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)
    
    DrinksPrice = "$ " + str('%.2f'%(PriceofDrinks))
    CostofDrinks.set(DrinksPrice)

    CakesPrice = "$ " + str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakesPrice)
   
    SC="$ " + str('%.2f'%(10))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "$ " + str('%.2f'%(PriceofDrinks + PriceofCakes + 10))
    SubTotal.set(SubTotalofITEMS)

    Tax= "$ " + str('%.2f'%((PriceofDrinks + PriceofCakes + 10) *0.12))
    PaidTax.set(Tax)

    TC= "$ "+ str('%.2f'%((PriceofDrinks + PriceofCakes + 10)+(PriceofDrinks + PriceofCakes +10) *0.12))
    TotalCost.set(TC)

# Function to display receipt
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL# " + randomRef)

    Item1 = float(chkForNull(E_Latte.get()))
    Item2 = float(chkForNull(E_Espresso.get()))
    Item3 = float(chkForNull(E_Iced_Latte.get()))
    Item4 = float(chkForNull(E_Vale_Coffee.get()))
    Item5 = float(chkForNull(E_Cappucino.get()))
    Item6 = float(chkForNull(E_African_Coffee.get()))
    Item7 = float(chkForNull(E_American_Coffee.get()))
    Item8 = float(chkForNull(E_Iced_Cappucino.get()))
    Item9 = float(chkForNull(E_Coffee_Cake.get()))
    Item10 = float(chkForNull(E_Red_Velvet_Cake.get()))
    Item11 = float(chkForNull(E_Black_Forest_Cake.get()))
    Item12 = float(chkForNull(E_Boston_Cream_Cake.get()))
    Item13 = float(chkForNull(E_Lagos_Chocolate_Cake.get()))
    Item14 = float(chkForNull(E_Kilburn_Chocolate_Cake.get()))
    Item15 = float(chkForNull(E_Carlton_Hill_Cake.get()))
    Item16 = float(chkForNull(E_Queen_Park_Chocolate_Cake.get()))
    
    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ Receipt_Ref.get()+'\t\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items:\t\t\t' + "Qty:\t"+ "Price:\t"+ "Subtotal\n\n")
    txtReceipt.insert(END, 'Latte:\t\t\t' + E_Latte.get() + "\t1.20\t" + str('%.2f'%(Item1 * 1.2)) + "\n")
    txtReceipt.insert(END, 'Espresso:\t\t\t' + E_Espresso.get() + "\t1.99\t" + str('%.2f'%(Item2 * 1.99)) + "\n")
    txtReceipt.insert(END, 'Iced Latte:\t\t\t' + E_Iced_Latte.get() + "\t2.05\t" + str('%.2f'%(Item3 * 2.05)) + "\n")
    txtReceipt.insert(END, 'Vale Coffee:\t\t\t' + E_Vale_Coffee.get() + "\t1.89\t" + str('%.2f'%(Item4 * 1.89)) + "\n")
    txtReceipt.insert(END, 'Cappucino:\t\t\t' + E_Cappucino.get() + "\t1.99\t" + str('%.2f'%(Item5 * 1.99)) + "\n")
    txtReceipt.insert(END, 'African Coffee:\t\t\t' + E_African_Coffee.get() + "\t2.99\t" + str('%.2f'%(Item6 * 2.99)) + "\n")
    txtReceipt.insert(END, 'American Coffee:\t\t\t' + E_American_Coffee.get() + "\t2.39\t" + str('%.2f'%(Item7 * 2.39)) + "\n")
    txtReceipt.insert(END, 'Iced Cappucino:\t\t\t' + E_Iced_Cappucino.get() + "\t1.29\t" + str('%.2f'%(Item8 * 1.29)) + "\n")
    txtReceipt.insert(END, 'Coffee Cake:\t\t\t' + E_Coffee_Cake.get() + "\t1.35\t" + str('%.2f'%(Item9 * 1.35)) + "\n")
    txtReceipt.insert(END, 'Red Velvet Cake:\t\t\t' + E_Red_Velvet_Cake.get() + "\t2.20\t" + str('%.2f'%(Item10 * 2.2)) + "\n")
    txtReceipt.insert(END, 'Black Forest Cake:\t\t\t' + E_Black_Forest_Cake.get() + "\t1.99\t" + str('%.2f'%(Item11 * 1.99)) + "\n")
    txtReceipt.insert(END, 'Boston Cream Cake:\t\t\t' + E_Boston_Cream_Cake.get() + "\t1.49\t" + str('%.2f'%(Item12 * 1.49)) + "\n")
    txtReceipt.insert(END, 'Lagos Chocolate Cake:\t\t\t' + E_Lagos_Chocolate_Cake.get() + "\t1.80\t" + str('%.2f'%(Item13 * 1.8)) + "\n")
    txtReceipt.insert(END, 'Kilburn Chocolate Cake:\t\t\t' + E_Kilburn_Chocolate_Cake.get() + "\t1.67\t" + str('%.2f'%(Item14 * 1.67)) + "\n")
    txtReceipt.insert(END, 'Carlton Hill Choco Cake:\t\t\t' + E_Carlton_Hill_Cake.get() + "\t1.60\t" + str('%.2f'%(Item15 * 1.60)) + "\n")
    txtReceipt.insert(END, 'Queen Park Choco Cake:\t\t\t' + E_Queen_Park_Chocolate_Cake.get() + "\t1.99\t" + str('%.2f'%(Item16 * 1.99)) + "\n")
    txtReceipt.insert(END, 'Costs of Drinks:\t\t' + CostofDrinks.get() + '\tVAT:\t\t' + PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Costs of Cakes:\t\t' + CostofCakes.get() + '\tSubTotal:\t\t' + SubTotal.get()+"\n")
    txtReceipt.insert(END, 'ServiceCharge:\t\t' + ServiceCharge.get() + '\tTotal Cost:\t\t' + TotalCost.get()+"\n")

# Function to exit the program
def qExit():
        qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
        if qExit > 0:
            root.destroy()
            return

# Function to reset all text fields and receipt
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latte.set("")
    E_Espresso.set("")
    E_Iced_Latte.set("")
    E_Vale_Coffee.set("")
    E_Cappucino.set("")
    E_African_Coffee.set("")
    E_American_Coffee.set("")
    E_Iced_Cappucino.set("")
    E_Coffee_Cake.set("")
    E_Red_Velvet_Cake.set("")
    E_Black_Forest_Cake.set("")
    E_Boston_Cream_Cake.set("")
    E_Lagos_Chocolate_Cake.set("")
    E_Kilburn_Chocolate_Cake.set("")
    E_Carlton_Hill_Cake.set("")
    E_Queen_Park_Chocolate_Cake.set("")

# Body
lblInfo = Label(Tops, font=('arial', 70, 'bold'), text="   IFHAUM RAJA MINI HOTEL  \t", bd=10)
lblInfo.grid(row=0, column=0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()
E_Latte = StringVar()
E_Espresso = StringVar()
E_Iced_Latte = StringVar()
E_Vale_Coffee = StringVar()
E_Cappucino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappucino = StringVar()
E_Coffee_Cake = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Black_Forest_Cake = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()
E_Latte.set("")
E_Espresso.set("")
E_Iced_Latte.set("")
E_Vale_Coffee.set("")
E_Cappucino.set("")
E_African_Coffee.set("")
E_American_Coffee.set("")
E_Iced_Cappucino.set("")
E_Coffee_Cake.set("")
E_Red_Velvet_Cake.set("")
E_Black_Forest_Cake.set("")
E_Boston_Cream_Cake.set("")
E_Lagos_Chocolate_Cake.set("")
E_Kilburn_Chocolate_Cake.set("")
E_Carlton_Hill_Cake.set("")
E_Queen_Park_Chocolate_Cake.set("")
DateofOrder.set(time.strftime("%d/%m/%Y"))

# Labels (Drinks)
Latte = Label(f1aa, text="Latte \t\t", font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Espresso = Label(f1aa, text="Espresso \t\t", font=('arial', 18, 'bold')).grid(row=1, sticky=W)
Iced_Latte = Label(f1aa, text="Iced Latte \t\t", font=('arial', 18, 'bold')).grid(row=2, sticky=W)
Vale_Coffee = Label(f1aa, text="Vale Coffee \t\t", font=('arial', 18, 'bold')).grid(row=3, sticky=W)
Cappucino = Label(f1aa, text="Cappucino \t\t", font=('arial', 18, 'bold')).grid(row=4, sticky=W)
African_Coffee = Label(f1aa, text="African Coffee \t\t", font=('arial', 18, 'bold')).grid(row=5, sticky=W)
American_Coffee = Label(f1aa, text="American Coffee \t\t", font=('arial', 18, 'bold')).grid(row=6, sticky=W)
Iced_Cappucino = Label(f1aa, text="Iced Cappucino \t\t", font=('arial', 18, 'bold')).grid(row=7, sticky=W)

# Labels (Cakes)
CoffeeCake = Label(f1ab, text=" Coffee Cake\t", font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Red_Velvet_Cake = Label(f1ab, text=" Red Velvet Cake\t", font=('arial', 18, 'bold')).grid(row=1, sticky=W)
Black_Forest_Cake = Label(f1ab, text=" Black Forest Cake\t", font=('arial', 18, 'bold')).grid(row=2, sticky=W)
Boston_Cream_Cake = Label(f1ab, text=" Boston Cream Cake\t", font=('arial', 18, 'bold')).grid(row=3, sticky=W)
Lagos_Chocolate_Cake = Label(f1ab, text=" Lagos Chocolate Cake\t", font=('arial', 18, 'bold')).grid(row=4, sticky=W)
Kilburn_Chocolate_Cake = Label(f1ab, text=" Kilburn Chocolate Cake       ", font=('arial', 18, 'bold')).grid(row=5, sticky=W)
Carlton_Hill_Cake = Label(f1ab, text=" Carlton Hill Cake\t", font=('arial', 18, 'bold')).grid(row=6, sticky=W)
Queen_Park_Cake = Label(f1ab, text=" Queen's Park Cake\t", font=('arial', 18, 'bold')).grid(row=7, sticky=W)

# Textbox(Drinks)
txtLatte = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Latte, state=NORMAL)
txtEspresso = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Espresso, state=NORMAL)
txtIced_Latte = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Iced_Latte, state=NORMAL)
txtVale_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Vale_Coffee, state=NORMAL)
txtCappucino = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Cappucino, state=NORMAL)
txtAfrican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_African_Coffee, state=NORMAL)
txtAmerican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_American_Coffee, state=NORMAL)
txtIced_Cappucino = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Iced_Cappucino, state=NORMAL)

txtLatte.grid(row=0, column=1)
txtEspresso.grid(row=1, column=1)
txtIced_Latte.grid(row=2, column=1)
txtVale_Coffee.grid(row=3, column=1)
txtCappucino.grid(row=4, column=1)
txtAfrican_Coffee.grid(row=5, column=1)
txtAmerican_Coffee.grid(row=6, column=1)
txtIced_Cappucino.grid(row=7, column=1)

# Textbox(Cakes)
txtCoffee_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Coffee_Cake, bd=8, width=6, justify='left', state=NORMAL)
txtRed_Velvet_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Red_Velvet_Cake, bd=8, width=6, justify='left', state=NORMAL)
txtBlack_Forest_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Black_Forest_Cake, bd=8, width=6, justify='left', state=NORMAL)
txtBoston_Cream_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Boston_Cream_Cake, bd=8, width=6, justify='left', state=NORMAL)
txtLagos_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Lagos_Chocolate_Cake, bd=8, width=6, justify='left', state=NORMAL)
txtKilburn_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Kilburn_Chocolate_Cake, bd=7, width=6, justify='left', state=NORMAL)
txtCarlton_Hill_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Carlton_Hill_Cake, bd=8, width=6, justify='left', state=NORMAL)
txtQueen_Park_Cake = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=E_Queen_Park_Chocolate_Cake, bd=8, width=6, justify='left', state=NORMAL)

txtCoffee_Cake.grid(row=0, column=1)
txtRed_Velvet_Cake.grid(row=1, column=1)
txtBlack_Forest_Cake.grid(row=2, column=1)
txtBoston_Cream_Cake.grid(row=3, column=1)
txtLagos_Chocolate_Cake.grid(row=4, column=1)
txtKilburn_Chocolate_Cake.grid(row=5, column=1)
txtCarlton_Hill_Cake.grid(row=6, column=1)
txtQueen_Park_Cake.grid(row=7, column=1)

# Receipt Information Display
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt.grid(row=1, column=0)

# Buttons
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 12, 'bold'), width=6, text="Total", command=CostofItem).grid(row=0, column=0)
btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 12, 'bold'), width=6, text="Receipt",command= Receipt).grid(row=0, column=1)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 12, 'bold'), width=6, text="Reset", command=Reset).grid(row=0, column=2)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 12, 'bold'), width=5, text="Exit", command=qExit).grid(row=0, column=3)

# Item Cost Information
lblCostofDrinks = Label(f2aa, font=('arial', 16, 'bold'), text="Cost of Drinks \t", bd=8, anchor='w')
txtCostofDrinks = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=CostofDrinks)
lblCostofCakes = Label(f2aa, font=('arial', 16, 'bold'), text="Cost of Cakes", bd=8, anchor='w')
txtCostofCakes = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=CostofCakes)
lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text="Service Charge", bd=8, anchor='w')
txtServiceCharge = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=ServiceCharge)

lblCostofDrinks.grid(row=2, column=0, sticky=W)
txtCostofDrinks.grid(row=2, column=1)
lblCostofCakes.grid(row=3, column=0, sticky=W)
txtCostofCakes.grid(row=3, column=1)
lblServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge.grid(row=4, column=1)

CostofDrinks.set("")
CostofCakes.set("")

# Payment Information
lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text="V.A.Tax", bd=8)
txtPaidTax = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=PaidTax)
lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text="Sub Total", bd=8)
txtSubTotal = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=SubTotal)
lblTotalCost = Label(f2ab, font=('arial', 16, 'bold'), text="Total", bd=8)
txtTotalCost = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=TotalCost)

lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax.grid(row=2, column=1)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal.grid(row=3, column=1)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost.grid(row=4, column=1)

# Main
root.mainloop()
