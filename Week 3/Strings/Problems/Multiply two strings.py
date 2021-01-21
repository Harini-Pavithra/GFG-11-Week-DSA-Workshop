Multiply two strings 

Given two numbers as stings s1 and s2 your task is to multiply them.

Example 1:

Input:
s1 = 33
s2 = 2
Output: 66
Example 2:

Input:
s1 = 11
s2 = 23
Output: 253
Your Task:

You are required to complete the function multiplyStrings() which takes two strings s1 and s2 as its only argument and returns their product as strings.

 

Expected time complexity: O( n1 * n2 )
Expected auxiliary space: O( n1 + n2 ) ; where n1 and n2 are sizes of strings s1 and s2 respectively.

 

Constraints:
1 <= length of s1 and s2 <= 103


Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

Solution

#User function Template for python3

def multiplyStrings(a,b):
    # code here
    # return the product string
    if a=='0' or b=='0':
        return '0'
    
    negative = False
    if a[0]=='-':
        negative = not negative
        a = a[1:]
    
    if b[0]=='-':
        negative = not negative
        b = b[1:]
    
    product = [ 0 for _ in range(len(a)+len(b)) ]
    
    for i in range( len(b)-1, -1, -1 ):
        digit1 = int(b[i])
        carry = 0
        
        for j in range( len(a)-1, -1, -1 ):
            digit2 = int(a[j])
            
            product[i+j+1] += digit1 * digit2 + carry
            carry = product[i+j+1] // 10
            product[i+j+1] = product[i+j+1] % 10
        
        nextIndex = i
        while carry:
            product[nextIndex] += carry
            carry = product[nextIndex] // 10
            product[nextIndex] = product[nextIndex] % 10
            nextIndex -=1
    
    res = ''.join(str(x) for x in product)
    
    zeroes = 0
    while zeroes<len(res)-1 and res[zeroes]=='0':
        zeroes+=1
    res = res[zeroes:]
    
    if negative:
        res = '-' + res
    
    return res
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(multiplyStrings( a.strip() , b.strip() ))

# } Driver Code Ends