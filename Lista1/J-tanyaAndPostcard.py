desejadas = input()
recortadas = input()

YAY = 0
WHOOPS = 0
desejo = {}
possuo = {}
for rec in desejadas:
  if(rec not in desejo):
    desejo[rec] = 1
  else:
    desejo[rec] += 1

for rec in recortadas:
  if(rec not in possuo):
    possuo[rec] = 1
  else:
    possuo[rec] += 1

for chave in desejo:
  if(chave in possuo):
    minimo = min(desejo[chave], possuo[chave])
    desejo[chave] -= minimo
    possuo[chave] -= minimo
    YAY += minimo

if(len(desejo) < len(possuo)):
  for chave in desejo:
    if(chave.isupper()): chaveCase = chave.lower()
    else: chaveCase = chave.upper()
    if(chaveCase in possuo):
      minimo = min(desejo[chave], possuo[chaveCase])
      desejo[chave] -= minimo
      possuo[chaveCase] -= minimo
      WHOOPS += minimo

else:
  for chave in possuo:
    if(chave.isupper()): chaveCase = chave.lower()
    else: chaveCase = chave.upper()
    if(chaveCase in desejo):
      minimo = min(desejo[chaveCase], possuo[chave])
      desejo[chaveCase] -= minimo
      possuo[chave] -= minimo
      WHOOPS += minimo

print(str(YAY) + " " + str(WHOOPS))

