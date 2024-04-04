"""
We have a two-dimensional board game involving snakes.  The board has two types of squares on it: +'s represent impassable squares where snakes cannot go, and 0's represent squares through which snakes can move.

Snakes may move in any of four directions - up, down, left, or right - one square at a time, but they will never return to a square that they've already visited.  If a snake enters the board on an edge square, we want to catch it at a different exit square on the board's edge.

The snake is familiar with the board and will take the route to the nearest reachable exit, in terms of the number of squares it has to move through to get there. Note that there may not be a reachable exit.

Here is an example board:

    col-->        0  1  2  3  4  5  6  7  8
               +---------------------------
    row      0 |  +  +  +  +  +  +  +  0  0
     |       1 |  +  +  0  0  0  0  0  +  +
     |       2 |  0  0  0  0  0  +  +  0  +
     v       3 |  +  +  0  +  +  +  +  0  0
             4 |  +  +  0  0  0  0  0  0  +
             5 |  +  +  0  +  +  0  +  0  +

Write a function that takes a rectangular board with only +'s and O's, along with a starting point on the edge of the board, and returns the coordinates of the nearest exit to which it can travel.  If there is a tie, return any of the nearest exits.
-----------------------------------------------------
Sample inputs:

queue = dequeue()
visited = set()

board1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
          ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
          ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
          ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
          ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
          ['+', '+', '0', '+', '+', '0', '+', '0', '+']]
start1_1 = (2, 0) # Expected output = (5, 2) 
start1_2 = (0, 7) # Expected output = (0, 8)
start1_3 = (5, 2) # Expected output = (2, 0) or (5, 5)
start1_4 = (5, 5) # Expected output = (5, 7)

board2 = [['+', '+', '+', '+', '+', '+', '+'],
          ['0', '0', '0', '0', '+', '0', '+'],
          ['+', '0', '+', '0', '+', '0', '0'],
          ['+', '0', '0', '0', '+', '+', '+'],
          ['+', '+', '+', '+', '+', '+', '+']]
start2_1 = (1, 0) # Expected output = null (or a special value representing no possible exit)
start2_2 = (2, 6) # Expected output = null 

board3 = [['+', '0', '+', '0', '+',],
          ['0', '0', '+', '0', '0',],
          ['+', '0', '+', '0', '+',],
          ['0', '0', '+', '0', '0',],
          ['+', '0', '+', '0', '+']]
start3_1 = (0, 1) # Expected output = (1, 0)
start3_2 = (4, 1) # Expected output = (3, 0)
start3_3 = (0, 3) # Expected output = (1, 4)
start3_4 = (4, 3) # Expected output = (3, 4)

board4 = [['+', '0', '+', '0', '+',],
          ['0', '0', '0', '0', '0',],
          ['+', '+', '+', '+', '+',],
          ['0', '0', '0', '0', '0',],
          ['+', '0', '+', '0', '+']]
start4_1 = (1, 0) # Expected output = (0, 1)
start4_2 = (1, 4) # Expected output = (0, 3)
start4_3 = (3, 0) # Expected output = (4, 1)
start4_4 = (3, 4) # Expected output = (4, 3)

board5 =  [['+', '0', '0', '0', '+',],
           ['+', '0', '+', '0', '0',],
           ['+', '0', '0', '0', '0',],
           ['+', '0', '0', '0', '+']]
start5_1 = (0, 1) # Expected output = (0, 2)
start5_2 = (3, 1) # Expected output = (3, 2)
start5_3 = (1, 4) # Expected output = (2, 4)

board6 = [['+', '+', '+', '+', '+', '+', '+', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '+'],
          ['+', '+', '+', '+', '+', '+', '0', '+']]

start6_1 = (4,0) # Expected output = (1, 0)

All test cases:
findExit(board1, start1_1) => (5, 2)
findExit(board1, start1_2) => (0, 8)
findExit(board1, start1_3) => (2, 0) or (5, 5)
findExit(board1, start1_4) => (5, 7)
findExit(board2, start2_1) => null (or a special value representing no possible exit)
findExit(board2, start2_2) => null
findExit(board3, start3_1) => (1, 0)
findExit(board3, start3_2) => (3, 0)
findExit(board3, start3_3) => (1, 4)
findExit(board3, start3_4) => (3, 4)
findExit(board4, start4_1) => (0, 1)
findExit(board4, start4_2) => (0, 3)
findExit(board4, start4_3) => (4, 1)
findExit(board4, start4_4) => (4, 3)
findExit(board5, start5_1) => (0, 2)
findExit(board5, start5_2) => (3, 2)
findExit(board5, start5_3) => (2, 4)
findExit(board6, start6_1) => (1, 0)

Complexity Analysis:

r: number of rows in the board
c: number of columns in the board
"""

board1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
           ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
           ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
           ['+', '+', '0', '+', '+', '0', '+', '0', '+']]
start1_1 = (2, 0) # Expected output = (5, 2) 
start1_2 = (0, 7) # Expected output = (0, 8)
start1_3 = (5, 2) # Expected output = (2, 0) or (5, 5)
start1_4 = (5, 5) # Expected output = (5, 7)

board2 = [['+', '+', '+', '+', '+', '+', '+'],
           ['0', '0', '0', '0', '+', '0', '+'],
           ['+', '0', '+', '0', '+', '0', '0'],
           ['+', '0', '0', '0', '+', '+', '+'],
           ['+', '+', '+', '+', '+', '+', '+']]
start2_1 = (1, 0) # Expected output = null (or a special value representing no possible exit)
start2_2 = (2, 6) # Expected output = null 

board3 = [['+', '0', '+', '0', '+'],
           ['0', '0', '+', '0', '0'],
           ['+', '0', '+', '0', '+'],
           ['0', '0', '+', '0', '0'],
           ['+', '0', '+', '0', '+']]
start3_1 = (0, 1) # Expected output = (1, 0)
start3_2 = (4, 1) # Expected output = (3, 0)
start3_3 = (0, 3) # Expected output = (1, 4)
start3_4 = (4, 3) # Expected output = (3, 4)

board4 = [['+', '0', '+', '0', '+'],
           ['0', '0', '0', '0', '0'],
           ['+', '+', '+', '+', '+'],
           ['0', '0', '0', '0', '0'],
           ['+', '0', '+', '0', '+']]
start4_1 = (1, 0) # Expected output = (0, 1)
start4_2 = (1, 4) # Expected output = (0, 3)
start4_3 = (3, 0) # Expected output = (4, 1)
start4_4 = (3, 4) # Expected output = (4, 3)

board5 = [['+', '0', '0', '0', '+'],
           ['+', '0', '+', '0', '0'],
           ['+', '0', '0', '0', '0'],
           ['+', '0', '0', '0', '+']]
start5_1 = (0, 1) # Expected output = (0, 2)
start5_2 = (3, 1) # Expected output = (3, 2)
start5_3 = (1, 4) # Expected output = (2, 4)


board6 = [['+', '+', '+', '+', '+', '+', '+', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '+'],
          ['+', '+', '+', '+', '+', '+', '0', '+']]

start6_1 = (4, 0) # Expected output = (1, 0)

          
from dataclasses import dataclass

@dataclass
class Lanes:
    rows: list
    columns: list
    
# O(2*c*r)
# Space: c+r

def findPassableLanes(board: list) -> Lanes:
    assert(len(board) > 0)
    result = Lanes(rows=[], columns=[])
    
    rows_n = len(board)
    columns_n = len(board[0])
    for row_i in range(rows_n):
        for column_i in range(columns_n):
            if board[row_i][column_i] != '0':
                break
        else:
            result.rows.append(row_i)        
    
    for column_i in range(columns_n):
        for row_i in range(rows_n):
            if board[row_i][column_i] != '0':
                break
        else:
            result.columns.append(column_i)
            
    return result
    
from collections import deque 

def findExit(board, start_point):
    rows_n = len(board)
    cols_n = len(board[0])
    visited = set()
    queue = deque()
    queue.append(start_point)
    
    while queue:
        # print(queue.popleft())
        row, col = queue.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        if (row == 0 or row == rows_n - 1 or col == 0 or col == cols_n - 1) and (row, col)  != start_point:
            return (row, col)
            
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows_n and 0 <= new_col < cols_n and (new_row, new_col) not in visited and board[new_row][new_col] == '0':
                queue.append((new_row, new_col))
    return None
    
    
print(findExit(board1, start1_1)) # => (5, 2)
print(findExit(board1, start1_2)) # => (0, 8)
print(findExit(board1, start1_3)) # => (2, 0) or (5, 5)
print(findExit(board1, start1_4)) # => (5, 7)
print(findExit(board2, start2_1)) # => null (or a special value representing no possible exit)
print(findExit(board2, start2_2)) # => null
print(findExit(board3, start3_1)) # => (1, 0)
print(findExit(board3, start3_2)) # => (3, 0)
print(findExit(board3, start3_3)) # => (1, 4)
print(findExit(board3, start3_4)) # => (3, 4)
print(findExit(board4, start4_1)) # => (0, 1)
print(findExit(board4, start4_2)) # => (0, 3)
print(findExit(board4, start4_3)) # => (4, 1)
print(findExit(board4, start4_4)) # => (4, 3)
print(findExit(board5, start5_1)) # => (0, 2)
print(findExit(board5, start5_2)) # => (3, 2)
print(findExit(board5, start5_3)) # => (2, 4)
print(findExit(board6, start6_1)) # => (1, 0)