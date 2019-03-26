#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:29:56 2019

@author: vol35098
"""

import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Entry, Label, Button
from random import randint
dobre = 0
celkem = 0
vysledek = 0

class Application(tk.Tk):
    name = 'Výpočet'
    
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        
        
        ###------FUNKCE------###
        self.funkceFrame = LabelFrame(self, text = "FUNKCE", padx=5, pady=5)
        self.funkceFrame.pack(anchor=tk.W)
        self.znamenkoVar= tk.StringVar()
        self.AVar = tk.StringVar()
        self.BVar = tk.StringVar()
        
        ###
        Radiobutton(self.funkceFrame, text = '+', variable=self.znamenkoVar, value='+', command=self.plus).pack()
        Radiobutton(self.funkceFrame, text = '-', variable=self.znamenkoVar, value='-', command=self.minus).pack()
        Radiobutton(self.funkceFrame, text = '*', variable=self.znamenkoVar, value='*', command=self.krat).pack()
        Radiobutton(self.funkceFrame, text = '/', variable=self.znamenkoVar, value='/', command=self.deleno).pack()
        self.znamenkoVar.set('+')


        #Button(self.funkceFrame, text="Vypočítej", command=self.zkontroluj, width=10).pack()
        #Button(self.funkceFrame,text="zkontroluj", command=self.zkontroluj, width=10).pack()
        
        ###------FUNKCE------###
        
        ###------CISLA------###
        self.cisloFrame = LabelFrame(self,padx=5,pady=5)
        self.cisloFrame.pack(anchor=tk.W)
        ###
        self.cisloA = Entry(self.cisloFrame, state='readonly', width='3', 
                            textvariable=self.AVar)
        self.cisloA.grid(row=4, column=3)
        
        self.znamenko = Label(self.cisloFrame, textvariable=self.znamenkoVar, 
                              width='3')
        self.znamenko.grid(row=4, column=4)
        
        self.cisloB = Entry(self.cisloFrame, state='readonly', width='3', 
                            textvariable=self.BVar)
        self.cisloB.grid(row=4, column=5)
        
        self.rovnitko = Label(self.cisloFrame, text='=', width='3')
        self.rovnitko.grid(row=4, column=6)
        
        self.vysledek = Entry(self.cisloFrame, width='3')
        self.vysledek.grid(row=4, column=7)

        self.lblcor= Label(self.cisloFrame, text="")
        self.lblcor.grid(row=4, column=8)

        self.statistika = Label(self.cisloFrame, text="0/0")
        self.statistika.grid(row=5, column=4)
        
        ###------CISLA------###
        
        ###------HODNOCENI------###
        self.hodnoceFrame = LabelFrame(self, text='HODNOCENÍ', padx=5, pady=5)
        self.funkceFrame.pack(anchor=tk.W)
        ###------HODNOCENI------###
        
        ###------PROMENA pro znaménko------###
        self.znamenkoVar.trace('w', self.plus,)
        
        
   # def zmena(self, x, y, z):
            #pro výpočty
           #print(self.znamenkoVar.get())
    #        pass
         ###------PROMENA pro znaménko------###
    
    
    def plus(self):
        self.cisloA= randint(0, 99)
        self.cisloB= randint(0, 99)
        self.vysledek= self.cisloA+self.cisloB
        print(self.cisloA, "+", self.cisloB, '=', self.vysledek)
        return()
        

    def minus(self):
        self.cisloA= randint(0, 99)
        self.cisloB= randint(0, self.cisloA)
        self.vysledek= self.cisloA-self.cisloB
        print(self.cisloA, "-", self.cisloB, '=', self.vysledek)
        return()
        
        
        
    def deleno(self):
        self.vysledek= randint(0, 9)
        self.cisloB= randint(1, 9)
        self.cisloA= self.cisloB*self.vysledek
        print(self.cisloA, ":", self.cisloB, '=', self.vysledek)
        return()
        
    def krat(self):
        self.cisloA= randint(0, 9)
        self.cisloB= randint(0, 9)
        self.vysledek= self.cisloA*self.cisloB
        print(self.cisloA,"x" , self.cisloB, '=', self.vysledek)
        return()
 
 










app = Application()
app.mainloop()
