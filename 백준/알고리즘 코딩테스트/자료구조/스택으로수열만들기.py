# 1874

n = int(input())
num_list = []
for i in range(0, n):
    k = int(input())
    num_list.append(k)
print(num_list)
stack_list = [1]
stack_num = 1
result = True
answer_list = ""
i = 0
while len(stack_list) > 0:
    if num_list[i] > stack_num:
        stack_list.append(stack_num)
        print("num_list", num_list[i])
        print(stack_list, stack_num)
        answer_list = answer_list + "+\n"
        stack_num += 1
        result = True
    elif num_list[i] <= stack_num:
        n = stack_list.pop()
        print(stack_list)
        answer_list = answer_list + "-\n"
        i += 1
        result = True

        if n > stack_num:
            print("NO")
            result = False
            break

if result == True:
    print(answer_list)
