def isPalindromo(word):
  middle = len(word) // 2
  for index in range(middle):
    if(word[index] != word[(-1 * index) - 1]):
      return False
  return True

word = input()

if(len(set(word)) == 1): print(0)
else:
  if(isPalindromo(word)): print(len(word) - 1)
  else: print(len(word))
  