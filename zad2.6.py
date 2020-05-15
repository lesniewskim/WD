import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

def spr(a,b,x,y) : 
    r = math.sqrt(((x-a)**2)+((y-b)**2))
    return r

print(spr(a,b,x,y))
