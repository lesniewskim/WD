a = int(input("podaj a "))
b = int(input("podaj b "))
x = int(input("podaj x "))
spr = a * x + b
print("wynik to:",spr)
if a > 0:
    print("Funkcja rosnąca.")
elif a < 0:
    print("Funkcja malejąca.")
else:
    print("Funkcja stała")


#return k -- zwracamy dana wartosc 