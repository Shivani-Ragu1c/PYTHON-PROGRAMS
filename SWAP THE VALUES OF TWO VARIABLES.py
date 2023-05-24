#write a function to swap the values of two variables.

#INPUT:
def swap():
 x = int(input("Enter value of x: "))
 y = int(input("Enter value of y: "))
 print("Before swapping a:", x)
 print("Before swapping b:", y)

 x, y = y, x
 print("After swapping a :", x)
 print("After swapping b :", y)
swap()

#OUTPUT:
'''Enter value of x: 4
Enter value of y: 8
Before swapping a: 4
Before swapping b: 8
After swapping a : 8
After swapping b : 4'''

#OR

#INPUT:
def swap():
 x =4
 y =8
 print("Before swapping:")
 print("value of x:",x,"and y:", y)

 x, y = y, x
 print("After swapping:")
 print("value of x:",x,"and y:", y)
swap()


#OUTPUT:
'''Before swapping:
value of x: 4 and y: 8
After swapping:
value of x: 8 and y: 4'''


#OR

#INPUT:
x =4
y =8
print("Before swapping:")
print("value of x:",x,"and y:", y)

x, y = y, x
print("After swapping:")
print("value of x:",x,"and y:", y)


#OUTPUT:
'''Before swapping:
value of x: 4 and y: 8
After swapping:
value of x: 8 and y: 4'''


#OR

#INPUT:
x =4
y =8
print("Before swapping:")
print("value of x:",x,"and y:", y)

x=y
y=x
x=y
print("After swapping:")
print("value of x:",x,"and y:", y)


#OUTPUT:
'''Before swapping:
value of x: 4 and y: 8'''