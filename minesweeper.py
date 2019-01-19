# Author: Lemfon Karl Ndze'dzenyuy
# Date: 13/01/2019
# Intent: This is an implementation of my proposed solution to the minesweeper problem in the Programming Challenges book

import numpy
arr1 = numpy.array( [['*', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '*', '.', '.'],
        ['.', '.', '.', '.']]
)

arr2 = numpy.array([
['*','*','.','.','.'],
['.','.','.','.','.'],
['.','*','.','.','.']
])
print("This is the first dude")
# Function that checks the number of mines arround a particluar position
def mineCount(arr,i,j,m,n):  # The arguments of the funtion are the matrix, i and j for the current position, and m and n for the dimensions
    count = 0
    if j-1 >=0: # Ensuring that j-1 does not exceed the size of the mining board
        if arr[i][j-1] == '*':
            count += 1
        if i-1 >=0:
            if arr[i-1][j-1] == '*':
                count += 1
        if i+1<=m-1:
            if arr[i+1][j-1] == '*':
                count += 1
    if j+1<=n-1:
        if arr[i][j+1] == '*':
            count += 1
        if i-1>= 0:
            if arr[i-1][j+1] == '*':
                count += 1
        if i+1 <= m-1:
            if arr[i+1][j+1] == '*':
                count += 1
    if i+1 <= m-1:
        if arr[i+1][j] == '*':
            count += 1
    if i-1 >= 0:
        if arr[i-1][j] == '*':
            count += 1
    return count
# Trying for the first test
dimensions = arr1.shape
answer = []
for r in range(dimensions[0]):
    temp = []
    for s in range(dimensions[1]):
        if arr1[r][s] == '*':
            temp.append('*')
        else:
            temp.append(mineCount(arr1,r,s,dimensions[0],dimensions[1]))
    answer.append(temp)
# Printing the answer in an appropriate manner
print("This is the result of the first test")
for i in range(len(answer)):
    print(answer[i])

# Tring for the second test
dimensions2 = arr2.shape
answer = []
for r in range(dimensions2[0]):
    temp = []
    for s in range(dimensions2[1]):
        if arr2[r][s] == '*':
            temp.append('*')
        else:
            temp.append(mineCount(arr2,r,s,dimensions2[0],dimensions2[1]))
    answer.append(temp)
# Printing the answer in an appropriate manner
print("This is the result for the second test")
for i in range(len(answer)):
    print(answer[i])
