'''
You are in an infinite 2D grid where you can move in any of the 8 directions :
 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
 You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
 Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
Return an Integer, i.e minimum number of steps.
Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        s = 0
        for i in range(len(A)-1):
            s = s+max(abs(A[i+1]- A[i]), abs(B[i+1]- B[i]))
        return s
