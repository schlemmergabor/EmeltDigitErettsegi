# 2023. őszi (október-november) digitális kultúra emelt szintű
# érettségi feladat megoldása
# (c) https://digiterettsegi.hu/


# listában tárolom a fájlból beolvasott adatokat
adatok = []

# összes függvény -> 6. feladat
def osszes(varos, nap):
    
    # db kezdetben 0
    db = 0
    
    # végig megyek az adatok listán
    for i in adatok:
        
        # ha az aktuális (i edik) városa és napja megegyezik
        if i["varos"]==varos and i["nap"] == nap:
            # darabszám növelése
            db += i["db"]
    
    # db érték visszaadása
    return db


# 1. feladat -> fájlból beolvasás
# megnyitom olvasásra
file = open("rendel.txt")

# soronként beolvasom
for sor in file:
    # strip -> eltűnteti a sor végéről a \n (enter)-t
    # split -> feldaraboljuk -> sor[0], sor[1], sor[2] lesz belőle
    sor = sor.strip().split(" ")
    
    # szótár elemet készítek
    # egy szótárban key:value párok vannak
    # int( ... ) -> kell mert egész számot tárol
    elem = {"nap":   int(sor[0]),
            "varos": sor[1],
            "db":    int(sor[2])}

    # a listához hozzáadom a szótár elemet
    adatok.append(elem)

# print(adatok) - ellenőrzéshez használtam


print("2. feladat")
# len(...) -> lista hossza mennyi
print(f"A rendelések száma: {len(adatok)}")


print("3. feladat")
# int(...) -> a szám beolvasás miatt
adottNap = int(input("Kérem, adjon meg egy adott napot: "))

# rendelések száma kezdetben 0
db = 0

# végig megyünk a listán
for i in adatok:
    # épp az adott napit dolgozzok fel
    if i["nap"] == adottNap:
        db += 1 # db = db + 1

print(f"A rendelések száma az adott napon: {db}")

print("4. feladat")
# üres halmazt készítettem
# a halmazban kétszer nincs ugyanolyan elem, azaz
# minden elem csak 1x szerepel benne -> ez kell nekünk!
napok = set()

# végig megyünk az adatokon
for i in adatok:
    # ha nem reklámmal érintett város
    if i["varos"]=="NR":
        # hozzáadjuk a set/halmaz-hez/hoz
        napok.add(i["nap"])

# hány napon nem volt rendelés?
# 30 - napok száma
nincsRendeles = 30 - len(napok)

if nincsRendeles == 0:
    print("Minden nap volt rendelés a reklámban nem érintett városból")
else:
    print(f"{nincsRendeles} nap nem volt a reklámban nem érintett városból rendelés")


# maxtétel
print("5. feladat")
# max értéke
maxDb = 0
# max értékhez tartozó nap
maxNap = 0

# végig járjuk a listát
for i in adatok:
    # ha a mostani nagyobb érték, mint az eddigi
    if i["db"] > maxDb:
        # maxDd frissítése
        maxDb = i["db"]
        # nap frissítése
        maxNap = i["nap"]
        
print(f"A legnagyobb darabszám: {maxDb}, a rendelés napja: {maxNap}")

# 6. feladat -> összes függvény készítése
# lásd feljebb

print("7. feladat")
# felhasználjuk az összes függvényt
print(f'A rendelt termékek darabszáma a 21. napon PL: {osszes("PL", 21)} TV: {osszes("TV", 21)} NR: {osszes("NR", 21)}')

# segéd függvény a számításhoz
# hányszor rendeltek adott napon, adott városból

def dbossz(varos, nap):
    db = 0
    for i in adatok:
        if i["nap"]==nap and i["varos"]==varos:
            # db = db + 1, mert
            # nem a rendelés db száma a lényeg, hanem hogy
            # rendelés volt
            db += 1

    return db


print("8. feladat")
# write módba nyitom meg a fájlt
f = open("kampany.txt", "w")

# kiirom
print("Napok\t1..10\t11..20\t21..30")
# fájlba is kiírom
# sor végén \n az enter
f.write("Napok\t1..10\t11..20\t21..30\n")

# segédváltozók első 10 nap, második 10 nap, harmadik 10 napra
ossz1 = 0
ossz2 = 0
ossz3 = 0

# első tíz nap -> 1-től 10-ig
for i in range(1, 11):
    ossz1 += dbossz("PL", i)
    
for i in range(11, 21):
    ossz2 += dbossz("PL", i)
    
for i in range(21, 31):
    ossz3 += dbossz("PL", i)

# kiiírás
print(f"PL\t{ossz1}\t{ossz2}\t{ossz3}")
f.write(f"PL\t{ossz1}\t{ossz2}\t{ossz3}\n")

# következő város
ossz1 = 0
ossz2 = 0
ossz3 = 0

for i in range(1, 11):
    ossz1 += dbossz("TV", i)
for i in range(11, 21):
    ossz2 += dbossz("TV", i)
for i in range(21, 31):
    ossz3 += dbossz("TV", i)

print(f"TV\t{ossz1}\t{ossz2}\t{ossz3}")
f.write(f"TV\t{ossz1}\t{ossz2}\t{ossz3}\n")

# harmadik város
ossz1 = 0
ossz2 = 0
ossz3 = 0

for i in range(1, 11):
    ossz1 += dbossz("NR", i)
for i in range(11, 21):
    ossz2 += dbossz("NR", i)
for i in range(21, 31):
    ossz3 += dbossz("NR", i)

print(f"NR\t{ossz1}\t{ossz2}\t{ossz3}")
f.write(f"NR\t{ossz1}\t{ossz2}\t{ossz3}\n")

# fájlt lezárom -> elmentem
f.close()

# a feladat a táblázatkezelőben folytatódik
# nézd meg a videót !!!



    
        



    

