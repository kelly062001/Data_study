## 백준 10986
import sys

input = sys.stdin.readline
sum_remain_list = [0]

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
remain_list = [0] * m


sum_num = 0
for i in range(n):
    sum_num = num_list[i] + sum_num
    sum_num = sum_num % m
    sum_remain_list.append(sum_num)

for i in range(n + 1):
    k = sum_remain_list[i]
    remain_list[k] += 1

answer = 0
for i in range(m):
    if remain_list[i] > 1:
        answer = answer + (remain_list[i] * (remain_list[i] - 1) // 2)
print(answer)
