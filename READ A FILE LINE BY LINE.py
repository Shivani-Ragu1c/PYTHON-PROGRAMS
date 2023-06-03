
# by using readlines()

L= ["python\n", "lab\n", "work\n"]

# write a file
f1 = open('myfile.txt', 'w')
f1.writelines(L)
f1.close()

# open a file
f1 = open('myfile.txt', 'r')
lines = f1.readlines()

count = 0
for line in lines:
    count += 1
    print(count,line)





# by using readline()

L= ["python\n", "lab\n", "work\n"]

# Write a file
f1 = open('myfile.txt', 'w')
f1.writelines((L))
f1.close()

# open a file
f1 = open('myfile.txt', 'r')
lines = f1.readline()
count = 0
for line in lines:
    count += 1
    print(count,line)




# by using read()

L= ["python\n", "lab\n", "work\n"]

# Write a file
f1 = open('myfile.txt', 'w')
f1.writelines((L))
f1.close()

# open a file
f1 = open('myfile.txt', 'r')
lines = f1.read()
count = 0
for line in lines:
    count += 1
    print(count,line)



# using for loop

L= ["python\n", "lab\n", "work\n"]

# Write a file
f1 = open('myfile.txt', 'w')
f1.writelines(L)
f1.close()

# opening file
f1 = open('myfile.txt', 'r')
count = 0
for line in f1:
    count += 1
    print(count,line)

# close a file
f1.close()