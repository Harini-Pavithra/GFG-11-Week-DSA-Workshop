Coin Change - Minimum number of coins 

You are given an amount denoted by value. You are also given an array of coins. The array contains the
denominations of the give coins. You need to find the minimum number of coins to make the change for value using the coins of given denominations. Also, keep in mind that you have infinite supply of the coins.

Example 1:

Input:
value = 5
numberOfCoins = 3
coins[] = {3,6,3}
Output: Not Possible
Explanation:We need to make the change for
value = 5 The denominations are {3,6,3}
It is certain that we cannot make 5 using
any of these coins.
Example 2:

Input:
value = 10
numberOfCoins = 4
coins[] = {2 5 3 6}
Output: 2
Explanation:We need to make the change for
value = 10 The denominations are {2,5,3,6}
We can use two 5 coins to make 10. So
minimum coins are 2.
Your Task:
You only need to complete the function minimumNumberOfCoins() that take array of coins, size of array, and value as parameters. You need to return the minimum number of coins required. If it is not possible to make the exact value out of the given coin denominations, return -1 ("Not Possible" will be printed by the driver's code in this case).

Expected Time Complexity: O(number of coins * value).
Expected Auxiliary Space: O(value)

Constraints:
1 <= value <= 103
1 <= numberOfCoins <= 103
1 <= coinsi <= 1000

Solution

class Solution:
    #Function to find the minimum number of coins to make the change 
    #for value using the coins of given denominations.
    def minimumNumberOfCoins(self,coins,numberOfCoins,value):
        
        minimumNumberOfCoinsRequired=[99999999]*(value+1)
        minimumNumberOfCoinsRequired[0]=0
        
        for coin in coins:
            #running a loop from 1 to value.
            for i in range(1,value+1):
                if(i>=coin):
                    #taking minimum of coins required for current index and 
                    #coins required for (i-coin value)+1.
                    minimumNumberOfCoinsRequired[i]=min(minimumNumberOfCoinsRequired[i],minimumNumberOfCoinsRequired[i-coin]+1)
        
        
        #if value cannot be obtained from the coin set then returning -1.
        #else returning minimum coins required to make the value.
        if (minimumNumberOfCoinsRequired[value] == 99999999):
            return -1
        return minimumNumberOfCoinsRequired[value]


#{ 
#Driver Code Starts.

def main():
    testcases=int(input())
    while(testcases>0):
        value=int(input())
        numberOfCoins=int(input())
        coins=[int(x) for x in input().strip().split()]
        answer=Solution().minimumNumberOfCoins(coins,numberOfCoins,value)
        print("Not Possible") if answer == -1 else print(answer)
        testcases-=1

if __name__=="__main__":
    main()
    
#} Driver Code Ends