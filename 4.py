g = {'A': 0}  # Cost from start
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}  # Heuristic
p = {'A': None}  # Parent pointers

G = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}  # Graph

o = {'A'}  # Open set

while o:
    n = min(o, key=lambda x: g[x] + h[x])  # Node with lowest f = g + h

    if n == 'D':
        break

    o.remove(n)

    for m in G[n]:
        g[m] = g[n] + 1
        p[m] = n
        o.add(m)

# Reconstruct path
path = []
while n is not None:
    path.append(n)
    n = p[n]

print("Path:", path[::-1])
