'''
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .

Output:
For each test case print the length of longest  common subsequence of the two strings .

Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100

Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS of "ABC" and "AC" is "AC" of length 2
'''


# code
def LCS(str1, str2, m, n):
    lcs = [[0 for x in range(m+1)] for y in range(n+1)]
    s1 = list(str1)
    s2 = list(str2)
    print(lcs)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (s1[j-1] == s2[i-1]):
                lcs[i][j] = 1+lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[n][m]




for _ in range(int(input())):
    m, n = map(int, input().split())
    str1 = input()
    str2 = input()
    sol = LCS(str1, str2, m, n)
    print(sol)

'''
Recursive LCS
'''

# def LCS(str1, str2, m, n):
#     if (m==0 or n == 0):
#         return 0
#     elif (str1[m-1] == str2[n-1]):
#         return (1+LCS(str1, str2, m-1, n-1))
#     else:
#         return max(LCS(str1, str2, m-1, n), LCS(str1, str2, m, n-1))
#
# str1 = "ABCDGH"
# str2 = "AEDFHR"
# print(LCS(str1, str2, 6,6))