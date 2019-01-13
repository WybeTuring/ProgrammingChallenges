# Author: Lemfon Karl Ndze'dzenyuy
# Date: 13/01/2019
# Intent: This is an implementation of my proposed solution to the 3n+1 problem in the Programming Challenges book

#This function generates the numbers as specified by the question from a given number
def generator(num):
    count = 1 #since the element itself is always included in the list
    while num > 1:
        if num % 2 == 0:
            num = num //2
            count += 1
        else:
            num = (3*num) + 1
            count += 1
    return count;

# Function that determines the largest cycle length
def cyclen(num1,num2):
    max = 1
    for i in range(num1,num2+1):
        if (generator(i) > max):
            max = generator(i)
    return max

n = input("Please enter the numbers: ")
n = n.split()
# Changing the type of the values to intergers
for i in range(0,len(n)):
    n[i] = int(n[i])

answer = cyclen(n[0],n[1])
# printing in the required format
print(str(n[0]) + '\t' + str(n[1]) + '\t' + str(answer))
