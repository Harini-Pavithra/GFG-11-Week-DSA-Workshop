Convert to Roman No

Given an integer n, your task is to complete the function convertToRoman which prints the corresponding roman number of n. Various symbols and their values are given below.

I 1
V 5
X 10
L 50
C 100
D 500
M 1000

 

Example 1:

Input:
n = 5
Output: V
 

Example 2:

Input:
n = 3
Output: III
 

Your Task:
Complete the function convertToRoman() which takes an integer N as input parameter and returns the equivalent roman. 

 

Expected Time Complexity: O(log10N)
Expected Auxiliary Space: O(log10N * 10)

 

Constraints:
1<=n<=3999

Solution

#Your task is to complete this function 
#Your function should return a String
def convertRoman(n):
    #Code here
    strrom=[["","I","II","III","IV","V","VI","VII","VIII","IX"],
                  ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                  ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                  ["","M","MM","MMM","","","","","",""]]
    i = 0
    str=""
    while(n != 0):
        str = strrom[i][n%10] + str
        n=n//10
        i+=1
    return str




#{ 
#  Driver Code Starts
#Your Code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends