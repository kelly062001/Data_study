# 1940
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
ing_list = list(map(int, input().split()))

ing_list.sort()

start = 0
end = n - 1
count = 0

while start < end:
    if (ing_list[start] + ing_list[end]) < m:
        start += 1
    elif (ing_list[start] + ing_list[end]) > m:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)
