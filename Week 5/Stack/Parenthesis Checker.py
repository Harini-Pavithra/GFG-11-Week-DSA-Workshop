Parenthesis Checker

Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.

Example 1:

Input:
{([])}

Output: 
true

Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balaced pairs, with 0 number of 
unbalanced bracket.
Example 2:

Input: 
()

Output: 
true

Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.
Example 3:

Input: 
([]

Output: 
false

Explanation: 
([]. Here square bracket is balanced but 
the small bracket is not balanced and 
Hence , the output will be unbalanced.
Your Task:
This is a function problem. You only need to complete the function ispar() that takes a string as a parameter and returns a boolean value true if brackets are balanced else returns false. The printing is done automatically by the driver code.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 32000

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

Solution:

Function Arguments :
		@param  : s (given string containing parenthesis) 
		@return : boolean True or False
'''
def ispar(x):
    # code here
    stack = [] # our stack to be used, initially empty

    for char in s:
        if char in ['{','[','('] : # check if the bracket is opening
            stack.append(char) # push it in the stack

        else:       # compare current char with top of stack, it should be complementary to it.
            
            if len(stack) == 0: # if no unmatched opening char present before this.
                return False
                
            if char == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
            return False  # if control reaches here, means pair is mismatched
            
    if len(stack): # if after traversing string completely, some opening present in stack
        return False
    return True
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends