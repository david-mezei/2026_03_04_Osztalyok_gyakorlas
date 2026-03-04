class Auto:

    def __init__(self, marka_: str, tipus_: str, gyartasi_ev_: int, fogyasztas_ = 7.5, uzemanyag_ = 50):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_
        self.sebesseg = 0
        self.fogyasztas = fogyasztas_
        self.uzemanyag = uzemanyag_

    def __str__(self):
        return f"{self.marka} {self.tipus} ({self.gyartasi_ev}), sebesség: {self.sebesseg} km/h, üzemanyag: {self.uzemanyag} l"

    def gyorsit(self, ertek: int):
        self.sebesseg += ertek
        if self.sebesseg > 200:
            self.sebesseg = 200

    def fekez(self, ertek: int):
        self.sebesseg -= ertek
        if self.sebesseg < 0:
            self.sebesseg = 0

    def tankol(self, liter):
        self.uzemanyag += liter
        if self.uzemanyag > 50:
            self.uzemanyag = 50
            print("Tele van a tank! ")

    def utazik(self, km):
        fogyasztott = (km / 100) * self.fogyasztas
        self.uzemanyag -= fogyasztott
        if self.uzemanyag < 0:
            self.uzemanyag = 0
            print("Nincs elég üzemanyag!")