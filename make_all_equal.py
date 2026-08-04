n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

found = False
M = min(a)

# Compute minimal reachable values (residues)
min_reachable = [ai % bi if bi != 0 else ai for ai, bi in zip(a, b)]

# X must be at least the maximum residue
lower_bound = max(min_reachable)

for X in range(M, lower_bound - 1, -1):
  total_steps = 0
  possible = True

  for ai, bi in zip(a, b):
    if bi == 0:
      if ai != X:
        possible = False
        break
      continue

    diff = ai - X

    if diff < 0 or diff % bi != 0:
      possible = False
      break

    total_steps += diff // bi

  if possible:
    print(total_steps)
    found = True
    break

if not found:
  print(-1)