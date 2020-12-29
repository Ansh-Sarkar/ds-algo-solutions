import itertools

A = [input() for i in range(10)]
horizontal, vertical = [], []
for lst in (horizontal, vertical):
  for row in range(10):
    for c, g in itertools.groupby(range(10), key=lambda x: A[row][x]):  
      l = list(g)
      if c == '-' and len(l) > 1:
        lst.append([row, l[0], l[-1]])
  A = list(map(list, zip(*A)))

intersections = [(i, column[0] - row[1], j, row[0] - column[1]) \
                 for i, row in enumerate(horizontal) for j, column in enumerate(vertical) \
                 if row[1] <= column[0] <= row[2] and column[1] <= row[0] <= column[2]]

words = input().split(';')
result = None
for l in itertools.permutations(words, len(words)):
  if all(len(l[i]) == horizontal[i][2] - horizontal[i][1] + 1 for i in range(len(horizontal))) and \
     all(len(l[i + len(horizontal)]) == vertical[i][2] - vertical[i][1] + 1 for i in range(len(vertical))) and \
     all(l[i[0]][i[1]] == l[i[2] + len(horizontal)][i[3]] for i in intersections):
    result = l
    break

for i, x in enumerate(horizontal):
  A[x[0]][x[1]:x[2]+1] = result[i]
A = list(map(list, zip(*A)))
for i, x in enumerate(vertical):
  A[x[0]][x[1]:x[2]+1] = result[i + len(horizontal)]
A = list(map(list, zip(*A)))

print(*(''.join(x) for x in A), sep='\n')