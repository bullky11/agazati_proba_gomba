"""A gombak.txt forrásállomány, gombák adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:
·         gomba neve: pl.: piros csészegomba
·         nemzettség pl.: csészegomba
·         évszak pl.: tél, tavasz
Az állomány első sora a mezőneveket tartalmazza @  jellel elválasztva.
A megoldás mintája:
III/A, B:
            	A gombák száma: 78.
III/C:
           Az első papsapkagomba neve: homoki papsapka.
III/D:
            	A tinóru gombák száma: 14.
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gombák.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a gombák számát a mintának megfelelően a konzolra! A metódus neve legyen gombak_szama! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy a melyik a papsapkagombák nemzettségben melyik az első gomba, amelyik szerepel a listában?  A metódus neve legyen papsapka! (4p)
D.	Írassa ki konzolra a mintának megfelelően a tinóru nemzettséghez tartozó gombák számát! A metódus neve tinoru legyen  (4p)

"""
from Gombaclass import Gombaclass
gomba_lista=[]
def beolvas():
    fajlom=open("gombak_jav.txt","r",encoding="utf-8")
    fajlom.readline()
    fajltartalom=fajlom.readlines()
    i=0
    while i<len(fajltartalom):
        sor=fajltartalom[i].strip().split("@")
        gomba_lista.append(Gombaclass(sor))
        i+=1
    print(gomba_lista[0])
    print(len(gomba_lista))
def papsapka():
    i=0
    elso_sapka=[]
    while i<len(gomba_lista):
        if gomba_lista[i].nemzettseg=="papsapkagombák ":
            elso_sapka.append(gomba_lista[i].nev)
        i+=1
    print(elso_sapka[0])
def tinoru():
    i=0
    db=0
    while i<len(gomba_lista):
        if gomba_lista[i].nemzettseg=="tinóru":
            db+=1
        i+=1
    print(db)