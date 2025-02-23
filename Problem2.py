# Problem 2 : Find Largest Value in Each Tree Row
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # checking if the root is None
        if root is None:
            return []
        # queue for storing the node for level wise
        queue = deque([root])
        # variable to store the maximum value for each level 
        answer = []

        # traverse until the queue is not empty
        while queue:
            # intialize the maxValue to negative infinity
            currentMax = float('-inf')
            # size of the queue
            size = len(queue)
            # loop the level of the tree
            for i in range(size):
                num = queue.popleft()
                # checking the maximum number for the level with the current maximum and store in the currentMax number
                currentMax = max(currentMax, num.val)
                # check if the node has left child and if there is child node then add the node to queue
                if num.left:
                    queue.append(num.left)
                # check if the node has right child and if there is child node then add the node to queue
                if num.right:
                    queue.append(num.right)
            answer.append(currentMax)
        return answer

        