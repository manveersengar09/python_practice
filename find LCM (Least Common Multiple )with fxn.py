def gcd(a,b):
    while b !=0:
        a,b=b,a%b
    return a 

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
#INPUT
a = int(input("enter a number:- ".upper()))
b = int(input("enter a number:- ".upper()))

print(f"lcm of {a} and {b} is :- {lcm(a,b)}".upper())