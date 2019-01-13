# Author: Lemfon Karl Ndze'dzenyuy
# Date: 13/01/2019
# Intent: This is an implementation of my proposed solution to the minesweeper problem in the Programming Challenges book

# Function that checks the number of mines arround a particluar position
def mineCountSingle(arr,i,j,n,m): # Passing the array, the position of the current element and the dimensions of the array into the funtion
    count = 0 # initializing the mineCountSingle
    if (i != n-1) and (i != 0) and (j != m-1) and (j != 0): # ensuring the element is not on the border
        for v in range(i-1,i+2):
            for h in range(j-1,j+2):
                if (arr[v][h] == '*') and ((v != i) and (h != j)):
                    count += 1
    else:
        # Taking the cases when the element under consideration is on the edge i.e i = 0, and j=0 or j = m-1 or j=m-1 and i =0 or i = n-1
        if (i == 0) and (j == 0):
            for v in range(i,i+2):
                for h in range(j,j+2):
                    if (arr[v][h] == '*') and ((v != i) and (h != j)):
                        count += 1
        elif (i == 0) and (j == m-1):
            for v in range(i,i+2):
                for h in range(j,j-2,-1):
                    if (arr[v][h] == '*') and ((v != i) and (h != j)):
                        count += 1
        elif (i == n-1) and (j == 0):
            for v in range(i,i-2,-1):
                for h in range(j,j+2):
                    if (arr[v][h] == '*') and ((v != i) and (h != j)):
                        count += 1
        elif (i == n-1) and (j == m-1):
            for v in range(i,i-2,-1):
                for h in range(j,j-2,-1):
                    if (arr[v][h] == '*') and ((v != i) and (h != j)):
                        count += 1
        elif i == 0:
            for v in range(i-1,i+2):
                for h in range(j,j+2):
                    if (arr[v][h] == '*') and ((v != i) and (h != j)):
                        count += 1
        elif j == 0:
            for v in range(i-1,i+2):
                for h in range(j,j-2,-1):
                    if (arr[v][h] == '*') and ((v != i) and (h != j)):
                        count += 1
        # The function returns the number of mines adjeacent to a position
        return count

arr1 = [ ['*', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '*', '.', '.'],
        ['.', '.', '.', '.']
]

print(mineCountSingle(arr1,2,3,4,4))
