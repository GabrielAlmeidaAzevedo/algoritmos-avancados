limMin, limMax, number = input().split()
limMin = int(limMin)
limMax = int(limMax)
number = int(number)

index = 0
powered = []
while(number**index <= limMax):
  if(number**index >= limMin):
    powered.append(number**index)
  index += 1

if(len(powered) < 1): print(-1)
else:
  result = ""
  for i in range(len(powered)):
    result = result + str(powered[i])
    if(i < len(powered) -1): result = result + " "

  print(result)


