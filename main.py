from auto import Auto
import random as r
from datetime import datetime

auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Seat", "Cordoba", 2005)
auto4 = Auto("Suzuki", "Swift", 2009)
auto5 = Auto("Kia", "Ceed", 2021)

autok = [auto1, auto2, auto3, auto4, auto5]
for auto in autok:
    print(auto)

print("\nGyorsít\n")
for auto in autok:
    auto.gyorsit(r.randint(30, 130))
    print(auto)

# Atlag eletkor kiszamitasa
year = datetime.now().year
autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = year - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor / autok_szama
print(f"Az autók átlagéletkora: {atlag_eletkor} év")

# Legöregebb autó
legoregebb = autok[0]
for auto in autok:
    if auto.gyartasi_ev < legoregebb.gyartasi_ev:
        legoregebb = auto

legoregebb_eletkor = year - legoregebb.gyartasi_ev

print(f"A legöregebb autó: {legoregebb.marka} {legoregebb.tipus} ({legoregebb.gyartasi_ev}, életkora: {legoregebb_eletkor})")

