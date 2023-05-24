#write a program to calculate the factorial of an integer using recursion.

#INPUT:
def factorial(n):
    if n<=1:
        return 1
    else:
        return (n * factorial(n - 1))
n = int(input("enter number:"))
print(factorial(n))

#OUTPUT:
'''enter number:6
720'''