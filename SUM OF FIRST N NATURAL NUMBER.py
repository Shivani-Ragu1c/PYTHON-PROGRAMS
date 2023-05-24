#python program for sum of first n natural number.

#INPUT:
def sumofsquares(n):
    if n<0:
     pass
    sum = n*(n+1)*(2*n+1) //6
    return int(sum)

n = int(input("Enter n:"))
sum = sumofsquares(n)
print(sumofsquares(n))

#OUTPUT:
'''Enter n:2
5'''

#OR

#INPUT:
n=int(input("enter number:"))
sum=0
for i in range(1,n+1):
    sum+=i**2
    print(sum)

#OUTPUT:
'''enter number:2
1
5'''

#OR

#INPUT:
def squaresum(n):
    return(n*(n+1)*(2*n+1)) //6
n = int(input("Enter number:"))
print(squaresum(n))

#OUTPUT:
'''Enter number:2
5'''

#OR

#INPUT:
def squaresum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i**2)
    return sum
n = int(input("Enter number:"))
print(squaresum(n))

#OUTPUT:
'''Enter number:2
5'''