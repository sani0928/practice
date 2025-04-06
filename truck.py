import sys;sys.stdin=open('truck.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int,input().split())
        lst.append([s, e])

    lst.sort(key=lambda x:x[1])

    time = 0
    cnt = 0

    for s, e in lst:

        if time == lst[-1][1]:
            break

        if time <= s:
            cnt += 1
            time = e

    print(f'#{tc} {cnt}')
