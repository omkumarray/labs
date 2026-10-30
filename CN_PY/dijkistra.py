import heapq

n = int(input("Enter no.of edges:"))
print("Enter edges in format : node1 node2 weight")

graph = {}
for _ in range(n):
    a, b, w = input().split()
    w = int(w)
    graph.setdefault(a, []).append((b, w))
    graph.setdefault(b, []).append((a, w))

src = input("Enter source node:")
dest = input("Enter destination node:")

dist = {node: float("inf") for node in graph}
prev = {}
dist[src] = 0
pq = [(0, src)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            prev[v] = u
            heapq.heappush(pq, (dist[v], v))

if dist[dest] == float("inf"):
    print("No path found")
else:
    path = [dest]
    while path[-1] != src:
        path.append(prev[path[-1]])
    path.reverse()
    print(f"Shortest path from {src} to {dest}:")
    print("->".join(path), "with cost", dist[dest])
    
    
  
#OUTPUT- 
#Enter no.of edges:5
#Enter edges in format : node1 node2 weight
# A B 1 
# A C 4 
# B C 2
# B D 6
# C D 3
# Enter source node:A
# Enter destination node:D