def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b,w):
    global cost

    root_a = find(a)
    root_b = find(b)

    if root_a in spot and root_b in spot:
        return

    cost += w

    if root_a in spot:
        parent[root_b] = root_a

    else:
        parent[root_a] = root_b

N, M, K = map(int,input().split())
spot = set(map(int,input().split()))
edges = []
parent = [i for i in range(N+1)]
cost = 0

for _ in range(M):
    u,v,w = map(int,input().split())
    edges.append((w,u,v))

edges.sort()

for w,u,v in edges:

    if find(u) != find(v):
        union(u,v,w)

    if all(find(parent[i]) in spot for i in range(1, N+1)):
        print(cost)
        break