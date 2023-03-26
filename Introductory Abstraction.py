Complete the Exercises - Representing Abstraction Through Code 
In programming, we deal with two kinds of elements: functions and data. 

Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 

By the concept of abstraction create functions representing abstracting principles through function 

Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)

def arth(a,b):
    c = a + b
    print("The sum of two numbers is:",c)
    q = a-b
    print("The subtraction of two number is:",q)
    e = a**b
    print("Exponention of entered two number is:",e)

print(arth(a=float(input()),b=float(input())))

def sc(n):
    inches = n / 2.54
    feet = inches / 12
    yards = feet / 3
    return (inches, feet, yards)
print(sc(n=int(input())))

def earthquake(n):
    if 1.0 <= n < 2:
        return "Micro"
    elif 2 <= n < 4:
        return "Minor"
    elif 4 <= n < 5:
        return "Light"
    elif 5 <= n < 6:
        return "Modernte"
    elif 6 <= n < 7:
        return "Strong"
    elif 7 <= n < 8:
        return "Major"
    elif 8 <= n < 10:
        return "Great"

n = float(input())
print(earthquake(n))


def wc(T,V):
    WC = 13.12 + 0.6215 * T * ((0.3965 * T) - 11.37) * (V**(0.16))
    return WC
T = float(input("Enter temperature in degree Celsius:"))
V = float(input("Enter wind speed in Kmph:"))
print(wc(T,V))