'''
Input
The first line of input consists of a single integer T, denoting the number of integers in Kostya's list.

Then, there are T lines, each of them contain a single integer from the list.

Output
Output T lines. Each of these lines should contain the number of occurences of the digit 4 in the respective integer from Kostya's list.
'''

t=int(input())
while t>0:
    a1=0
    n=input()
    for i in n:
        if int(i)==4:
            a1+=1
    print(a1)
    t=t-1
