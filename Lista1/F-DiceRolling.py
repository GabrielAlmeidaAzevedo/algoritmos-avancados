numQueries = int(input())

for i in range(numQueries):
  num = int(input())

  if(num <= 7): print(1)
  else: print(num // 2)
