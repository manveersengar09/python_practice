##find the greatest common divisor (GCD) of two numbers with or without any module.


# find G.C.D.(GREATEST COMMON DIVISOR )without any module

def gcd(a,b):
    while b!=0:
        a,b=b,a % b
    return a 
num1 = int(input("ENTER A NUMBER :- ".upper()))
num2 = int(input("enter a number :- ".upper()))
print(f"the GCD of {num1} and {num2} is {gcd(num1,num2)}")

# find G.C.D.(GREATEST COMMON DIVISOR )with MATH module

import math

num1 = int(input("enter first number :- ").upper())
num2 = int(input("enter second number :- ").upper())

print(f"the GCD of {num1} and {num2} is {math.gcd}")