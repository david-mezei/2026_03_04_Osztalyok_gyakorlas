from auto import Auto
import random as r
from datetime import datetime

auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Seat", "Cordoba", 2005)
auto4 = Auto("Suzuki", "Swift", 2009)
auto5 = Auto("Kia", "Ceed", 2021)
auto6 = Auto("BMW", "320d", 2019, 6.5)

autok = [auto1, auto2, auto3, auto4, auto5]
print("Alaphelyzet: ")
for auto in autok:
    print(auto)

print("\nGyorsít: ")
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
print(f"\nAz autók átlagéletkora: {atlag_eletkor} év")

# Legöregebb autó:  C version
gyartasi_evek = [auto.gyartasi_ev for auto in autok]
for auto in autok:
    if auto.gyartasi_ev == min(gyartasi_evek):
        eletkora = year - auto.gyartasi_ev
        print(f"\nA legidősebb autó: {auto.marka} {auto.tipus} ({auto.gyartasi_ev}) - [életkora: {eletkora} év]")

auto6.utazik(200)
print("\nUtazás után:", auto6)
auto6.tankol(20)
print("\nTankolás után:", auto6)


