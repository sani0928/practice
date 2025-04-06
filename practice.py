import sys;sys.stdin=open('practice.txt')
import math

def calculator(p1,p2):
    return math.sqrt((abs(p1[0] - p2[0]))**2 + (abs(p1[1] - p2[1]))**2)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    points = [list(map(int,input().split())) for _ in range(N)]
    edges = []
    parent = [i for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            w = calculator(points[i], points[j])
            edges.append((w,i,j))

    edges.sort(key = lambda x:x[0])

    total = 0
    for w,u,v in edges:
        if find(u) != find(v):
            union(u,v)
            total += w

    print(f'#{tc} {total:.2f}')
