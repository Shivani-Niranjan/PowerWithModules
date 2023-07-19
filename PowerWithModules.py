'''
You are given A, B and C .
Calculate the value of (A ^ B) % C

Input 1:
A = 2 B = 3 C = 3

Input 2:
A = 5 B = 2 C = 4

Output 1: 2

Output 2: 1
'''

a, b, c = [int(i) for i in input().split()]
ans = 1
for i in range(b):
    ans *=a

print((ans) % c)
