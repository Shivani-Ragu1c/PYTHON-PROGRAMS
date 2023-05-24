#write a program to check whether it is palindrome or not.

#INPUT:
num = input("Enter a number:")
if num == num[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#OUTPUT:
'''Enter a number:886688
palindrome'''