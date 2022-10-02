'''
Problem
The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.

Input
The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.

Output
Write a single integer to output, denoting how many integers ti are divisible by k.
'''

# cook your dish here
n,k=map(int, input().split())
a1=[]
for i in range(1,n+1):
    i=int(input())
    if i%k==0:
        a1.append(i)
print(len(a1))
