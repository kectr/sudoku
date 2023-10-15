from tkinter import *
from tkinter import ttk
from listfonc import *

global donduruculiste,listem,sudokual,temizle,girdi
donduruculiste = [0, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
listem = []
girdi = []
twod_listcreat(girdi,9)
for x in range(9):
    for _ in range(9):
        girdi[x].append(0)
threed_listcreat(listem,9,9)

def sudokual():
    try:
        for x in range(9):
            for y in range(9):
                girdi[x][y] = listem[x][y].get()
    except ValueError:
        raise ValueError

def temizle():
    for x in range(9):
        for y in range(9):
            listem[x][y].set('')

def calistir():
    root = Tk()
    root.title("Sudoku giris ekrani")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=10)
    root.rowconfigure(0, weight=10)


    for x in range(9):
        for y in range(9):
            listem[x][y] = StringVar()


    for x in range(11):
        if x == 3 or x == 7:
            pass
        for y in range(11):
            if x != 3 and x != 7 and y != 3 and y != 7:
                feet_entry = ttk.Entry(mainframe, width=3, textvariable=listem[donduruculiste[x]][donduruculiste[y]])
                feet_entry.grid(column=x, row=y)


    yatay = '-'
    dikey = '|'
    kesisim = '+'


    for x in range(11):
        ttk.Label(mainframe, text=yatay).grid(column=x, row=3)
        ttk.Label(mainframe, text=yatay).grid(column=x, row=7)
    for y in range(11):
        ttk.Label(mainframe, text=dikey).grid(column=3, row=y)
        ttk.Label(mainframe, text=dikey).grid(column=7, row=y)
    for x in (3,7):
        for y in (3,7):
            ttk.Label(mainframe, text=kesisim).grid(column=x, row=y)







    ttk.Button(mainframe, text="Tamam", command=sudokual).grid(column=13, row=10, sticky=W)
    ttk.Button(mainframe, text='Temizle', command=temizle).grid(column=14, row=10, sticky=W)


    root.bind("<Return>", sudokual)
    root.bind("<Return>", temizle)


    root.mainloop()