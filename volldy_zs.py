#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:03:25 2019

@author: vol35098
"""

import tkinter as tk
from tkinter import Label, LabelFrame, Radiobutton, Entry, Button, END
from random import randint

start = tk.Tk()
start.title("Počítání pro Zš")

dobre=0
celkem=0
vysledek=0
znamenko=tk.StringVar()

#zaklad
znamenka = LabelFrame(start, text="Vyber si znaménko", padx=5, pady=5)
znamenka.grid(row=0)

priklad = LabelFrame(start, text="Příklad", padx=5, pady=5)
priklad.grid(row=1)

statistika = LabelFrame(start, text="Hodnocení", padx=5, pady=5)
statistika.grid(row=2)

novypriklad = LabelFrame(start, padx=5, pady=5)
novypriklad.grid(row=3)

def vyberznamenka():
    selection=str(znamenko.get())
    matematickaoperaceVar.set(selection)
    #novyprikladButt.invoke()

def kontrola(*args):
    global vysledek
    if vysledek == int(vysledekEntry.get()):
        promenaHodnoceni.set(':)')
    else:
        promenaHodnoceni.set(':(')

   

#menu pro znamenka
Radiobutton(znamenka, text="+", value="+", variable=znamenko, command=vyberznamenka).pack()
Radiobutton(znamenka, text="-", value="-", variable=znamenko, command=vyberznamenka).pack()
Radiobutton(znamenka, text="*", value="*", variable=znamenko, command=vyberznamenka).pack()
Radiobutton(znamenka, text="/", value="/", variable=znamenko, command=vyberznamenka).pack()


#přiklad
promenaA=tk.StringVar()
cisloAentry=Entry(priklad, width=4, state="readonly", textvariable=promenaA)
cisloAentry.grid(row=1, column=0)

matematickaoperaceVar=tk.StringVar()
matematickaoperaceVar.set("?")
matematickaoperaceLabel=Label(priklad, textvariable=matematickaoperaceVar)
matematickaoperaceLabel.grid(row=1, column=1)

promenaB=tk.StringVar()
cisloBentry=Entry(priklad, width=4, state="readonly", textvariable=promenaB)
cisloBentry.grid(row=1, column=2)

rovnitkoLabel=Label(priklad, text="=")
rovnitkoLabel.grid(row=1, column=3)

promenaVysledek=tk.StringVar()
vysledekEntry=Entry(priklad, width=4, textvariable=promenaVysledek)
vysledekEntry.grid(row=1, column=4)
vysledekEntry.bind('<Return>', kontrola)

promenaHodnoceni=tk.StringVar()
promenaHodnoceni.set('?')
hodnoceniLabel=Label(statistika, textvariable=promenaHodnoceni)
hodnoceniLabel.grid(row=1, column=0)

vysledek = 0
def priklady(*args):        #*args všechny argumenty ,které nejsou zadané tak jsou vraceny jako pole
                            #proste neomezenej počet argumentů
    global promenaA
    global promenaB
    global vysledek
    if matematickaoperaceVar.get() == "+":
        A = randint(1,10)
        B = randint(1,10)
        vysledek = A + B
        promenaA.set(A)  
        promenaB.set(B)
    if matematickaoperaceVar.get() == "-":
        A = randint(0,99)
        B = randint(0, A)
        vysledek = A - B
        promenaA.set(A)
        promenaB.set(B)
    if matematickaoperaceVar.get() == "*":
        A = randint(1,9)
        B = randint(1,9)
        vysledek = A * B
        promenaA.set(A)
        promenaB.set(B)
    if matematickaoperaceVar.get() == "/":
        A = randint(1 ,9)
        B = randint(1, 9)
        vysledek = A / B
        promenaA.set(A)
        promenaB.set(B)
    print(vysledek)

matematickaoperaceVar.trace("w", priklady )

    
    
    
    
    





start.mainloop()