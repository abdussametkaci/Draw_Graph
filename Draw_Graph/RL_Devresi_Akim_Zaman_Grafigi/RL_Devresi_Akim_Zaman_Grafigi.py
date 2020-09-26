import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *
import math as m

class Ekran(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x720")
        self.label_gerilim = Label(self, text = "Gerilim (V): ")
        self.label_gerilim.pack()
        self.entry_gerilim = Entry(self)
        self.entry_gerilim.pack()
        self.label_direnç = Label(self, text = "Direnç (OHM): ")
        self.label_direnç.pack()
        self.entry_direnç = Entry(self)
        self.entry_direnç.pack()
        self.label_indüktans = Label(self, text = "İndüktans (mH): ")
        self.label_indüktans.pack()
        self.entry_indüktans = Entry(self)
        self.entry_indüktans.pack()
        self.label_zaman_aralığı = Label(self, text = "Zaman Aralığı (ms): ")
        self.label_zaman_aralığı.pack()
        self.label_başlangıç = Label(self, text = "Başlangıç")
        self.label_başlangıç.pack()
        self.entry_başlangıç = Entry(self)
        self.entry_başlangıç.pack()
        self.label_bitiş = Label(self, text = "Bitiş")
        self.label_bitiş.pack()
        self.entry_bitiş= Entry(self)
        self.entry_bitiş.pack()
        self.button = Button(self, text = "Çiz", command = self.çiz, width= 10, height = 1)
        self.button.pack()

    def çiz(self):
        def akım(V, R, L, t):
            T = L/R
            zaman.append(t)
            return (V/R)*(1 - m.exp(-t*10**-3/T))

        zaman = []
        akım = [akım(int(self.entry_gerilim.get()), int(self.entry_direnç.get()), int(self.entry_indüktans.get())*10**-3, i) for i in range(int(self.entry_başlangıç.get()), int(self.entry_bitiş.get()) + 1)]
        

        fig = Figure(figsize=(2,2), dpi = 100)
        a = fig.add_subplot(111)
        
        a.plot(zaman, akım,color='blue')

        a.set_title ("RL Devresi Akım-Zaman Grafiği", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = "bottom", fill="both", expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side="top", fill="both", expand=True)

ekran = Ekran()
ekran.mainloop()
