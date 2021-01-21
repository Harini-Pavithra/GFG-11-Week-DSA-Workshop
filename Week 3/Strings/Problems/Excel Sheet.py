Excel Sheet | Part - 1 

Given a positive integer N, return its corresponding column title as it would appear in an Excel sheet.
For N =1 we have column A, for 27 we have AA and so on.

Note: The alphabets are all in uppercase.

Example 1:

Input:
N = 51
Output: AY
Your Task:
Complete the function ExcelColumn() which takes N as input and returns output string.

Expected Time Complexity: O(Log(N))
Expected Auxiliary Space: O(Log(N))

Constraints:
1 ≤ N ≤ 107

Solution

#User function Template for python3

def ExcelColumn(n):
    # To store result (Excel column name)
    s=''

    # To store current index in str which is result
    i = 0

    while n > 0:
        # Find remainder
        rem = n % 26

        # if remainder is 0, then a
        # 'Z' must be there in output
        if rem == 0:
            s+='Z'
            i += 1
            n = (n // 26) - 1
        else:
            s+=chr((rem - 1) + ord('A'))
            i += 1
            n = n // 26
    
    return s[::-1]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        print(ExcelColumn(n))

# } Driver Code Ends