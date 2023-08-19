# 1253

import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
new_num_list = [num_list[0], num_list[1]]

count = 0
for i in range(3, n + 1):
    start = 0
    end = n - 1
    while start < end:
        if (num_list[start] + num_list[end]) < i:
            start += 1
        elif (num_list[start] + num_list[end]) > i:
            end -= 1
        else:
            count += 1
            new_num_list.append(i)
            break

print(count)
