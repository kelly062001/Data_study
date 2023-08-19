# 백준 2018

n = int(input())


count = 1
start_index = 1
end_index = 1
sum = start_index

while end_index != n:
    if sum < n:
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
        count += 1


print(count)
