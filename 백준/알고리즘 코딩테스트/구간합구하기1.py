import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

new_num_list = [0]
temp = 0

for i in num_list:
    temp += i
    new_num_list.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(new_num_list[b] - new_num_list[a - 1])
