Coin Change - Number of ways

You have an infinite supply of coins, each having some value. Find out the number of ways to use the coins to sum-up to a certain required value.

Example 1:

Input:
value = 4
numberOfCoins = 3
coins[] = {1,2,3}
Output: 4
Explanation: We need to make the change
for value = 4. The denominations are
{1,2,3} Change for 4 can be made:
1+1+1+1
1+1+2
1+3
2+2
So, as it is evident, we can do this in
4 ways.
Example 2:

Input:
value = 10
numberOfCoins = 4
coins[] = {2,5,3,6}
Output: 5
Your Task:
This is a function problem where you've to complete the funcion numberOfWays (). You are given an amount denoted by value. You are also given an array of coins. The array contains the denominations of the given coins. You need to return the number of ways you can make the change for value using the coins of given denominations. Also, keep in mind that you have an infinite supply of coins.
Note:  Try not to editing the part of the code provided to you in the function. Just complete the function as it has been described.

Expected Time Complexity: O(Number of Coins * Value).
Expected Auxiliary Space: O(Value).

Constraints:
1 <= value <= 103
1 <= numberOfCoins <= 103
1 <= coinsi <= 1000

Solution

class Solution:
    
    #Function to find out the number of ways to use the coins to
    #sum up to a certain required value.
    def numberOfWays(self,coins,numberOfCoins,value):
        
        #creating an array for storing number of ways.
        ways=[0]*(value+1)
        #initializing number of ways at 0 to 1.
        ways[0]=1 
        
        #running a loop on the list of coin denominations.
        for coin in coins: 
            #running a loop from 1 to value.
            for i in range(1,value+1):
                
                #if coin value is less than or equal to ith value.
                if(i>=coin): 
                    
                    #updating number of ways at ith 
                    #index as ways[i]+ways[i-coin].
                    ways[i]=ways[i]+ways[i-coin]
                    
        #returning the number of ways.
        return ways[value]

#{ 
#Driver Code Starts.

def main():
    testcases=int(input())
    while(testcases>0):
        value=int(input())
        numberOfCoins=int(input())
        coins=[int(x) for x in input().strip().split()]
        print(Solution().numberOfWays(coins,numberOfCoins,value))
        testcases-=1

if __name__=="__main__":
    main()
    
#} Driver Code Ends