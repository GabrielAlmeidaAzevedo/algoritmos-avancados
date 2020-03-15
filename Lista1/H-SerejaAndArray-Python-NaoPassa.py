tamArr, numOp = input().split()
tamArr = int(tamArr)
numOp = int(numOp)

arr = input().split()

acc = 0
for i in range(numOp):
  line = input().split()

  if(line[0] == '1'):
    index = int(line[1]) - 1
    arr[index] = int(line[2]) - acc  

  elif(line[0] == '2'):
    acc += int(line[1]) 
    
  else: 
    index = int(line[1]) - 1
    print(int(arr[index]) + acc)