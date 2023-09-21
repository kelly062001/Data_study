from collections import deque

n = int(input())
if n == 1:
    print(1)
    exit()

num_deque = deque(range(1, n + 1))

while True:
    n = num_deque.popleft()
    l = num_deque.popleft()
    num_deque.append(l)
    if len(num_deque) == 1:
        print(num_deque[0])
        break
