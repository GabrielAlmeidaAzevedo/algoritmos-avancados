numCities = int(input())
cities = input().split()

for index in range(len(cities)):
  cities[index] = int(cities[index])

for index in range(len(cities)):
  minCost = 0
  maxCost = 0
  if(index == 0):
    minCost = abs(cities[index] - cities[1])
    maxCost = abs(cities[index] - cities[numCities - 1])
  elif(index == numCities - 1):
    minCost =  abs(cities[index] - cities[index - 1])
    maxCost = abs(cities[index] - cities[0])
  else:
    min1 = abs(cities[index] - cities[index + 1]) 
    min2 = abs(cities[index - 1] - cities[index])
    minCost = min(min1, min2)

    max1 = abs(cities[numCities - 1] - cities[index])
    max2 = abs(cities[0] - cities[index])
    maxCost = max(max1, max2)

  print(minCost, maxCost)

