import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
num_list = deque([])
for i in range(n):
    k=int(input())
    num_list.append(k)
    
for i in range(5):
    queue0=deque