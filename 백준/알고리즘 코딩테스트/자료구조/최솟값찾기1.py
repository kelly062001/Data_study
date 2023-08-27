import sys

input = sys.stdin.readline
n, l = map(int, input().split())
a = list(map(int, input().split()))

new_list = []
answer_list = []
min = a[0]
for i in range(0, n):
    if i < l:
        new_list.append(a[i])
        if min >= a[i]:
            min = a[i]
        answer_list.append(min)
    else:
        new_list.append(a[i])
        if min >= a[i]:
            min = a[i]
        new_list.pop(0)

        answer_list.append(min)

print(answer_list)
