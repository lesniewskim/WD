import sys
x = "Podaj dwie liczby do mnozenia :" 


a = sys.stdin.readline()
a = int(a)


b = sys.stdin.readline()
b = int(b)

c = a*b
c = str(c)
sys.stdout.write(c)
 