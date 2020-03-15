numPart = int(input())
parts = input().split()

parts = set(parts)
parts.discard('0')

print(len(parts))