# write a python program to read a file line by line and print it.


# INPUT:

# by using readlines()
L= ["python\n", "lab\n", "work\n"]

f1 = open('myfile.txt', 'w')
f1.writelines(L)
f1.close()

f1 = open('myfile.txt', 'r')
lines = f1.readlines()

count = 0
for line in lines:
    count += 1
    print(count,line)



# by using readline()
L= ["python\n", "lab\n", "work\n"]

f1 = open('myfile.txt', 'w')
f1.writelines((L))
f1.close()

f1 = open('myfile.txt', 'r')
lines = f1.readline()
count = 0
for line in lines:
    count += 1
    print(count,line)



# by using read()
L= ["python\n", "lab\n", "work\n"]

f1 = open('myfile.txt', 'w')
f1.writelines((L))
f1.close()

f1 = open('myfile.txt', 'r')
lines = f1.read()
count = 0
for line in lines:
    count += 1
    print(count,line)



# using for loop
L= ["python\n", "lab\n", "work\n"]

f1 = open('myfile.txt', 'w')
f1.writelines(L)
f1.close()

f1 = open('myfile.txt', 'r')
count = 0
for line in f1:
    count += 1
    print(count,line)

f1.close()


# OUTPUT:

'''1 python

2 lab

3 work

1 p
2 y
3 t
4 h
5 o
6 n
7

1 p
2 y
3 t
4 h
5 o
6 n
7

8 l
9 a
10 b
11

12 w
13 o
14 r
15 k
16

1 python

2 lab

3 work'''
