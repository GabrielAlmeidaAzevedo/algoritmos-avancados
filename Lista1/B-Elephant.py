coordinate = int(input()) 
steps = (coordinate // 5)
if (coordinate % 5 != 0): steps += 1
print(steps)