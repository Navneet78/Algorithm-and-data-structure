'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
'''

from collections import OrderedDict 
for _ in range (int(input())):
    n, target = map (int, input().split())
    array = list(map(int, input().split()))
    sum_array = OrderedDict()
    current_sum = 0
    for c, x in enumerate(array):
        sum_array[current_sum+x]=c
        current_sum+=x
    flag= 0
    if (target in sum_array):
        print("1 {}".format(sum_array[target]+1))
        flag=1
    else:
        for key in sum_array:
            if target+key in sum_array:
                print("{} {}".format(sum_array[key]+2, sum_array[target+key]+1 ))
                flag=1
                break
    if (flag==0):
        print("-1")