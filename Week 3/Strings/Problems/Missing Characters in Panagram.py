Missing Characters in Panagram 

You are given a string s. You need to find the missing characters in the string to make a panagram.
Note: The output characters will be lowercase and lexicographically sorted.

 

Example 1:

Input:
s = Abcdefghijklmnopqrstuvwxy
Output: z
 

Example 2:

Input:
s = Abc
Output: defghijklmnopqrstuvwxyz
 

Your Task:

You only need to complete the function misssingPanagram() that takes s as parameter and returns -1 if the string is a panagram, else it returns a string that consists missing characters.

 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

 

Constraints:
1 <= |s| <= 10000

Solution

#User function Template for python3

"""
input - 
@s = given string 

output - 
return -1 or required ans
"""
#User function Template for python3

"""
input - 
@s = given string 

output - 
return -1 or required ans
"""
MAX_CHAR = 26

def missingPanagram(s):
        # A boolean array to store characters
    # present in string.
    present = [False for i in range(MAX_CHAR)]

    # Traverse string and mark characters
    # present in string.
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
            present[ord(s[i]) - ord('a')] = True
        elif (s[i] >= 'A' and s[i] <= 'Z'):
            present[ord(s[i]) - ord('A')] = True

    # Store missing characters in alphabetic
    # order.
    res = ""

    for i in range(MAX_CHAR):
        if (present[i] == False):
            res += chr(i + ord('a'))

    return res




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(missingPanagram(s))
        t = t-1

# } Driver Code Ends