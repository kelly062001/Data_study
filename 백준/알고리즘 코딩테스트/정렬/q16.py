# 2750
import sys

input = sys.stdin.readline

n = int(input())
num_list = []
for i in range(n):
    new_num = int(input())
    num_list.append(new_num)

for j in range(n):
    for i in range(0, n - j - 1):
        if num_list[i] > num_list[i + 1]:
            temp = num_list[i]
            num_list[i] = num_list[i + 1]
            num_list[i + 1] = temp

for i in range(n):
    print(num_list[i])
