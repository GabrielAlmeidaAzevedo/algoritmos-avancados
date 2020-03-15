number = int(input())
digits = [9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(digits)):
  if(number % digits[i] == 0):
    complemento = " {0}".format(digits[i])
    resp = str(digits[i]) + (((number // digits[i]) - 1) * complemento)

    print(number // digits[i])
    print(resp)
    break