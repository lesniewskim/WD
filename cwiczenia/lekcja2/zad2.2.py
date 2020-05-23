import random
macierz = [random.sample(range(1, 99), 1) for _ in range(4)]
for wiersz in macierz:        
        print(macierz)

        przekatna = []
for i in range(len(macierz)):
        przekatna.append(macierz[i][i])
        print(przekatna)

