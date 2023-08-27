# 1427

n = input()
num_list = list(map(int, n))
len_n = len(n)

for i in range(len_n - 1):
    max_num = num_list[i]
    for j in range(i, len_n):
        if max_num <= num_list[j]:
            max_num = num_list[j]
            k = j
    temp = num_list[i]
    num_list[i] = max_num
    num_list[k] = temp

for i in range(len_n):
    print(num_list[i], end="")
