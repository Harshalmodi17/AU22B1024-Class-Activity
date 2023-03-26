Complete the Following Exercises.
You are free to use any IDE.

Steps Involved:
1. Understand a Problem (Make it clear through Instructor)

2. Understand Inputs

3. Understand Output 

4.Understand the Constraints

5.Code 

6. Validate  

 

Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)

#Arithmetic
a = float(input())
b = float(input())
sum = a + b
print("The sum of two entered number is:",sum)
diff = a - b
print("The difference of two entered number is:",diff)
mult = a*b
print("Multiplication of two entered number is:",mult)
div = a/b
print("Division of two entered number is:",div)
mod = a%b
print("Remainder of two entered number is:",mod)
exp = a**b
print("Exponent of two entered number is:",exp)
fd = a//b
print("Floor division of two entered number is:",fd)

#Conversion
#Micrometer to meter
um = float(input()) 
m = um*pow(10,-6)
print(m)

#Astronomical unit to meter
AU = float(input())
mt = AU*1.496*pow(10,11)
print(mt)

#Earthquake Impact
a = float(input())
if 1.0<=a<2:
    print("Micro")
elif 2<=a<4:
    print("Minor")
elif 4<=a<5:
    print("Light")
elif 5<=a<6:
    print("Moderate")
elif 6<=a<7:
    print("Strong")
elif 7<=a<8:
    print("Major")
elif 8<=a<10:
    print("Great")

#Factor
T = float(input("Enter temperature in degree Celsius:"))
V = float(input("Enter wind speed in Kmph:"))
WC = 13.12 + 0.6215 * T * ((0.3965 * T) - 11.37) * V**0.16
print(WC)