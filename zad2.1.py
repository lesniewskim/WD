A = [1/x for x in range(1,11)]
print(A)
B = [2**n for n in range(1,11)]
print(B)
C = {x: x for x in B if x % 4 == 0}
print(C)
