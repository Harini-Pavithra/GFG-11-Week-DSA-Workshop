Reverse words in a given string 

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i
Example 2:

Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole
string , the input string becomes
mno.pqr

Your Task:
You dont need to read input or print anything. Complete the function reverseWords() which takes string S as input parameter and returns a string containing the words in reversed order. Each word in the returning string should also be separated by '.' 


Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)


Constraints:
1 <= |S| <= 2000


Solution
# User function Template for python3

def reverseWords(S):
    # code here 
    lst=[]
    a=0
    b=0
    for i in range(len(S)):
        if S[i] == '.':
            b=i
            word = S[a:b]
            a=i+1
            lst.append(word)
            # print(word)
    #last word
    lst.append(S[a:])
    # print(lst)
    finalstr=""
    for i in range(len(lst)-1,-1,-1):
        finalstr = finalstr +lst[i] + "."
    # print(finalstr)
    finalstr = finalstr[0:len(finalstr)-1]
    # print(finalstr)
    return finalstr



#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))

# } Driver Code Ends