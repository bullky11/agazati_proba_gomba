"""I/A:
A generált szám: 45

I/B:
A szám öttel és hárommal is osztható!

A.	Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban!  (2p)
B.	A program írja ki a következők egyikét: (a mintának megfelelően – 1p):
•	Amennyiben a szám 5-tel osztható:
“A szám öttel osztható!”,
•	Amennyiben a szám 3-mal osztható:
“A szám hárommal  osztható!”,
•	Amennyiben a szám 5-tel és 3 – mal is osztható:
“A szám öttel és hárommal is osztható!”,

A három kiírás közül csak az egyik jelenjen meg a képernyőn!. (4p + 1p)
"""
import random


def veletlen_szamok():
    szam=random.randint(1,50)
    print(szam)
    if (szam %5==0 and szam %3==0):
         print("A szám öttel és hárommal is osztható!")
    elif szam %5==0:
        print("A szám öttel osztható!")
    elif szam %3==0:
        print("A szám hárommal  osztható!")
    else:
        print(f"A {szam} se 5 el se 3 al nem osztható")
