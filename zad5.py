
print("Podaj a: ")
a = input()
a = int(a)
print("Podaj b: ")
b = input()
b = int(b)
print ("Podaj c: ")
c = input()
c = int(c)
if (a>=0 and a<=10):
    print("a jest w przedziale od 0 do 10 i")
    if(a>b):
        print("a jest wieksze od b")
    elif(b>c):
        print("b jest wieksze od c")
    elif(a==b and b==c):
        print("liczby sa rowne")
    else:
        print("c ma najwieksza wartosc")

else:
        print("a nie jest w przediale od 0 do 10")

        