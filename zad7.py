    # print("Podaj ile liczb bedziesz potegowac: ")
    # ile = input()
    # ile = int(ile)
    # i=0
    # while True:
    #     i+=1
    #     liczba = input()
    #     liczba = int (liczba)
    #     if i == ile:
    #         break
    #     else:
    #         print("kwadraty liczb: ",i,liczba*liczba) -- wersja robocza



while True:

    print("Podaj liczbe: ")
    liczba = input()
    liczba = int(liczba)
    a = liczba*liczba
    print("potega z liczby",liczba ,"wynosi: ",a)
    print("Liczymy dalej Y/N: ")

    b = input()

    if b == 'n' :
        print("Koniec pracy Programu") 
        break 