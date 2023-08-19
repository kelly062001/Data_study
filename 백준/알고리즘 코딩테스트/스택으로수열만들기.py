n = int(input())
num_list = []
for i in range(0, n):
    k = int(input())
    num_list.append(k)
print(num_list)
stack_list = [1]
stack_num = 1
i = 0
while len(stack_list) > 0:
    if num_list[i] > stack_num:
        stack_list.append(stack_num)
        print("num_list", num_list[i])
        print(stack_list, stack_num)
        print("+")
        stack_num += 1
    elif num_list[i] <= stack_num:
        stack_list.pop()
        print(stack_list)
        print("-")
        i += 1
        if len(stack_list) == 0:
            break

    if len(stack_list) == 0:
        print("NO")
