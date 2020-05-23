import math

#a = int(input("Podaj a: "))
#b = int(input("Podaj b: "))
a = 6
b = 8
def spr(a,b) :
    pit = math.sqrt(a**2+b**2)
    return pit

print(spr(a,b))