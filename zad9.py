
print("Podaj liczbe : ")

liczba = input()
i = 0

while i<len(liczba): 
    
    i+=1  
    liczba = int(liczba)
    suma +=liczba[i]

print("Suma cyfr tworzacych podana liczbe to: " , suma)
