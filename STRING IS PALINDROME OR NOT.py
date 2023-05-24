#python program to check if a string is palindrome or not.


#INPUT:
def isPalindrome(s):
    return s == s[::-1]
s = "radar"
x = isPalindrome(s)

if x:
    print("palindrome string")
else:
    print("not palindrome string")


#OUTPUT:
'''palindrome string'''

