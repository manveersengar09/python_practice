def max(a,b,c):
    if a>=b and a>=c:
        return a 
    elif b>=a and b>=c:
        return b
    else:
        return c
    
#call fxn
num1 = int(input("enter first number :- "))
num2 = int(input("enter second number :- "))
num3 = int(input("enter third number :- "))

# maximum = max(num1,num2,num3)
print(f"the maximum of three number is :- {max(num1,num2,num3)}")
