print("Podaj zakres liczb ktore sprawdzasz czy sa podielne przez 5: ")
print("Podaj od jakiej liczby zazyna sie zakres: ")
od = input()
od = int(od)
print("Podaj do jakiej liczby konczy sie zakres: ")
do = input()
do = int(do)
# print("Podaj przez jaka liczbe maja byc podielne liczby: ")opcja rozwinieta bardziej dla uzytkownika
# input = przez() porbierana liczba 
# przez = int(przez) konwertacja na calkwoite
for i in range(od,do):
    i = int(i)
    i+=1
    if i%5==0: # zamaist %5 wstawiamy  (do wersji rozszerzonej)
           print("liczba:",i)


