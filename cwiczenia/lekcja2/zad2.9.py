a1 = 1
r = 1
ile = 10
def spr(a1,r,ile):
    iloczyn=a1
    i=1
    while i < ile:
        iloczyn *= a1+i
        i += 1
    return iloczyn
print(spr(a1,r,ile))