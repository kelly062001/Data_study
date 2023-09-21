from collections import Counter
import sys

input = sys.stdin.readline
p, s = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

count = 0
start_count = Counter(dna[0:s])
A = start_count["A"]
C = start_count["C"]
T = start_count["T"]
G = start_count["G"]
if A >= a and C >= c and G >= g and T >= t:
    count += 1
for i in range(0, p - s):
    start = i
    new_start = i + s
    if dna[start] == "A":
        A = A - 1
    elif dna[start] == "C":
        C = C - 1
    elif dna[start] == "T":
        T = T - 1
    else:
        G = G - 1
    # print("A C T G ")
    # print(A, C, T, G, start)

    if dna[new_start] == "A":
        A = A + 1
    elif dna[new_start] == "C":
        C = C + 1
    elif dna[new_start] == "T":
        T = T + 1
    else:
        G = G + 1
    # print("A C T G ")
    # print(A, C, T, G, new_start)

    if A >= a and C >= c and G >= g and T >= t:
        count += 1


print(count)
