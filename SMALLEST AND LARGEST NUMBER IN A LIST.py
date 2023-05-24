#python program to find smallest and largest number in a list.

#INPUT:
list = [50, 24, 36, 20, 85]
list.sort()
print("Smallest number:",list[0])
print("largest number:",list[-1])

#OUTPUT:
'''Smallest number: 20
largest number: 85'''


#OR

#INPUT:
list = [50, 24, 36, 20, 85]
print("Smallest number:",min(list))
print("largest number:",max(list))

#OUTPUT:
'''Smallest number: 20
largest number: 85'''