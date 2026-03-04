class Auto:
    def __init__(self, marka_: str, tipus_: str, gyartasi_ev_: int):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_

    def __str__(self):
        return f"{self.marka} {self.tipus} ({self.gyartasi_ev})"