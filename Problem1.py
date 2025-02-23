# Problem 1 : Valid Sudoku
# Time Complexity : O(n^2)
# Space Complexity : O(n^2)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Creating a boolean matrix for storing the visited values of rows, columns
        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        # Creating a boolean matrix for storing the visited values for 3*3 matrix
        boxSquare = [[False] * 9 for _ in range(9)]

        # Iterating over matrix
        for i in range(9):
            for j in range(9):
                cellValue = board[i][j]
                # if the cell is empty then will skip this cell
                if cellValue == ".":
                    continue
                # Convert the number string to int and adjust to zero index
                currNum = int(cellValue) - 1
                # Calculate the box index for 3*3 square matrix using division method
                boxIndex = (i//3) * 3 + (j//3)

                # Checking if the current number is present in the rows, column and square matrix boolean variable
                # if it is present then board is not valid sudoku
                if rows[i][currNum] or columns[j][currNum] or boxSquare[boxIndex][currNum]:
                    return False
                # setting the value in the rows, columns and square matrix
                rows[i][currNum] = True
                columns[j][currNum] = True
                boxSquare[boxIndex][currNum] = True
                # else the board is valid sudoku
        return True
 
        