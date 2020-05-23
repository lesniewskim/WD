lista = {"ogorek luz.": "szt", "mleko": "litr"  ,"banan": "kg" , "bulki": "szt"}
produkt = {klucz: wartosc for klucz, wartosc in lista.items() if wartosc == "szt"}
print(produkt)