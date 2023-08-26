n = int(input())
if n == 1:
    print(1)
    exit()

num_list = list(range(2, n + 1, 2))

while True:
    n = num_list.pop(0)
    l = num_list.pop(0)
    num_list.append(l)
    if len(num_list) == 1:
        print(num_list[0])
        break
