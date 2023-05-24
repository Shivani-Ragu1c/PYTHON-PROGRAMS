#python program to print even length words in a string.

#INPUT:
str="I am from AIADS branch"
s=str.split(" ")
for i in s:
  if len(i)%2==0:
    print(i)


#OUTPUT:
'''am
from
branch'''

#OR

#INPUT:
def printWords(s):
    s = s.split(" ")
    for word in s:
        if len(word)%2==0:
            print(word)
s = "i am from vidisha"
printWords(s)


#OUTPUT:
'''am
from'''

#OR

#INPUT:
str="I am Shivani Raghuwanshi"
s=str.split(" ")
print([i for i in s if len(i)%2==0])


#OUTPUT:
'''['am']'''


