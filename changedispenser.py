# Author: Lemfon Karl Ndze'dzenyuy
# Date: 13/01/2019
# Intent: This is an implementation of my proposed solution to the change dispenser problem in the Programming Challenges book
# Problem 3 of the getting started problems

num = int(input("Please enter the number of students: "))
expenses = input("Enter the individual expenses seperated by spaces: ").split()
print(expenses)
for i in range(len(expenses)):
    expenses[i] = float(expenses[i])
print(expenses)
totaL = sum(expenses)
remainder = totaL/num
totalOwed = 0
for x in expenses:
    if x > remainder:
        totalOwed += x - remainder
print(totalOwed)
