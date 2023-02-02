"""II/A, B, C:
           	20 : 34 : 78 : 83 : 90
II/D, E:
           	Első idős ember korának helye a listában: 2.
kimutatas.txt tartalma:
II/F:
 Első idős ember korának helye a listában: 2.

A.	Kérj be 5 egész számot a felhasználótól, melyek az egyes személyek korát jelentik! [0,120] (4p)
B.	A bekért  értékeket tárolja lista adatszerkezetben! (1p)
C.	Írasd ki a képernyőre a számokat : -tal (kettősponttal) elválasztva. A : jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írj függvényt elso_idos néven, ami megkeresi az első  70 év feletti kort. A visszatérési érték legyen egy egész szám, melynek a kornak az INDEX-ét tartalmazza, a függvény bemenete a lista! (3p)
E.	Az elso_idos függvény eredményét írasd ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazz meg! (2p)
F.	Az elso_idos függvény eredményét írasd ki a mintának megfelelően a oreg.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)
"""
korok_lista=[]
def adatbeker():
    i=0
    while i<5:
        korok_lista.append(int(input("mondj nekem életkorokat!")))
        i+=1
    print(korok_lista)
    print("-".join(str(szamok)for szamok in korok_lista))
def elso_idos():
    i=0
    hetvenesek=[]
    elso=0
    while i<len(korok_lista):
        if korok_lista[i]>70:
            hetvenesek.append(i)
        i+=1
    elso=hetvenesek[0]
    return (elso)
    print(elso)
    konzol_kiir(elso)

def konzol_kiir(elso):
    (f" Első idős ember korának helye a listában: {elso}")



