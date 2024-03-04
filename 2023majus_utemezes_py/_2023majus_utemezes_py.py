# 2023. őszi (október-november) digitális kultúra emelt szintű
# érettségi feladat megoldása
# (c) https://digiterettsegi.hu/

# listában fogom tárolni a fájlból beolvasott adatokat
adatok = []

# megnyitom "read" módban a fájlt
file = open("taborok.txt")

# soronként bejárom a fájlt
for sor in file:
    # .strip() -> eltűnteti a \n-t a végéről
    # .split() -> feldarabolja a \t karakternél
    sor = sor.strip().split("\t")

    # szótár elemet létrehozok
    # int(...) -> egész számok miatt kell
    elem = {"hoTol":int(sor[0]),
            "napTol":int(sor[1]),
            "hoIg": int(sor[2]),
            "napIg": int(sor[3]),
            "diakok": sor[4],
            "tipus": sor[5]
    }

    # hozzáadom a szótár elemet a listához
    adatok.append(elem)

# ellenőrzés miatt volt itt, kommentben hagyom
# print(adatok)
    
print("2. feladat")
# lista hossza = adatsorok száma len(listaNeve)
print(f"Az adatsorok száma: {len(adatok)}")
# listaNeve[0] -> első érték
print(f'Az először rögzített tábor témája: {adatok[0]["tipus"]}')
# listaNeve[-1] -> utolsó érték
print(f'Az utoljára rögzített tábor témája: {adatok[-1]["tipus"]}')


print("3. feladat")
# volt-e már zenei tábor? -> kezdetben nem volt -> False
voltE = False

# végig megyek az adatok listán
for i in adatok:
    # ha az i. (aktuális) típusa zenei
    if i["tipus"]=="zenei":
        # akkor volt zenei tábor
        voltE = True
        # mintaszerű kiírás
        print(f'Zenei tábor kezdődik {i["hoTol"]}. hó {i["napTol"]}. napján.')

# ha maradt a voltE értéke False -> nem volt tábor
if voltE == False:
    print("Nem volt zenei tábor.")


print("4. feladat")
# kezdetben eddigi max táborozói létszám 0
maxLetszam = 0
# végig megyek az adatokon
for i in adatok:
    # táborozók létszáma -> a diákok betűinek hossza -> len
    # ha a mostani hossz > eddigi max hossz
    if len(i["diakok"]) > maxLetszam:
        # a mostani legyen az új max hossz
        maxLetszam = len(i["diakok"])

### 

print("Legnépszerűbbek: ")
# végig megyek újra az adatokon
for i in adatok:
    # ahol a táborozók száma megegyezik a maxLétszámmal
    if len(i["diakok"]) == maxLetszam:
        # minta szerű kiírás
        print(f'{i["hoTol"]} {i["napTol"]} {i["tipus"]}')

# függvény készítése
# neve(paraméter1, paraméter2)
def sorszam(honap, nap):
    if honap == 6: 
        return nap-15
    if honap == 7:
        return nap + (30-15)
    if honap == 8:
        return nap + (31) + (30-15)

# függvény kipróbálása
# print(sorszam(8, 31))

print("6. feladat")
honap = int(input("hó: "))
nap = int(input("nap: "))
# a beolvasott hónap-nap páros hányadik nap a szünetből
napsorszam = sorszam(honap, nap)
# kezdetben 0 db tábor van ezen a napon
db = 0
# végig járjuk az adatokat
for i in adatok:
    # az aktuális tábor kezdőnapjának sorszáma
    kezdoNap = sorszam(i["hoTol"], i["napTol"])
    # az aktuális tábor utolsó napjának sorszáma
    utolsoNap = sorszam(i["hoIg"], i["napIg"])

    # ha a beolvasott nap a kettő között van, akkor zajlik a tábor
    if kezdoNap <= napsorszam <= utolsoNap:
        db += 1

print(f"Ekkor éppen {db} tábor tart.")


print("7. feladat")
betu = input("Adja meg egy tanuló betűjelét: ")
# üres lista a tanuló táborainak
taborai = [] # tanuló táborai

# végig járjuk az adatokat
for i in adatok:
    # ha a tanuló betűje benne van az aktuális tábor névsorában
    if betu in i["diakok"]:
        # hozzáadjuk a listához
        taborai.append(i)

# rendezett listába rendezzük a taborai listát
# key - a rendezési kulcs
# először "hoTol" érték szerint, majd "napTol" szerint
rendezett = sorted(taborai, key=lambda x: (int(x["hoTol"]), int(x["napTol"])))

# kimeneti fájlt megnyitjuk írásra (write)
f = open("egytanulo.txt", "w")

# végig megyünk a rendezett értékeken
for i in rendezett:
    # először kiírtam a képernyőre, hogy ellenőrizzem -> utána komment
    # print(i)
    # fájlba írok a \n a sor vége jel !
    f.write(f'{i["hoTol"]}.{i["napTol"]}-{i["hoIg"]}.{i["napIg"]}. {i["tipus"]}\n')

# elmentem a fájlt
f.close()

# segédváltozó, kezdetben azt mondom, hogy ott tud lenni mindenhol
OK = True # ott tud lenni mindenhol

# az előző tábor amin részt vett, annak a sorszáma
vegeNap = 0

# végig megyünk a rendezett táborain
for i in rendezett:
    # ha az aktuális kezdősorszáma előtte van a mai napnak, akkor
    # ütköznek nem tud ott lenni
    if sorszam(i["hoTol"], i["napTol"]) <= vegeNap:
        OK = False # nem tud ott lenni végig
    
    # végenap frissítése -> következő tábor vizsgálatánál ezt vegye figyelembe
    vegeNap = sorszam(i["hoTol"], i["napTol"])

# ha OK értéke False
if OK == False:
    print("Nem mehet el mindegyik táborba")
# minden más esetben (ha OK értéke True)
else:
    print("Ott tud lenni mindegyiken")
