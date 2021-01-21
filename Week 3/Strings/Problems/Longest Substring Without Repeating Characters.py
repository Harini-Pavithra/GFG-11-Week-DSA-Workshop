Longest Substring Without Repeating Characters 

Given a string S, find the length of its longest substring that does not have any repeating characters.

Example 1:

Input:
S = geeksforgeeks
Output: 7
Explanation: The longest substring
without repeated characters is "ksforge".
Example 2:

Input:
S = abbcdb
Output: 3
Explanation: The longest substring is
"bcd". Here "abcd" is not a substring
of the given string.
Your Task:
Complete SubsequenceLength function that takes string s as input and returns the length of the longest substring that does not have any repeating characters.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints: 
0<= N <= 10^5
here, N = S.length

Solution

#User function Template for python3
def SubsequenceLength(s):
    if (len(s) == 0 ):
            return 0

    count = 1 # length of current substring 
    answer = 1 # result 


    ''' Define the visited array to represent all 
    256 ASCII characters and maintain their last 
    seen position in the processed substring.
    Initialize the array as -1 to indicate that 
    no character has been visited yet. '''
    visited = [-1]*256
    
    ''' Mark first character as visited by storing the index  
    of first character in visited array. '''
    
    visited[ord(s[0])]=0;

    '''Start from the second character. ie- index 1 as 
    the first character is already processed. '''
    for end in range(1,len(s)):
        idx = ord(s[end])

        ''' If the current character is not present in the  
        already processed string or it is not part of the 
        current non-repeating-character-string (NRCS), 
        increase count by 1 '''
        
        if(visited[idx] == -1 or end-count > visited[idx]):
            count+=1

        # If current character is already present in NRCS
        else:
            ''' check whether length of the previous 
            NRCS was greater than answer or not '''
            answer = max(count, answer)

            ''' update NRCS to start from the next 
            character of the previous instance. '''
            count = end - visited[idx]
            
        # update the index of current character in visited array
        visited[idx]=end
    return max(count,answer)



#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    s = input()
    print(SubsequenceLength(s))
    
# } Driver Code Ends