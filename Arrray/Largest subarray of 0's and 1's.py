'''
Given an array of 0's and 1's your task is to complete the function maxLen which returns size of the largest sub array with equal number of 0's and 1's. The function maxLen takes 2 arguments. The first argument is the array A[] and second argument is the size 'N' of the array A[].

Input:
The first line of the input is T denoting the number of test cases. Then T test cases follow . Each test case contains two lines. The first line of each test case is a number N denoting the size of the array and in the next line are N space separated values of A [].

Output:
For each test case output in a new line the max length of the subarray.

Constraints:
1 <= T <= 100
1 <= N <= 100
0 <= A[] <= 1

Example:
Input
2
4
0 1 0 1
5
0 0 1 0 0

Output
4
2

Explanation:
Testacase 1: The array from index [0...3] contains equal number of 0's and 1's. Thus maximum length of subarray having equal number of 0's and 1's is 4.
'''
def maxLen(n, lis):
    #code here
    lis = [-1 if x==0 else x for x in lis]
    Sum = 0
    right_array = list()
    left_array = list()
    for i in lis:
        right_array.append(Sum+i)
        Sum=Sum+i
    total= right_array[-1]
    prev  = 0
    h_t = dict()
    for k,i in enumerate(right_array):
        if i not in h_t:
            h_t[i] = [k]
        else:
           h_t[i].append(k)
    max_len = 0
    for k in h_t:
        if(len(h_t)==1):
            continue
        else:
            max_len = max(max_len, h_t[k][-1]-h_t[k][0])
        if(k==0):
            max_len = max(max_len , h_t[k][-1]+1)
    return max_len

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n, arr))