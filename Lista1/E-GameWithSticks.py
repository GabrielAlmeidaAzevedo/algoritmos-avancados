hor, ver = input().split(" ")
hor = int(hor)
ver = int(ver)
minimum = min(hor, ver)
if(minimum % 2 == 0): print("Malvika")
else: print("Akshat")