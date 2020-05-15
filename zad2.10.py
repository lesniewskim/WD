lista = {"ogorek luz.": "szt", "mleko": "litr"  ,"banan": "kg" , "bulki": "szt"}
produkt = {klucz: wartosc for klucz, wartosc in lista.items() if wartosc == "szt"}

def spr(**produkt):
    return len(produkt)
def spr1(**lista):
    return len(lista)

print(spr(**produkt))
print("Ogolnie produktow jest na liscie :",spr(**lista))
