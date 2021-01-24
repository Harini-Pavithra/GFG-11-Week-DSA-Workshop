Evaluation of Postfix Expression 

Given string S representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like *, /, + and -.

 

Example 1:

Input: S = "231*+9-"
Output: -4
Explanation:
After solving the given expression, 
we have -4 as result.
 

Example 2:

Input: S = "123+*8-"
Output: -3
Explanation:
After solving the given postfix 
expression, we have -3 as result.

Your Task:
You do not need to read input or print anything. Complete the function evaluatePostfixExpression() that takes the string S denoting the expression as input parameter and returns the evaluated value.


Expected Time Complexity: O(|S|)
Expected Auixilliary Space: O(|S|)


Constraints:
1 ≤ |S| ≤ 105

Solution:
#User function Template for python3

'''
Function Arguments :
		@param  : S (given postfix expression)
		@return : return the desired value
'''
def EvaluatePostfix(S):
    #code here
    stack1=[]
    operators = ['+', '-', '*', '/', '(', ')', '^']
    for i in S:
        if i in operators:
            a = int(stack1.pop())
            b = int(stack1.pop())
            if i == '*':
                c = a * b
            elif i == '+':
                c = a + b
            elif i == '-':
                c = b - a
            elif i == '/':
                c = b//a
            else:
                print("any other optrt",i)
            stack1.append(c)
        else:
            stack1.append(i)
    # print(stack1)
    return stack1.pop()




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

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
        exp = str(input())
        print('{0:g}'.format(float(EvaluatePostfix(exp))))
# } Driver Code Ends