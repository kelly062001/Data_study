import sys

input = sys.stdin.readline
num_list = []
n, m = map(int, input().split())
sum_list = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    prefix_num = list(map(int, input().split()))
    num_list.append(prefix_num)


for i in range(n + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            sum_list[i][j] = 0
        elif i == 1 and j == 1:
            sum_list[i][j] = num_list[i - 1][j - 1]
        elif i == 1:
            sum_list[i][j] = num_list[i - 1][j - 1] + sum_list[i][j - 1]
        elif j == 1:
            sum_list[i][j] = num_list[i - 1][j - 1] + sum_list[i - 1][j]
        else:
            sum_list[i][j] = (
                sum_list[i - 1][j]
                + sum_list[i][j - 1]
                - sum_list[i - 1][j - 1]
                + num_list[i - 1][j - 1]
            )

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    answer = (
        sum_list[x2][y2]
        - sum_list[x1 - 1][y2]
        - sum_list[x2][y1 - 1]
        + sum_list[x1 - 1][y1 - 1]
    )
    print(answer)
