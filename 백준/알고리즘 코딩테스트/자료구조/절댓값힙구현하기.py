# 11286

import sys
from queue import PriorityQueue

print = sys.stdout.write
input = sys.stdin.readline
n = int(input())

myQueue = PriorityQueue()

for i in range(0, n):
    k = int(input())
    if k == 0:
        if myQueue.empty():
            print("0\n")
        else:
            temp = myQueue.get()
            print(str((temp[1])) + "\n")
    else:
        myQueue.put(abs(k), k)
