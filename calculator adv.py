from tkinter import *
import math
import tkinter.messagebox

root=Tk()
root.geometry("650x400+300+300")
root.title("CALCULATOR")

def btn1():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'1')

def btn2():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'2')

def btn3():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'3')

def btn4():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'4')

def btn5():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'5')

def btn6():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'6')


def btn7():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'7')

def btn8():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'8')

def btn9():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'9')

def btn0():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'0')



def btn_sum():
    x=len(disp.get())
    disp.insert(x,'+')
    
def btn_sub():
    x=len(disp.get())
    disp.insert(x,'-')

def btn_mul():
    x=len(disp.get())
    disp.insert(x,'*')

def btn_div():
    x=len(disp.get())
    disp.insert(x,'/')

def pow():
    x=len(disp.get())
    disp.insert(x,'**')

def brc_r():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,')')

def brc_l():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'(')

    
def eq():
    try:
        ans=disp.get()
        ans=eval(ans)
        disp.delete(0,END)
        disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR")

def sq_rt():
    if disp.get()=='0':
        disp.delete(0,END)
    x=len(disp.get())
    disp.insert(x,'**0.5')

   
        
            
   


    
        




disp=Entry(root,font="verdana 20",fg="Black",bg="mistyrose",justify=RIGHT)
disp.insert(0,'0')
disp.pack(expand=TRUE,fill=BOTH)
row1=Frame(root)
row1.pack(expand=TRUE,fill=BOTH)
sum=Button(row1,text="+",command=btn_sum).pack(side=LEFT,expand=TRUE,fill=BOTH)
sub=Button(row1,text="-",command=btn_sub).pack(side=LEFT,expand=TRUE,fill=BOTH)
mul=Button(row1,text="*",command=btn_mul).pack(side=LEFT,expand=TRUE,fill=BOTH)
div=Button(row1,text="/",command=btn_div).pack(side=LEFT,expand=TRUE,fill=BOTH)
exp=Button(row1,text="^",command=pow).pack(side=LEFT,expand=TRUE,fill=BOTH)
sqrt=Button(row1,text="sqrt",command=sq_rt).pack(side=LEFT,expand=TRUE,fill=BOTH)


row2=Frame(root)
row2.pack(expand=TRUE,fill=BOTH)
num1=Button(row2,text="1",command=btn1).pack(side=LEFT,expand=TRUE,fill=BOTH)
num2=Button(row2,text="2",command=btn2).pack(side=LEFT,expand=TRUE,fill=BOTH)
num3=Button(row2,text="3",command=btn3).pack(side=LEFT,expand=TRUE,fill=BOTH)
num4=Button(row2,text="4",command=btn4).pack(side=LEFT,expand=TRUE,fill=BOTH)
num5=Button(row2,text="5",command=btn5).pack(side=LEFT,expand=TRUE,fill=BOTH)

row3=Frame(root)
row3.pack(expand=TRUE,fill=BOTH)
num6=Button(row3,text="6",command=btn6).pack(side=LEFT,expand=TRUE,fill=BOTH)
num7=Button(row3,text="7",command=btn7).pack(side=LEFT,expand=TRUE,fill=BOTH)
num8=Button(row3,text="8",command=btn8).pack(side=LEFT,expand=TRUE,fill=BOTH)
num9=Button(row3,text="9",command=btn9).pack(side=LEFT,expand=TRUE,fill=BOTH)
num0=Button(row3,text="0",command=btn0).pack(side=LEFT,expand=TRUE,fill=BOTH)

row4=Frame(root)
row4.pack(expand=TRUE,fill=BOTH)
par1=Button(row4,text="(",command=brc_l).pack(side=LEFT,expand=TRUE,fill=BOTH)
par2=Button(row4,text=")",command=brc_r).pack(side=LEFT,expand=TRUE,fill=BOTH)
eq=Button(row4,text="=",command=eq).pack(side=LEFT,expand=TRUE,fill=BOTH)




root.mainloop()
