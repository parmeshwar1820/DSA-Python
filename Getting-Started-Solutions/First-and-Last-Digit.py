'''
Problem
If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

Input
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.

Output
For each test case, display the sum of first and last digits of N in a new line.
'''

t=int(input())
while t>0:
    n=input()
    print(int(n[0])+int(n[-1]))
    t=t-1
