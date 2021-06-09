#!/usr/bin/env python
# coding: utf-8

# In[1]:


size = 9

sudoku = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]

def print_sudoku():
    for i in sudoku:
        print(i)

def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0,size):
        for j in range (0,size):
            #cell is unassigned
            if sudoku[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

def is_safe(n, r, c):
    #checking in row
    for i in range(0,size):
        if sudoku[r][i] == n:
            return False
    #checking in column
    for i in range(0,size):
        if sudoku[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
    #checking the submatrix
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if sudoku[i][j]==n:
                return False
    return True

def solve_sudoku():
    row = 0
    col = 0
    
    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    for i in range(1,10):
        
        if is_safe(i, row, col):
            sudoku[row][col] = i
            if solve_sudoku():
                return True
            
            sudoku[row][col]=0
    return False

if solve_sudoku():
    print_sudoku()
else:
    print("No solution")


# In[ ]:




