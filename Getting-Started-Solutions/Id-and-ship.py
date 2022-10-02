'''
Problem
Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

Class ID	Ship Class
B or b	BattleShip
C or c	Cruiser
D or d	Destroyer
F or f	Frigate
Input
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains a character.

Output
For each test case, display the Ship Class depending on ID, in a new line.
'''

t=int(input())
while t>0:
    a=input()
    if a=='b' or a=='B':
        print("BattleShip")
    elif a=='c' or a=='C':
        print("Cruiser")
    elif a=='d' or a=='D':
        print("Destroyer")
    else:
        print("Frigate")
    t=t-1
