def factorial(n):
    if n<0:
        return " this number is less than 0 ,so we can't find it's factorial"
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# call fxn
num = int(input("ENTER A NUMBER :- "))
print(f"the factorial of {num} is {factorial(num)} ")