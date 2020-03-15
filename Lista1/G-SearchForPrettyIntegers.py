tamanhos = input()
tl1, tl2 = tamanhos.split()

lista1 = input().split()
lista1 = set(map(int, lista1))
lista2 = input().split()
lista2 = set(map(int, lista2))

ambos = lista1 & lista2

if(len(ambos) != 0): print(min(ambos))
else:
  min1 = min(lista1)
  min2 = min(lista2)
  if(min1 < min2 ): print(str(min1) + str(min2))
  else: print(str(min2) + str(min1))


''' 
9 1
5 4 2 3 6 1 7 9 8
9
'''