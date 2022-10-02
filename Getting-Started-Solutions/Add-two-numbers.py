'''
Problem
Problem Statement
Every problem starts with a Problem Statement. It tells you in detail about the task to be solved.
Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.

The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

Input Format
This section tells you the format in which your program should receive the input.
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

Output Format
This section tells us the format in which your program should give the output
For each test case, add A and B and display the sum in a new line.

Everything your program prints is considered “output”, so if you output some debugging statements like “Please enter T”, this will be considered as part of your answer, 
and because it does not satisfy the output format, it will be marked wrong, even if your answer is otherwise correct!
'''

# cook your dish here
t=int(input())
while t>0:
    a,b=map(int, input().split())
    print(a+b)
    t=t-1
