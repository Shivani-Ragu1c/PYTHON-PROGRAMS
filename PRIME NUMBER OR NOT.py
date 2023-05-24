#write a program in python to check whether its is prim or not.

#INPUT:
n=5
if n%2==1:
    print("prime number")
    'break'
else:
    print("not prime number")

#OUTPUT:
'''prime number'''

#OR

#INPUT:
n=int(input("enter number:"))
if n%2==1:
    print("prime number")
    'break'
elif n>1:
    print("niether prime nor not prime")
else:
    print("not prime number")

#OUTPUT:
'''enter number:5
prime number'''

#OR

#INPUT:
n=int(input("enter number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
           print(n,"not prime number")
           'break'
        else:
            print(n,"prime number")
else:
            print(n,"neither prime nor not prime number")

#OUTPUT:
'''enter number:5
5 prime number'''

