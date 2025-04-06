import sys;sys.stdin=open('mine.txt')
from collections import deque

def bfs(r, c):

    q = deque()
    q.append((r,c))
    visited[r][c] = True

    while q:

        cr, cc = q.popleft()
        if neardy_mine_num[cr][cc] == 0:
            for dr,dc in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == '.':
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr,nc))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0

    matrix = [list(input()) for _ in range(N)]
    neardy_mine_num = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '*':
                continue
            for dr,dc in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if matrix[nr][nc] == '*':
                        neardy_mine_num[r][c] += 1

    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '.' and neardy_mine_num[r][c] == 0:
                if not visited[r][c]:
                    bfs(r,c)
                    cnt += 1

    # 남은 '.' 중 방문표시가 안된 칸 카운팅
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '.' and not visited[r][c]:
                cnt += 1

    print(f'#{tc} {cnt}')




