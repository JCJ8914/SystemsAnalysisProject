from cgitb import reset
from ctypes.wintypes import HDC
from email.headerregistry import Address
from sqlite3 import Date
from tkinter import*
import tkinter.messagebox
import time
import datetime
from datetime import datetime
import tkinter
from turtle import back
from numpy import pad
import random

import backend

root = Tk()

MainFrame = Frame(root)
MainFrame.grid()

TopFrame = Frame(MainFrame, bd=10, width=1350, height=550, padx=2, relief=RIDGE)
TopFrame.pack(side=TOP)

LeftFrame = Frame(TopFrame, bd=5, width=400, height=550, relief=RIDGE)
LeftFrame.pack(side=LEFT)
RightFrame = Frame(TopFrame, bd=5, width=820, height=550, relief=RIDGE)
RightFrame.pack(side=RIGHT)


RightFrame1 = Frame(RightFrame, bd=5, width=800, height=50, padx=10, relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=5, width=800, height=100, padx=3, relief=RIDGE)
RightFrame2.grid(row=1, column=0)

RightFrame3 = Frame(RightFrame, bd=5, width=800, height=400, padx=4, relief=RIDGE)
RightFrame3.grid(row=3, column=0)

BottomFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=2, relief=RIDGE)
BottomFrame.pack(side=BOTTOM)

global cd

CusID = StringVar()
FirstName = StringVar()
LastName = StringVar()
Contact = StringVar()
CusAddress = StringVar()
Room = StringVar()

NoOfDays = StringVar()
SubTotal = StringVar()
PaidTax = StringVar()

DateIn = StringVar()
DateOut = StringVar()
TotalDays = StringVar()

DateIn.set(time.strftime("%d/%m/%Y"))
DateOut.set(time.strftime("%d/%m/%Y"))

rand = random.randint(1190, 8000)
randomReference = str(rand)
CusID.set(randomReference)

def iExit():
    iExit = tkinter.messagebox.askyesno("Management System", "Confirm if you want to exit.")
    if iExit > 0:
        root.destroy()
        return

def reset():

    root.txtCusID.delete(0,END)
    root.txtFirstname.delete(0,END)
    root.txtSurname.delete(0,END)
    root.txtContact.delete(0,END)
    root.txtAddress.delete(0,END)
    root.txtAddress.delete(0,END)
    root.txtCheckin.delete(0,END)
    root.txtCheckout.delete(0,END)

    DateIn.set(time.strftime("%d/%m/%Y"))
    DateOut.set(time.strftime("%d/%m/%Y"))

    rand = random.randint(1190, 8000)
    randomReference = str(rand)
    CusID.set(randomReference)

def add():

    if(len(CusID.get()) != 0):
        backend.addData(CusID.get(), FirstName.get(), LastName.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get())
        lstReso.delete(0,END)
        lstReso.insert(END, (CusID.get(), FirstName.get(), LastName.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get()))

def delete():
    if(len(CusID.get()) != 0):
        backend.deleteData(cd[0])
        reset()
        display()

def display():

    lstReso.delete(0,END)
    for row in backend.viewData():
        lstReso.insert(END, row, str("")) 

def search():

    lstReso.delete(0,END)
    for row in backend.searchData(CusID.get(), FirstName.get(), LastName.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get()):
        lstReso.insert(END, row, str(""))

def update():

    if(len(CusID.get()) != 0):
        backend.deleteData(cd[0])
    if(len(CusID.get()) != 0):
        backend.addData(CusID.get(), FirstName.get(), LastName.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get())
        lstReso.delete(0,END)
        lstReso.insert(END, (CusID.get(), FirstName.get(), LastName.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get()))

def records():

    global cd
    searchcdb = lstReso.curselection() [0]
    cd = lstReso.get(searchcdb)

    root.txtCusID.delete(0,END)
    root.txtCusID.insert(END,cd[1])
    root.txtFirstname.delete(0,END)
    root.txtFirstname.insert(END,cd[2])
    root.txtSurname.delete(0,END)
    root.txtSurname.insert(END,cd[3])
    root.txtContact.delete(0,END)
    root.txtContact.insert(END,cd[4])
    root.txtAddress.delete(0,END)
    root.txtAddress.insert(END,cd[5])
    root.txtRoom.delete(0,END)
    root.txtRoom.insert(END,cd[6])
    root.txtCheckin.delete(0,END)
    root.txtCheckin.insert(END,cd[7])
    root.txtCheckout.delete(0,END)
    root.txtCheckout.insert(END,cd[8])

def totalcostadddata():
    InDate = DateIn.get() 
    OutDate = DateOut.get()
    Indate = datetime.strptime(InDate, "%d/%m/%Y")
    Outdate = datetime.strptime(OutDate, "%d/%m/%Y")
    TotalDays.set(abs((Outdate - Indate).days))

    


#=======================================LEFT WIDGETS==================================================
root.lblCusID = Label(LeftFrame, font=('arial', 12,'bold'), text="Customer No:", padx=1)
root.lblCusID.grid(row=0, column=0, sticky =W)
root.txtCusID =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=CusID)
root.txtCusID.grid(row=0, column=1, pady=3, padx=20)

root.lblFirstname = Label(LeftFrame, font=('arial', 12,'bold'), text="First Name:", padx=1)
root.lblFirstname.grid(row=1, column=0, sticky =W)
root.txtFirstname =Entry(LeftFrame, font=('arial',12,'bold',) ,width =18, textvariable=FirstName)
root.txtFirstname.grid(row=1, column=1, pady=3, padx=20)

root.lblSurname = Label(LeftFrame, font=('arial', 12,'bold'), text="Surname:", padx=1)
root.lblSurname.grid(row=2, column=0, sticky =W)
root.txtSurname =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=LastName)
root.txtSurname.grid(row=2, column=1, pady=3, padx=20)

root.lblContact = Label(LeftFrame, font=('arial', 12,'bold'), text="Contact No:", padx=1)
root.lblContact.grid(row=3, column=0, sticky =W)
root.txtContact =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=Contact)
root.txtContact.grid(row=3, column=1, pady=3, padx=20)

root.lblAddress = Label(LeftFrame, font=('arial', 12,'bold'), text="Address:", padx=1)
root.lblAddress.grid(row=4, column=0, sticky =W)
root.txtAddress =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=CusAddress)
root.txtAddress.grid(row=4, column=1, pady=3, padx=20)

root.lblRoom = Label(LeftFrame, font=('arial', 12,'bold'), text="Room No:", padx=1)
root.lblRoom.grid(row=5, column=0, sticky =W)
root.txtRoom =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=Room)
root.txtRoom.grid(row=5, column=1, pady=3, padx=20)

root.lblCheckin = Label(LeftFrame, font=('arial', 12,'bold'), text="Check In Date:", padx=1)
root.lblCheckin.grid(row=6, column=0, sticky =W)
root.txtCheckin =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=DateIn)
root.txtCheckin.grid(row=6, column=1, pady=3, padx=20)

root.lblCheckout = Label(LeftFrame, font=('arial', 12,'bold'), text="Check Out Date:", padx=1)
root.lblCheckout.grid(row=7, column=0, sticky =W)
root.txtCheckout =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=DateOut)
root.txtCheckout.grid(row=7, column=1, pady=3, padx=20)

#=======================================RIGHT WIDGETS==================================================
root.lblLabel = Label(RightFrame1, font=('arial', 9,'bold'), padx=6, pady=10, text="Customer No\tFirstname\t Surname \t Contact No \t Address \t Room Num \tCheck In Date\t Check Out Date")
root.lblLabel.grid(row=0, column=0, columnspan=17)

scrollbar= Scrollbar(RightFrame2)
scrollbar.grid(row=0, column=0,sticky='ns')
lstReso = Listbox(RightFrame2, width=103, height=14, font=('arial', 9, 'bold'), yscrollcommand= scrollbar.set)
lstReso.bind('<<ListboxSelct>>')
lstReso.grid(row=0, column=0, padx=7, sticky= 'nsew')
scrollbar.config(command = lstReso.xview)
#=======================================RIGHT WIDGETS==================================================
root.lblDays = Label(RightFrame3, font=('arial', 12,'bold'), text="No. of Days:", padx=2, pady=2)
root.lblDays.grid(row=0, column=0, sticky =W)
root.txtDays =Entry(RightFrame3, font=('arial',12,'bold') ,width =76, textvariable=TotalDays)
root.txtDays.grid(row=0, column=1, pady=3, padx=20)

root.lblPaid = Label(RightFrame3, font=('arial', 12,'bold'), text="Amount Paid:", padx=2, pady=2)
root.lblPaid.grid(row=1, column=0, sticky =W)
root.txtPaid =Entry(RightFrame3, font=('arial',12,'bold') ,width =76)
root.txtPaid.grid(row=1, column=1, pady=3, padx=20)

root.lblTotal = Label(RightFrame3, font=('arial', 12,'bold'), text="Total Cost:", padx=2, pady=2)
root.lblTotal.grid(row=2, column=0, sticky =W)
root.txtTotal =Entry(RightFrame3, font=('arial',12,'bold') ,width =76)
root.txtTotal.grid(row=2, column=1, pady=3, padx=20)
#=======================================WIDGET BUTTONS==================================================

root.btnTotalandAddData = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='AddNew/Total', command=totalcostadddata).grid(row=0, column=0, padx =4,  pady=1)

root.btnDisplay = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='Display', command=display).grid(row=0, column=1, padx =4,  pady=1)

root.btnUpdate = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='Update', command=update).grid(row=0, column=2, padx =4,  pady=1)

root.btnDelete = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='Delete', command=delete).grid(row=0, column=3, padx =4,  pady=1)

root.btnSearch = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='Search', command=search).grid(row=0, column=4, padx =4,  pady=1)

root.btnReset = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='Reset', command=reset).grid(row=0, column=5, padx =4,  pady=1)

root.btnExit = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
width=13, height=2, text='Exit', command=iExit).grid(row=0, column=6, padx =4,  pady=1)


root.mainloop()