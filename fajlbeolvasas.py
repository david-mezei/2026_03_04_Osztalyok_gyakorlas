from auto import Auto
import random

autok = []
with open("adatok/autok.txt", "r", encoding="utf-8") as f:
    next(f)
    for sor in f:
        adatok = sor.strip().split(',')
        if len(adatok) >= 4:
            marka, tipus, gyartasi_ev, fogyasztas = adatok
            auto = Auto(marka, tipus, int(gyartasi_ev), float(fogyasztas))
            autok.append(auto)

for auto in autok:
    tavolsag = random.randint(100, 500)
    auto.utazik(tavolsag)
    print(f"{auto.marka} {auto.tipus} megtett {tavolsag} km-t.")

    if auto.uzemanyag > 0:
        print(f"\tVan még üzemanyag ({auto.uzemanyag:.1f} l).")
    else:
        print(f"\tKifogyott az üzemanyag!")