'''
Problem
Given an Integer N, write a program to reverse it.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
For each test case, display the reverse of the given number N, in a new line.
'''

# cook your dish here
t=int(input())
while t>0:
    n=input()
    print(int(n[::-1]))
    t=t-1
