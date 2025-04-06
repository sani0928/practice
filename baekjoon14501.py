import sys;sys.stdin=open('baekjoon14501.txt')
input = sys.stdin.readline

N = int(input())
check = {}
schedule = []
for i in range(1,N+1):
    days, profit = map(int,input().split())
    start_day = i
    end_day = start_day + days
    schedule.append((start_day, end_day, profit))

schedule.sort(key = lambda x : x[1])


day = 1
wallet = 0
for start,end,money in schedule:

    if day <= start and end <= N+1:
        day = end
        wallet += money

print(wallet)