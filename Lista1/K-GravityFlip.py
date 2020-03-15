numCols = int(input())
quntCol = list(map(int, input().split()))

quntCol.sort()
result = ""
for index in range(numCols):
  result += str(quntCol[index])
  if (index < numCols - 1):
    result += " "

print(result)