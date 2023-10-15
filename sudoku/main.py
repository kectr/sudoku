from listfonc import *
from tkinter import *
from tkinter import ttk


def nkare(x, y):
    return int(x / 3) + 3 * int(y / 3)


def nindis(x, y):
    return int(x % 3) + 3 * int(y % 3)


class Sudoku:
    def resetgelebilecekler(self):
        self.satir_gelebilecekler = threed_listcreat(9, 9)
        self.sutun_gelebilecekler = threed_listcreat(9, 9)
        self.kare_gelebilecekler = threed_listcreat(9, 9)

    def __init__(self):
        self.gelebilecek_sayilar = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.defaultvalue = ''
        self.donduruculiste = [0, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
        self.baslangicsatir = twod_listcreat(9, defaultvalue=self.defaultvalue, y=9)
        self.listem = threed_listcreat(9, 9)
        self.satir = twod_listcreat(9, defaultvalue=self.defaultvalue, y=9)
        self.sutun = twod_listcreat(9, defaultvalue=self.defaultvalue, y=9)
        self.kare = twod_listcreat(9, defaultvalue=self.defaultvalue, y=9)
        self.satir_gelebilecekler = None
        self.sutun_gelebilecekler = None
        self.kare_gelebilecekler = None
        self.resetgelebilecekler()

    def sskolustur(self):
        for x in range(9):
            for y in range(9):
                self.satir[x][y] = self.baslangicsatir[x][y]
                self.sutun[y][x] = self.baslangicsatir[x][y]
                self.kare[nkare(x, y)][nindis(x, y)] = self.baslangicsatir[x][y]
        self.resetgelebilecekler()
        self.sskolustur_gelebilecek()

    def sskolustur_gelebilecek(self):
        for x in range(9):
            for y in range(9):
                if self.satir[x][y] != '':
                    for z in self.gelebilecek_sayilar:
                        if self.satir[x].count(z) == 0 and self.sutun[y].count(z) == 0 and self.kare[nkare(x, y)].count(
                                z) == 0:
                            self.satir_gelebilecekler[x][y].append(z)
                            self.sutun_gelebilecekler[y][x].append(z)
                            self.kare_gelebilecekler[nkare(x, y)][nindis(x, y)].append(z)

    def gelebileceklerdensil(self, indis, sayi, tip):
        if tip == 'satir':
            for t in range(9):
                if self.satir_gelebilecekler[indis][t].count(sayi) != 0:
                    self.satir_gelebilecekler[indis][t].remove(sayi)
        elif tip == 'sutun':
            for t in range(9):
                if self.sutun_gelebilecekler[indis][t].count(sayi) != 0:
                    self.sutun_gelebilecekler[indis][t].remove(sayi)
        elif tip == 'kare':
            for t in range(9):
                if self.kare_gelebilecekler[indis][t].count(sayi) != 0:
                    self.kare_gelebilecekler[indis][t].remove(sayi)

    def sayikoy(self, x, y, sayi):
        self.satir[x][y] = sayi
        self.sutun[y][x] = sayi
        self.kare[nkare(x, y)][nindis(x, y)] = sayi
        self.gelebileceklerdensil(x, sayi, 'satir')
        self.gelebileceklerdensil(y, sayi, 'sutun')
        self.gelebileceklerdensil(nkare(x, y), sayi, 'kare')

    def hucretekalgoritmasi(self):
        for x in range(9):
            for y in range(9):
                if len(self.satir_gelebilecekler[x][y]) == 1:
                    self.sayikoy(x, y, self.satir_gelebilecekler[x][y][0])

    def ssk_tekalgoritmesi(self):
        for z in self.gelebilecek_sayilar:
            for x in range(9):
                satirztop = 0
                yforsatir = None
                for y in range(9):
                    if self.satir_gelebilecekler[x][y].count(z) != 0:
                        satirztop += self.satir_gelebilecekler[x][y].count(z)
                        yforsatir = y
                if satirztop == 1:
                    self.sayikoy(x, yforsatir, z)

            for y in range(9):
                sutunztop = 0
                xforsutun = None
                for x in range(9):
                    if self.sutun_gelebilecekler[y][x].count(z) != 0:
                        sutunztop += self.sutun_gelebilecekler[y][x].count(z)
                        xforsutun = x
                    if sutunztop == 1:
                        self.sayikoy(xforsutun, y, z)

            for i in range(9):
                kareztop = 0
                xforkare = None
                yforkare = None
                for j in range(9):
                    if self.kare_gelebilecekler[i][j].count(z) != 0:
                        kareztop += self.kare_gelebilecekler[i][j].count(z)
                        xforkare = 3 * (i % 3) + j % 3
                        yforkare = 3 * int(i / 3) + int(j / 3)
                    if kareztop == 1:
                        self.sayikoy(xforkare, yforkare, z)

    def nlialgoritmasi(self):
        for x in range(9):
            for y in range(9):
                if len(self.satir_gelebilecekler[x][y]) < (8 - y):
                    arananliste = self.satir_gelebilecekler[x][y]
                    arananlistelerinkordinatlari = list()
                    if len(arananliste) == self.satir_gelebilecekler[x].count(arananliste):
                        for i in range(9):
                            if self.satir_gelebilecekler[x][i] == arananliste:
                                arananlistelerinkordinatlari.append((x, i))
                        for z in arananliste:
                            self.gelebileceklerdensil(x, z, 'satir')
                        for (a, b) in arananlistelerinkordinatlari:
                            self.satir_gelebilecekler[a][b] = arananliste

        for y in range(9):
            for x in range(9):
                if len(self.sutun_gelebilecekler[y][x]) < (8 - x):
                    arananliste = self.sutun_gelebilecekler[y][x]
                    arananlistelerinkordinatlari = list()
                    if len(arananliste) == self.sutun_gelebilecekler[y].count(arananliste):
                        for i in range(9):
                            if self.sutun_gelebilecekler[y][i] == arananliste:
                                arananlistelerinkordinatlari.append((y, i))
                        for z in arananliste:
                            self.gelebileceklerdensil(y, z, 'sutun')
                        for (a, b) in arananlistelerinkordinatlari:
                            self.sutun_gelebilecekler[a][b] = arananliste

        for x in range(9):
            for y in range(9):
                if len(self.kare_gelebilecekler[nkare(x, y)][nindis(x, y)]) < (8 - nindis(x, y)):
                    arananliste = self.kare_gelebilecekler[nkare(x, y)][nindis(x, y)]
                    arananlistelerinkordinatlari = list()
                    if len(arananliste) == self.kare_gelebilecekler[nkare(x, y)].count(arananliste):
                        for i in range(9):
                            if self.kare_gelebilecekler[nkare(x, y)][i] == arananliste:
                                arananlistelerinkordinatlari.append((nkare(x, y), i))
                        for z in arananliste:
                            self.gelebileceklerdensil(nkare(x, y), z, 'kare')
                        for (a, b) in arananlistelerinkordinatlari:
                            self.kare_gelebilecekler[a][b] = arananliste

    def kazikalgortimasi(self):
        for i in range(9):
            for z in self.gelebilecek_sayilar:
                arananlarinkordinatlari = list()
                for j in range(9):
                    if self.kare_gelebilecekler[i][j].count(z) == 1:
                        x = 3 * (i % 3) + j % 3
                        y = 3 * int(i / 3) + int(j / 3)
                        arananlarinkordinatlari.append((x,y))
                    if 2 <= len(arananlarinkordinatlari) <= 3:
                        kaydedilenx = arananlarinkordinatlari[0][0]
                        for t in arananlarinkordinatlari:
                            if kaydedilenx == t[0]:
                                continue
                            else:
                                kaydedilenx = None
                                break
                        kaydedileny = arananlarinkordinatlari[0][1]
                        for k in arananlarinkordinatlari:
                            if kaydedileny == k[1]:
                                continue
                            else:
                                kaydedileny = None
                                break
                        if kaydedilenx != None:
                            self.gelebileceklerdensil(kaydedilenx,z,'satir')
                            for (a,b) in arananlarinkordinatlari:
                                self.satir_gelebilecekler[a][b].append(z)

                        if kaydedileny != None:
                            self.gelebileceklerdensil(kaydedileny,z,'sutun')
                            for (a,b) in arananlarinkordinatlari:
                                self.sutun_gelebilecekler[b][a].append(z)

    def coz(self):
        toplambos = 0
        for x in range(9):
            toplambos += self.satir[x].count('')
        while toplambos > 0:
            self.hucretekalgoritmasi()
            self.ssk_tekalgoritmesi()
            self.nlialgoritmasi()
            self.kazikalgortimasi()
            for x in range(9):
                toplambos = 0
                toplambos += self.satir[x].count('')








    def sudokual(self):
        for x in range(9):
            for y in range(9):
                self.baslangicsatir[x][y] = self.listem[x][y].get()
        self.sskolustur()

    def temizle(self):
        for x in range(9):
            for y in range(9):
                self.listem[x][y].set(self.defaultvalue)

    def calistir(self):
        root = Tk()
        root.title("Sudoku giris ekrani")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=10)
        root.rowconfigure(0, weight=10)
        for x in range(9):
            for y in range(9):
                self.listem[x][y] = StringVar()

        for x in range(11):
            if x == 3 or x == 7:
                pass
            for y in range(11):
                if x != 3 and x != 7 and y != 3 and y != 7:
                    feet_entry = ttk.Entry(mainframe, width=3,
                                           textvariable=self.listem[self.donduruculiste[x]][self.donduruculiste[y]])
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
        for x in (3, 7):
            for y in (3, 7):
                ttk.Label(mainframe, text=kesisim).grid(column=x, row=y)

        ttk.Button(mainframe, text="Tamam", command=self.sudokual).grid(column=13, row=10, sticky=W)
        ttk.Button(mainframe, text='Temizle', command=self.temizle).grid(column=14, row=10, sticky=W)
        ttk.Button(mainframe, text='Çöz', command=self.coz).grid(column=15, row=10, sticky=W)

        root.bind("<Return>", self.sudokual)
        root.bind("<Return>", self.temizle)
        root.mainloop()


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.calistir()
