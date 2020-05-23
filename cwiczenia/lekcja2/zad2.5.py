print("funkcja y1")
a1 = int(input("Podaj a1:"))
x1 = int(input("Podaj x1:"))
b1 = int(input("Podaj b1:"))
print("funkcja y2")
a2 = int(input("Podaj a2:"))
x2 = int(input("Podaj x2:"))
b2 = int(input("Podaj b2:"))

def spr(a1,a2):
    if a1 == a2:
        print("Równoległe")
    elif a1*a2 == -1:
        print("Prostopadłe")
    return ""

print("funkcja y1 wynosi:", a1*x1+b1)
print("funkcja y1 wynosi:", a2*x2+b2)
print("proste sa ",spr(a1,a2))