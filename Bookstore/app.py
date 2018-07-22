""" A book store application. """
from tkinter import *

WINDOW = Tk()

def conv():
    """ Converts kg to the required units. """
    kilos = float(E2_VAL.get())
    grams = kilos * 1000
    pound = kilos * 2.202462
    ounce = kilos * 35.274
    T1.delete("1.0", END)
    T1.insert(END, grams)
    T2.delete("1.0", END)
    T2.insert(END, pound)
    T3.delete("1.0", END)
    T3.insert(END, ounce)

L1 = Label(WINDOW, text='KG')
L1.grid(row=0, column=0)

E2_VAL = StringVar()
E2 = Entry(WINDOW, textvariable=E2_VAL)
E2.grid(row=0, column=1)

B1 = Button(WINDOW, text='convert', command=conv)
B1.grid(row=0, column=2)

T1 = Text(WINDOW, height=1, width=20)
T1.grid(row=1, column=0)

T2 = Text(WINDOW, height=1, width=20)
T2.grid(row=1, column=1)

T3 = Text(WINDOW, height=1, width=20)
T3.grid(row=1, column=2)

WINDOW.mainloop()
