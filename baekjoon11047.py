import sys;sys.stdin=open('baekjoon11047.txt')
input = sys.stdin.readline

N, K = map(int,input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)

goal = 0
total_num = 0
for i in lst:

    if K == 0:
        break

    if goal == K:
        break

    if i <= K:

        coin_num = K//i

        K -= i*coin_num
        total_num += coin_num

print(total_num)