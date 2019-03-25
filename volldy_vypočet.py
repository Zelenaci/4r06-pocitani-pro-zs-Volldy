import tkinter as tk
from tkinter import Label, LabelFrame, Radiobutton, Entry, Button
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

statistika = LabelFrame(start, text="Statistika", padx=5, pady=5)
statistika.grid(row=2)
#menu pro znamenka
Radiobutton(znamenka, value="+", variable=znamenko, command=vyberznamenka).pack()
Radiobutton(znamenka, value="-", variable=znamenko, command=vyberznamenka).pack()
Radiobutton(znamenka, value="*", variable=znamenko, command=vyberznamenka).pack()
Radiobutton(znamenka, value="/", variable=znamenko, command=vyberznamenka).pack()
novejpriklad=Button(znamenka, text="Začni na novo", command=priklady, width=5)

#přiklad
cisloAentry=Entry(priklad, width=4, state="readonly")
cisloAentry.grid(row=1, column=0)

matematickaoperaceLabel=Label(priklad, text="?")
matematickaoperaceLabel.grid(row=1, column=1)

cisloBentry=Entry(priklad, width=4, state="readonly")
cisloBentry.grid(row=1, column=2)

rovnitkoLabel=Label(priklad, text="=")
rovnitkoLabel.grid(row=1, column=3)

vysledekEntry=Entry(priklad, width=4)
vysledekEntry.grid(row=1, column=4)

#hodnocení
novyprikladButt=Button(statistika, text="Nový příklad", command=priklady)
novyprikladButt.grid(row=2)

statButt=Label(statistika, text="Zkontroluj", command=kontrola)
statButt.grid(row=3)

statLabel=Label(statistika, text="?")
statLabel.grid(row=3)

def vyberznamenka():
    selection=str(znamenko.get())
    matematickaoperaceLabel.config(text=selection)
    novejpriklad.invoke()

def priklady():
    if matematickaoperaceLabel ['text'] == "+":
        cisloAentry = random.randint(1,10)
        cisloBentry = random.randint(1,10)
    if matematickaoperaceLabel ['text'] == "-":
        cisloAentry =  random.randint(0, 99)
        cisloBentry = random.randint(0, cisloA)
    if matematickaoperaceLabel ['text'] == "*":
        cisloAentry =  random.randint(1, 9)
        cisloBentry = random.randint(1, 9)
    if matematickaoperaceLabel ['text'] == "/":
        cisloAentry =  random.randint(1, 9)
        cisloBentry = random.randint(1, 9)
    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA))
    cisloBentry.delete(0,END)
    cisloBentry.insert(0, str(cisloB))
    vysledekEntry.delete(0,EDN)
    
def kontrola():
    global dobre
    global celkem
    a = int(cisloAentry.get())
    b = int(cisloBentry.get())
    vys = vysledekEntry.get()
    if matematickaoperaceLabel['text'] == "+":
        vysledek = a+b
    if matematickaoperaceLabel['text'] == "-":
        vysledek = a-b
    if matematickaoperaceLabel['text'] == "*":
        vysledek = a*b
    if matematickaoperaceLabel['text'] == "/":
        vysledek = a/b
    try:
        if vysledek == int(vys):
            dobre+=1
            celkem+=1
            novejpriklad.invoke()
            vysledekEntry.delete(0)
            hlavni.title("Počítání pro základní školy")
        if vysledek != int(vys):
            celkem+=1
            novejpriklad.invoke()
            vysledekEntry.delete(0)
            hlavni.title("Počítání pro základní školy")
    except:
        hlavni.title("Ty jsi chobot")
        celkem+=1
        novejpriklad.invoke()
    statLabel.config(text='{0}/{1}'.format(dobre,celkem))


start.mainloop()
