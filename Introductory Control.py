Problem Statement- I
Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.

Steps to Follow: 
Understand how net run rate getting calculated (Cite the reference in submission comment)
Follow the computational thinking process.
Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
Design Controls -  Compound Statements and Suites
Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)
Problem Statement- II
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2

#Problem1
def T1(a,b,c,d):
    
    NRR = (a/b) - (c/d)
    return NRR
def T2(a,b,c,d):
    
    NRR = (a/b) - (c/d)
    return NRR
a = int(input("Total runs scored by Team 1: "))
b = int(input("Total overs played by Team 1: "))
c = int(input("Total runs scored against Team 1"))
d = int(input("Total overs played against Team 1"))
print("Team 1 has net run rate: ",T1(a,b,c,d))
p = int(input("Total runs scored by Team 2: "))
q = int(input("Total overs played by Team 2: "))
r = int(input("Total runs scored against Team 2"))
s = int(input("Total overs played against Team 2"))
print("Team 2 has net run rate: ",T1(p,q,r,s))
if T1(a,b,c,d) > T2(p,q,r,s):
    print("Team 1 has higher Net Run Rate than Team 2")
elif T1(a,b,c,d) < T2(p,q,r,s):
    print("Team 1 has lower Net Run Rate than Team 2")
elif T1(a,b,c,d) == T2(p,q,r,s):
    x = int(input("Enter total number of wins of Team 1: "))
    y = int(input("Enter total number of wins of Team 2: "))
    if x>y:
        print("Team 1 will top the points table")
    else:
        print("Team 2 will top the points table")
        
#Problem 2
Nint = 28
Div = 1
s = 0

while Div < Nint:
    if Nint % Div == 0:
        s += Div
    Div += 1

if s > Nint:
    print(Nint,"is an abundant number")
elif s < Nint:
    print(Nint,"is a deficient number")
else:
    print(Nint,"is a perfect number")
